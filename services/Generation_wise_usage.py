# kpis/cross_generation_usage.py

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def generate_cross_generation_chart(csv_path: str):
    # Load the CSV
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()  # Clean column names

    # KPI: Count mentions by generation
    gen_counts = df['Generation'].value_counts()

    # Plot
    plt.figure(figsize=(8, 5))
    gen_counts.plot(kind='bar', color='skyblue')
    plt.xlabel("Generation")
    plt.ylabel("Number of Mentions")
    plt.title("Cross-Generation Usage")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save chart to memory as PNG
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return img
