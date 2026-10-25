# Technical Report: Anti-Scraping Mitigation & Robust Data Pipeline Architecture

## 1. Executive Summary
Modern e-commerce platforms such as BestBuy Canada implement robust, multi-layered anti-bot protection systems (e.g., Akamai WAF, Cloudflare, PerimeterX, and custom behavioral fingerprinting). These systems scrutinize incoming traffic for browser automation flags, request velocity anomalies, and missing cryptographic tokens. 

This document details the architectural strategies, bypass methodologies, and fallback compliance frameworks engineered to ensure reliable review data collection while strictly adhering to ethical web scraping practices.

---

## 2. Core Obstacles & Technical Mitigations

### A. IP Blocking & Rate Limiting
* **The Obstacle**: E-commerce firewalls monitor request frequency from individual IP addresses. Exceeding threshold limits (e.g., >20 requests per minute) results in HTTP 429 (Too Many Requests) errors or permanent IP subnet bans.
* **Mitigation Strategy**: 
  * **Rotating Residential Proxy Pools**: Routing requests through a distributed network of residential proxies masks data center origin and distributes load across thousands of distinct ISP-assigned IP addresses.
  * **Request Throttling & Jitter**: Inserting randomized sleep intervals (e.g., `time.sleep(uniform(3.5, 7.2))`) breaks deterministic polling patterns, emulating natural human reading and browsing cadence.

### B. CAPTCHA & Automated Bot Detection (WAF Fingerprinting)
* **The Obstacle**: Headless browsers expose global JavaScript variables (such as `navigator.webdriver = true`) and present unique browser fingerprints (TLS handoffs, canvas rendering artifacts) that immediately trigger JavaScript challenges or CAPTCHA walls.
* **Mitigation Strategy**:
  * **Stealth Configuration Flags**: Utilizing Selenium WebDriver with experimental options (`--disable-blink-features=AutomationControlled`, disabling automation switches, and modifying `navigator.webdriver` via CDP scripts) eliminates standard automation signatures.
  * **User-Agent Rotators & Custom Headers**: Injecting realistic HTTP headers (`Accept-Language`, `Sec-Ch-Ua`, and modern desktop User-Agents) aligns automated requests with standard organic browser traffic profiles.

### C. Transient Network Errors & DOM Rendering Latency
* **The Obstacle**: Dynamic JavaScript rendering (AJAX/React hydration) often introduces race conditions where review cards fail to render before DOM parsing occurs, leading to empty data extraction.
* **Mitigation Strategy**:
  * **Explicit Waits (`WebDriverWait`)**: Replacing fixed timers with dynamic condition polling ensures scripts wait precisely until required DOM elements (e.g., `data-automation="review-card"`) are fully attached and interactive.
  * **Exponential Backoff Decorators**: Implementing decorator-based retry loops with exponential backoff handles transient HTTP 5xx errors and temporary connection drops gracefully.

---

## 3. Compliance & Ethical Data Engineering
* **Public View Limitation**: Scraping scripts strictly target publicly accessible review metadata without attempting unauthorized authentication, bypassing login barriers, or accessing private user profiles.
* **Robots.txt Adherence**: Data pipelines respect crawling etiquette, limiting concurrency and avoiding high-frequency server stress during peak operational windows.