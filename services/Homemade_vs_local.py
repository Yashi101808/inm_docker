import pandas as pd
import matplotlib.pyplot as plt
import io

def create_chart_image() -> bytes:
    csv_path = "KPI_data/homemade_vs_local_comparison.csv"
    
    # Load your CSV file
    df = pd.read_csv(csv_path)

    # Use only the relevant columns
    df = df[["Product Category", "Comparison Type", "Sentiment"]]

    # Count combinations
    grouped = df.groupby(["Product Category", "Comparison Type", "Sentiment"]).size().reset_index(name="Count")

    # Prepare the plot
    fig, ax = plt.subplots(figsize=(18, 6))

    # Generate a grouped bar chart
    categories = grouped["Product Category"].unique()
    comparison_types = grouped["Comparison Type"].unique()
    sentiments = grouped["Sentiment"].unique()

    bar_width = 0.2
    x_pos = list(range(len(comparison_types)))

    for i, sentiment in enumerate(sentiments):
        for j, category in enumerate(categories):
            subset = grouped[(grouped["Sentiment"] == sentiment) & (grouped["Product Category"] == category)]
            counts = [subset[subset["Comparison Type"] == ct]["Count"].sum() for ct in comparison_types]
            positions = [x + bar_width * i + bar_width * j * len(sentiments) for x in x_pos]
            ax.bar(positions, counts, bar_width, label=f"{sentiment} - {category}")

    ax.set_xlabel("Comparison Type")
    ax.set_ylabel("Count")
    ax.set_title("Sentiment by Product Category and Comparison Type")
    ax.set_xticks([x + bar_width for x in x_pos])
    ax.set_xticklabels(comparison_types, rotation=45)
    ax.legend()

    # Save plot to bytes buffer
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return buf.read()
