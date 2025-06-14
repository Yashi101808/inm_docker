# logic.py

import pandas as pd
import matplotlib.pyplot as plt
from fastapi.responses import FileResponse

def generate_switch_trigger_chart(csv_path='KPI_data/Brand_switching_triggers.csv', output_file='bar_chart.png'):
    # Read the CSV
    df = pd.read_csv(csv_path)

    # Count frequency of each switch trigger
    trigger_counts = df['Switch Trigger (Positive/Negative)'].value_counts()

    # Plotting
    plt.figure(figsize=(10, 6))
    trigger_counts.plot(kind='bar', color='skyblue')
    plt.title("Brand Switching Triggers (Mentioned)")
    plt.xlabel("Switch Triggers")
    plt.ylabel("Number of Mentions")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot
    plt.savefig(output_file)
    plt.close()

    return output_file
