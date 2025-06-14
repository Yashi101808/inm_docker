# services/Subscription_Intrest_Level.py

import pandas as pd
import matplotlib.pyplot as plt
import io

CSV_PATH = "KPI_Data/Subscription_Intrest.csv"

def generate_subscription_pie_chart():
    df = pd.read_csv(CSV_PATH)
    data = df['Subscription Interest Level'].value_counts()

    fig, ax = plt.subplots()
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf.read()
