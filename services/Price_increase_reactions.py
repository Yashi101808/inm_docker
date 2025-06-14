import pandas as pd
import matplotlib.pyplot as plt
import io

def load_reactions(csv_path):
    # Load the CSV
    df = pd.read_csv(csv_path)

    # We only need Sentiment column to classify positive vs negative
    # Let's count Positive and Negative sentiments; Neutral can be grouped separately or ignored.
    sentiment_counts = df[' Sentiment'].value_counts()

    # We'll consider only Positive and Negative (ignore Neutral or others if present)
    positive_count = sentiment_counts.get('Positive', 0)
    negative_count = sentiment_counts.get('Negative', 0)

    # Prepare data for pie chart
    labels = ['Positive', 'Negative']
    sizes = [positive_count, negative_count]

    return labels, sizes

def create_pie_chart(labels, sizes):
    plt.figure(figsize=(6,6))
    colors = ['#66b3ff', '#ff6666']  # blue for positive, red for negative
    explode = (0.1, 0)  # explode first slice (Positive) slightly

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=colors, explode=explode, shadow=True)

    plt.title("Response to Price Increase Justification - Sentiment Distribution")
    plt.axis('equal')  # Equal aspect ratio to ensure pie is circular

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf
