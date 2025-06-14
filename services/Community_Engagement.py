# kpi_community_engagement.py

from fastapi import FastAPI, Response
import pandas as pd
import matplotlib.pyplot as plt
import os

app = FastAPI()

@app.get("/kpi/community-engagement", tags=["KPI"])
def community_engagement_chart():
    # Read CSV
    df = pd.read_csv("KPI_data/community_engagement.csv")
    df.fillna("None", inplace=True)

    # Group by Platform
    grouped = df.groupby("Platform").size().sort_values(ascending=False)

    # Plot chart
    plt.figure(figsize=(10, 6))
    grouped.plot(kind="bar", color="orange")
    plt.title("Community Engagement by Platform")
    plt.xlabel("Platform")
    plt.ylabel("Number of Groups")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Save PNG
    os.makedirs("static/charts", exist_ok=True)
    chart_path = "static/charts/community_engagement.png"
    plt.savefig(chart_path)
    plt.close()

    # Return PNG
    with open(chart_path, "rb") as f:
        return Response(content=f.read(), media_type="image/png")
