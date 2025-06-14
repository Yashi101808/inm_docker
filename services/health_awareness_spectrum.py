import pandas as pd
import matplotlib.pyplot as plt
from fastapi.responses import StreamingResponse
import io

def get_health_awareness_chart():
    # Load the CSV file (update path as needed)
    df = pd.read_csv("KPI_Data/health_spectrum.csv")

    # Group by Health Awareness Level
    grouped = df.groupby("Health Awareness Level")["Mentions (Count)"].sum()

    # Define colors for each level
    colors = {
        "Low": "#FF6961",       # Red
        "Moderate": "#FFD700",  # Gold
        "High": "#77DD77"       # Green
    }

    # Plot pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%', colors=[colors[level] for level in grouped.index], startangle=90)
    ax.set_title("Health Awareness Spectrum")

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    return StreamingResponse(buf, media_type="image/png")
