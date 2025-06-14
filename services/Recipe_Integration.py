import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def get_recipe_usage_figure_bytes(csv_path: str) -> bytes:
    df = pd.read_csv(csv_path)
    df = df[['Product Mentioned', 'Product Usage']].drop_duplicates()

    usage_counts = df.groupby('Product Mentioned')['Product Usage'].nunique().reset_index()
    usage_counts.columns = ['Product', 'Unique Recipe Ideas']
    usage_counts = usage_counts.sort_values(by='Unique Recipe Ideas', ascending=True)

    plt.figure(figsize=(8, 6))
    sns.barplot(
        x='Unique Recipe Ideas',
        y='Product',
        data=usage_counts,
        palette='viridis'
    )
    plt.title('Unique Recipe Integration Ideas per Product')
    plt.tight_layout()

    # Save figure to bytes
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()
