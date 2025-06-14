import pandas as pd
import matplotlib.pyplot as plt
import io

INFLUENCE_KEYWORDS = {
    'Community Engagement': ['community'],
    'Promotions': ['discount', 'promotion', 'offer'],
    'Packaging': ['packaging'],
    'Product Quality': ['quality', 'consistency', 'freshness'],
    'Availability': ['availability', 'stock'],
    'Pricing': ['price', 'pricing', 'cost'],
    'Delivery': ['delivery', 'online ordering', 'home delivery'],
    'Recommendations': ['recommend', 'word of mouth', 'sharing'],
    'Seasonal Offers': ['festival', 'seasonal', 'diwali', 'holidays'],
    'Marketing': ['marketing', 'campaign'],
    'Health-conscious Options': ['health', 'calorie', 'healthy', 'vegan'],
    'Customer Service': ['customer service'],
    'Discount Codes': ['discount code'],
    'Innovation': ['innovation', 'new', 'launch', 'flavors'],
    'Regional Flavors': ['regional', 'local'],
    'Others': []
}

def classify_influence(text):
    text_lower = str(text).lower()
    for influence, keywords in INFLUENCE_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return influence
    return 'Others'

def load_and_process_data(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    print("Columns in CSV:", df.columns.tolist())

    # Try to use 'Key Influences/Insights', else fallback to 'Specific Feedback'
    possible_cols = ["Key Influences/Insights", "Specific Feedback", "Reaction Type"]
    target_col = None
    for col in possible_cols:
        for df_col in df.columns:
            if df_col.replace(" ", "").lower() == col.replace(" ", "").lower():
                target_col = df_col
                break
        if target_col:
            break

    if not target_col:
        raise ValueError(
            "Could not find a suitable column for influence classification. "
            f"Available columns: {df.columns.tolist()}"
        )

    df['Influence Type'] = df[target_col].apply(classify_influence)
    summary = df.groupby(['Platform', 'Influence Type']).size().reset_index(name='Count')
    return summary

def plot_kpi_bar_chart(summary_df):
    pivot_df = summary_df.pivot(index='Influence Type', columns='Platform', values='Count').fillna(0)
    ax = pivot_df.plot(kind='bar', figsize=(12,7))
    ax.set_ylabel('Number of Discussions')
    ax.set_title('Discussions by Platform and Influence Type')
    ax.legend(title='Platform')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf
