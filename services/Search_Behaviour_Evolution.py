import pandas as pd
import matplotlib.pyplot as plt
import io
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering
import matplotlib.pyplot as plt

CSV_FILE_PATH = "KPI_Data/Search_Behavior.csv"

def generate_search_behavior_evolution_chart():
    # Read CSV data
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Sort by Trend Change descending for better visualization
    df_sorted = df.sort_values(by='Trend Change (%)', ascending=False)

    # Plot setup
    plt.figure(figsize=(15, 10))
    
    indices = range(len(df_sorted))
    
    bar_width = 0.4
    
    # Bars for Today and 1-2 Years Ago
    bars_today = plt.bar(indices, df_sorted['Search Trend (Today)'], bar_width, label='Search Trend (Today)', color='green')
    bars_past = plt.bar([i + bar_width for i in indices], df_sorted['Search Trend (1-2 Years Ago)'], bar_width, label='Search Trend (1-2 Years Ago)', color='orange')
    
    # Highlight bars with positive and negative trend change
    for i, (today_val, past_val, change) in enumerate(zip(df_sorted['Search Trend (Today)'], df_sorted['Search Trend (1-2 Years Ago)'], df_sorted['Trend Change (%)'])):
        color_today = 'green' if change > 0 else 'red'
        bars_today[i].set_color(color_today)
    
    # Labels and ticks
    plt.xlabel('Search Queries / Keywords')
    plt.ylabel('Search Trend Value')
    plt.title('Search Behavior Evolution: Today vs 1-2 Years Ago')
    plt.xticks([i + bar_width / 2 for i in indices], df_sorted['Search Query/Keyword'], rotation=90)
    plt.legend()
    plt.tight_layout()
    
    # Save plot to in-memory bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()
