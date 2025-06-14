import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def generate_payment_issues_chart(csv_path='KPI_data/Digital_Payment_feedback.csv'):
    # Load data
    df = pd.read_csv(csv_path)

    # Group by Payment Method and Transaction Outcome and count
    summary = df.groupby(['Payment Method', 'Transaction Outcome']).size().unstack(fill_value=0)

    # Plot stacked bar chart
    plt.figure(figsize=(10,6))
    colors = ['#AEC6CF', '#FFB347']  # pastel blue for Success, pastel orange for Failed

    summary.plot(kind='bar', stacked=True, color=colors)

    plt.title('Payment Method - Success vs Failure Counts')
    plt.xlabel('Payment Method')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Transaction Outcome')
    plt.tight_layout()

    # Save plot to bytes buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf.getvalue()
