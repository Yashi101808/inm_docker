
import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_information_overload_chart():
    # Load CSV
    file_path = "KPI_data/Feedback_for_variety.csv"
    df = pd.read_csv(file_path)

    # Count occurrences of each confusion type
    confusion_counts = df['Confusion Type'].value_counts()

    # Plot
    plt.figure(figsize=(12, 6))
    bars = plt.bar(confusion_counts.index, confusion_counts.values, color='skyblue')
    plt.title("Information Overload / Simplicity Desire - Confusion Types")
    plt.xlabel("Confusion Type")
    plt.ylabel("Number of Comments")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save as PNG
    output_path = "output/information_overload_chart.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()

    return output_path
