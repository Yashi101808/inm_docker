import pandas as pd
import matplotlib.pyplot as plt
import io
from fastapi import Response

def generate_impulse_kpi_chart():
    # Load impulse purchase data CSV (update path as needed)
    df = pd.read_csv("KPI_data/impulse_purchase_Mentions.csv")

    # Group by Platform and Impulse Indicator Strength, count entries
    grouped = df.groupby(["Platform", "Impulse Indicator Strength"]).size().reset_index(name="Count")

    platforms = grouped["Platform"].unique()
    strengths = grouped["Impulse Indicator Strength"].unique()

    # Set figure size bigger for more space
    fig, ax = plt.subplots(figsize=(16, 7))

    bar_width = 0.2
    x_pos = list(range(len(platforms)))

    # Plot grouped bars by Impulse Indicator Strength for each platform
    for i, strength in enumerate(strengths):
        counts = []
        for platform in platforms:
            subset = grouped[(grouped["Platform"] == platform) & (grouped["Impulse Indicator Strength"] == strength)]
            counts.append(subset["Count"].sum() if not subset.empty else 0)
        positions = [x + bar_width * i for x in x_pos]
        ax.bar(positions, counts, bar_width, label=strength)

    ax.set_xlabel("Platform")
    ax.set_ylabel("Impulse Purchase Count")
    ax.set_title("Impulse Purchase Counts by Platform and Indicator Strength")
    ax.set_xticks([x + bar_width for x in x_pos])
    ax.set_xticklabels(platforms, rotation=45, ha='right')
    ax.legend()

    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return buf.read()
