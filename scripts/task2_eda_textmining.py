import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def run_advanced_eda_and_clustering():
    print("[*] Loading dataset for Task 2...")
    df = pd.read_csv("Hanuai_task2_assignment.csv")

    df['CAUSAL_VERBATIM'] = df['CAUSAL_VERBATIM'].fillna("No Causal Verbatim Provided")
    df['CAUSAL_CD_DESC'] = df['CAUSAL_CD_DESC'].fillna("Unspecified Cause")
    df['IN_USE_DATE'] = df['IN_USE_DATE'].fillna(df['Opened date'])

    os.makedirs("reports/figures", exist_ok=True)
    
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, y='MAKE', order=df['MAKE'].value_counts().index, hue='MAKE', palette='viridis', legend=False)
    plt.title("Distribution of Events by Vehicle Make")
    plt.xlabel("Count")
    plt.ylabel("Make")
    plt.tight_layout()
    plt.savefig("reports/figures/make_distribution.png")
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, y='COMPLAINT_CD_DESC', order=df['COMPLAINT_CD_DESC'].value_counts().index, hue='COMPLAINT_CD_DESC', palette='magma', legend=False)
    plt.title("Frequency of Complaint Categories")
    plt.xlabel("Count")
    plt.ylabel("Complaint Description")
    plt.tight_layout()
    plt.savefig("reports/figures/complaint_distribution.png")
    plt.close()

    def classify_issue(text):
        text_lower = str(text).lower()
        if 'radio' in text_lower or 'screen' in text_lower or 'display' in text_lower or 'audio' in text_lower:
            return "Audio/Display Glitch"
        elif 'communication' in text_lower or 'bus' in text_lower or 'ethernet' in text_lower or 'network' in text_lower:
            return "Communication / Bus Error"
        elif 'program' in text_lower or 'software' in text_lower or 'sps' in text_lower:
            return "Software / Programming Error"
        elif 'short' in text_lower or 'ground' in text_lower or 'power' in text_lower:
            return "Electrical / Power Issue"
        else:
            return "General Component Failure"

    df['Extracted_Issue_Category'] = df['CAUSAL_VERBATIM'].apply(classify_issue)

    print("[*] Running TF-IDF Vectorization and K-Means Clustering...")
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_tfidf = vectorizer.fit_transform(df['CAUSAL_VERBATIM'])

    optimal_clusters = 4
    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42, n_init=10)
    df['Failure_Cluster'] = kmeans.fit_predict(X_tfidf)

    cluster_labels = {
        0: "Cluster 0: Radio Internal Module Faults",
        1: "Cluster 1: Ethernet & Communication Bus Dropouts",
        2: "Cluster 2: Software Reprogramming & SPS Errors",
        3: "Cluster 3: Power Supply & Ground Circuit Faults"
    }
    df['Failure_Cluster_Label'] = df['Failure_Cluster'].map(cluster_labels)

    os.makedirs("data", exist_ok=True)
    output_path = "data/hanuai_task2_processed.csv"
    df.to_csv(output_path, index=False)
    print(f"[+] Task 2 Processing Complete. Saved processed dataset to {output_path}")

if __name__ == "__main__":
    run_advanced_eda_and_clustering()