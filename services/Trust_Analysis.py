import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering
import matplotlib.pyplot as plt

def generate_trust_analysis_plot(csv_file_path: str = "KPI_Data/Trust_Analysis.csv") -> bytes:
    # Load CSV data
    df = pd.read_csv(csv_file_path)

    # Extract and count trust-related keywords (lowercase)
    all_keywords = []
    for keywords in df['Trust-Related Keywords'].dropna():
        kw_list = [kw.strip().lower() for kw in keywords.split(',')]
        all_keywords.extend(kw_list)

    keyword_counts = Counter(all_keywords)
    keyword_df = pd.DataFrame(keyword_counts.items(), columns=['Keyword', 'Frequency'])
    keyword_df = keyword_df.sort_values(by='Frequency', ascending=False)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.bar(keyword_df['Keyword'], keyword_df['Frequency'], color='teal')
    plt.title('Frequency of Trust-Related Keywords in Positive Reviews')
    plt.xlabel('Trust-Related Keywords')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save plot to a BytesIO object as PNG
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    plt.close()
    img_buffer.seek(0)

    return img_buffer.read()
