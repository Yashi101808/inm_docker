import pandas as pd
import matplotlib.pyplot as plt
import io

def generate_issue_type_chart(csv_path):
    # Read CSV
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
    # Use 'Reaction Type' if that's what you want
    if 'Reaction Type' not in df.columns:
        raise ValueError(f"'Reaction Type' column not found in {csv_path}. Columns are: {df.columns.tolist()}")
    issue_counts = df['Reaction Type'].value_counts()

    # Plot bar chart
    plt.figure(figsize=(8,5))
    issue_counts.plot(kind='bar', color='skyblue')
    plt.title('Issue Type Counts')
    plt.ylabel('Count')
    plt.xlabel('Issue Type')
    plt.tight_layout()

    # Save plot to bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.read()
