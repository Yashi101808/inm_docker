import pandas as pd
import matplotlib.pyplot as plt
from fastapi.responses import FileResponse

CSV_FILE = "KPI_Data/platform_role.csv"
CHART_FILE = "platform_funnel_kpi_chart.png"

def get_platform_funnel_kpi_chart():
    df = pd.read_csv(CSV_FILE)
    
    # Group by Platform and Inferred Funnel Stage and count occurrences
    grouped = df.groupby(['Platform', 'Inferred Funnel Stage']).size().unstack(fill_value=0)
    
    platforms = grouped.index.tolist()
    funnel_stages = grouped.columns.tolist()
    
    x = range(len(platforms))
    bar_width = 0.1
    
    plt.figure(figsize=(12, 6))
    
    # For each funnel stage, plot bars side by side
    for i, stage in enumerate(funnel_stages):
        plt.bar([pos + i * bar_width for pos in x], grouped[stage], width=bar_width, label=stage)
    
    # Rotate x-axis labels for better readability
    plt.xticks([pos + bar_width * (len(funnel_stages)/2) for pos in x], platforms, rotation=45, ha='right')
    
    plt.ylabel("Count")
    plt.title("Distribution of Inferred Funnel Stages by Platform")
    plt.legend(title='Funnel Stage')
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=200)
    plt.close()
    
    # Return FileResponse WITHOUT filename to show inline image
    return FileResponse(CHART_FILE, media_type='image/png')
