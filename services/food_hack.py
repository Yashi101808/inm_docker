import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def generate_hacktype_bar_chart(csv_path='KPI_data/food_hack_mentions.csv') -> BytesIO:
    df = pd.read_csv(csv_path)
    counts = df['Hack Type'].value_counts()

    plt.figure(figsize=(8,5))
    counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Hack Type')
    plt.ylabel('Count')
    plt.title('Hack Type Counts')
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf
