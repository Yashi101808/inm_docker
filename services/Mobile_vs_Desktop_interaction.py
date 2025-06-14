import pandas as pd
import matplotlib.pyplot as plt
import io

CSV_FILE_PATH = "KPI_Data/Mobile_vs_Desktop_Interaction.csv"

def generate_mobile_desktop_bar_chart():
    # Read the CSV
    df = pd.read_csv(CSV_FILE_PATH)

    # We extract "Page Load Speed" row for numeric scores
    # (You can extend this by adding numeric columns for other KPIs if needed)
    pload = df[df['KPI'] == "Page Load Speed (KPI 59)"].iloc[0]

    # Extract numeric scores from text manually (since they are embedded in text)
    # "Mobile load speed score: 75/100 (average)"
    mobile_score_text = pload['Mobile Interaction']
    desktop_score_text = pload['Desktop Interaction']

    mobile_score = int(mobile_score_text.split(':')[1].strip().split('/')[0])
    desktop_score = int(desktop_score_text.split(':')[1].strip().split('/')[0])

    # Plot
    labels = ['Page Load Speed']
    mobile_scores = [mobile_score]
    desktop_scores = [desktop_score]

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(x, mobile_scores, width, label='Mobile')
    ax.bar([i + width for i in x], desktop_scores, width, label='Desktop')

    ax.set_ylabel('Score (out of 100)')
    ax.set_title('Mobile vs Desktop Page Load Speed')
    ax.set_xticks([i + width/2 for i in x])
    ax.set_xticklabels(labels)
    ax.legend()

    plt.tight_layout()

    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf
