# services/user_segmentation_proxy.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from fastapi import Response

def user_segmentation_proxy() -> Response:

    # 1️⃣ Load and preprocess
    df = pd.read_csv("KPI_data/user_segmentation_proxy.csv")
    df.fillna("N/A", inplace=True)
    df["Cluster_Label"] = df["Inferred User Cluster"] + " (" + df["Language Style"] + ")"

    # 2️⃣ Count occurrences
    counts = df["Cluster_Label"].value_counts().sort_values()

    # 3️⃣ Plot horizontal bar chart
    plt.figure(figsize=(10, max(6, len(counts) * 0.4)))
    counts.plot(kind="barh")
    plt.title("User Segmentation by Cluster & Language")
    plt.xlabel("Count")
    plt.ylabel("User Cluster (Language)")
    plt.tight_layout()

    # 4️⃣ Ensure output directory exists and save
    os.makedirs("static/charts", exist_ok=True)
    chart_path = "static/charts/user_segmentation.png"
    plt.savefig(chart_path)
    plt.close()

    # 5️⃣ Read back and return as PNG
    with open(chart_path, "rb") as img:
        return Response(content=img.read(), media_type="image/png")
