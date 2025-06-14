import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def generate_high_intent_keyword_trend_chart(csv_path):
    df = pd.read_csv(csv_path)
    # Aggregate total search volume by keyword
    keyword_totals = df.groupby('Keyword')['Search Volume'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10,6))
    keyword_totals.plot(kind='bar', color='skyblue')
    plt.title('Total Search Volume by High-Intent Keywords')
    plt.xlabel('Keyword')
    plt.ylabel('Total Search Volume')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()
