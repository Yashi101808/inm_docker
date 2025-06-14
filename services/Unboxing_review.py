import csv
from collections import Counter
import matplotlib.pyplot as plt
import io
from fastapi import Response

CSV_PATH = "KPI_data/Unboxing_Experience.csv"

def load_review_sentiments(file_path=CSV_PATH):
    sentiment_counts = Counter()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentiment = row["User Sentiment"].strip().lower()
            if sentiment in ("positive", "negative"):
                sentiment_counts[sentiment] += 1
    return sentiment_counts

def generate_sentiment_chart():
    sentiment_counts = load_review_sentiments()
    labels = ['Positive', 'Negative']
    values = [sentiment_counts.get('positive', 0), sentiment_counts.get('negative', 0)]

    plt.figure(figsize=(6,4))
    bars = plt.bar(labels, values, color=['#A8DADC', '#F4A261'])
    plt.title('Number of Positive and Negative Reviews')
    plt.ylabel('Count')
    plt.xlabel('Sentiment')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom')

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    return buf.getvalue()

def get_chart_response():
    img_bytes = generate_sentiment_chart()
    return Response(content=img_bytes, media_type="image/png")
