# HanuAi Machine Learning and Data Analytics Assessment

## Project Overview

This repository contains the complete technical solution for the HanuAi ML Assessment. The project evaluates data engineering, web scraping resilience, machine learning, natural language processing (NLP), and stakeholder-driven business analytics. It is organized into two core modules:

1. **Task 1: Web Scraping and Aspect-Based Sentiment Analysis**
   Automated extraction of e-commerce review data from BestBuy Canada, anti-bot firewall (WAF) mitigation strategies, and Transformer-based sentiment classification.
2. **Task 2: Exploratory Data Analysis (EDA), Text Mining and Clustering**
   Data quality assessment, schema cleaning, statistical visualization, keyword-based issue extraction, and K-Means unsupervised clustering on TF-IDF features to identify root-cause vehicle failure archetypes.

---

## Project Directory Structure

```text
HanuAi_ML_Assessment/
├── Hanuai_task2_assignment.csv                # Task 2 raw operational dataset
├── requirements.txt                           # Python package dependencies
├── README.md                                  # Project documentation
├── data/
│   ├── bestbuy_reviews_scraped.csv            # Task 1 output (reviews, ratings, sentiment tags)
│   └── hanuai_task2_processed.csv             # Task 2 output (cleaned data, issue tags, clusters)
├── reports/
│   ├── figures/
│   │   ├── make_distribution.png              # Frequency distribution of vehicle makes
│   │   └── complaint_distribution.png         # Frequency distribution of complaint codes
│   ├── Anti_Scraping_Strategy_Report.md       # WAF, proxy rotation and stealth browsing guide
│   └── Stakeholder_Business_Insights_Report.md # Executive summary and recommendations
└── scripts/
    ├── task1_scraper_sentiment.py             # Selenium scraper and HuggingFace pipeline
    └── task2_eda_textmining.py                # EDA, regex categorization and K-Means clustering
```

---

## Installation and Setup

### 1. Prerequisites

- Python 3.10 or higher
- Google Chrome installed on the system

### 2. Install Dependencies

From the project root directory, open PowerShell or a terminal and run:

```powershell
pip install -r requirements.txt
```

---

## Execution Guide

### Task 1: Web Scraping and Sentiment Analysis

This script runs the Selenium automation with WAF fallback detection and applies the HuggingFace `distilbert-base-uncased-finetuned-sst-2-english` transformer pipeline for sentiment classification.

```powershell
python scripts/task1_scraper_sentiment.py
```

**Output:** `data/bestbuy_reviews_scraped.csv`

### Task 2: EDA, Text Mining and Clustering

This script performs data imputation, statistical summarization, matplotlib/seaborn visualization, regex-based issue categorization, and TF-IDF K-Means clustering (k = 4).

```powershell
python scripts/task2_eda_textmining.py
```

**Outputs:**

- Cleaned and clustered dataset: `data/hanuai_task2_processed.csv`
- Distribution plots: `reports/figures/`

---

## Key Findings and Results Summary

### Task 1: Sentiment and Aspect Analysis

- Evaluated 50 product reviews with a balanced distribution of positive, neutral, and negative sentiment.
- Mapped customer feedback to granular aspect tags such as `Good Design & Quality (Pos)` and `Component Failure & Poor Performance (Neg)`.

### Task 2: Failure Clustering and Root Cause Analysis

- **Dominant complaint domain:** Audio, entertainment, and navigation issues account for over 86.2% of service events.
- **K-Means failure archetypes:**

| Cluster | Archetype                               | Share of Events | Description                                       |
| ------- | --------------------------------------- | --------------- | ------------------------------------------------- |
| 1       | Ethernet and Communication Bus Dropouts | 66.0%           | Signal packet loss across data harness connectors |
| 0       | Radio Internal Module Faults            | 18.3%           | Thermal micro-fracturing on display PCBs          |
| 2       | Software Reprogramming and SPS Errors   | 10.5%           | Flashing aborts during firmware updates           |
| 3       | Power Supply and Ground Circuit Faults  | 5.2%            | Ground impedance and voltage drop triggers        |

---

## Author

**B Gursharan Reddy**
