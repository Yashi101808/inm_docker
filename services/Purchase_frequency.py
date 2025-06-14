import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "KPI_Data/purchase_frequency.csv"
PNG_FILE = "purchase_frequency_mentions.png"

def generate_purchase_frequency_chart():
    df = pd.read_csv(CSV_FILE)

    # Count how many mentions per 'Interpreted Frequency'
    freq_counts = df['Interpreted Frequency'].value_counts().sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    bars = plt.bar(freq_counts.index, freq_counts.values, color='skyblue')
    plt.title("Purchase Frequency Mentions Count")
    plt.ylabel("Number of Mentions")
    plt.xlabel("Interpreted Frequency")

    # Rotate X axis labels for readability
    plt.xticks(rotation=45, ha='right')

    # Add counts above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig(PNG_FILE, dpi=200)
    plt.close()
