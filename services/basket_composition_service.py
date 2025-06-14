import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from collections import Counter
from itertools import product
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering


def get_basket_composition_chart(csv_path: str = "KPI_Data/basket_composition.csv") -> bytes:
    df = pd.read_csv(csv_path)

    pair_counts = Counter()

    for _, row in df.iterrows():
        # Get products mentioned and other items, split by comma and strip spaces
        haldiram_items = [item.strip() for item in str(row['Haldiram Products Mentioned']).split(',')]
        other_items = [item.strip() for item in str(row['Other Items Bought Together']).split(',')]

        # Create all pairs between haldiram and other items (cross-product)
        for pair in product(haldiram_items, other_items):
            pair_counts[tuple(sorted(pair))] += 1  # sorted tuple to avoid duplicates like (A,B) and (B,A)

    # Get top 10 most common pairs
    top_pairs = pair_counts.most_common(10)
    if not top_pairs:
        return b""

    pairs = [' & '.join(pair) for pair, _ in top_pairs]
    counts = [count for _, count in top_pairs]

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(pairs[::-1], counts[::-1], color='teal')
    plt.xlabel("Number of Mentions")
    plt.title("Top 10 Frequently Co-mentioned Product Pairs")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()
