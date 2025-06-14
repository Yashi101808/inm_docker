import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import io
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering
import matplotlib.pyplot as plt

class PostPurchaseDissonance:
    def __init__(self, csv_path='KPI_Data/Post_Purchase_Dessonance.csv'):
        self.csv_path = csv_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.csv_path)
        # Filter only negative comments with expectation mismatch as Yes
        self.df = self.df[(self.df['Sentiment'] == 'Negative') & (self.df['Expectation Mismatch'] == 'Yes')]

    def generate_dissonance_chart(self):
        if self.df is None:
            self.load_data()

        reason_counts = Counter(self.df['Dissonance Reason'])
        top_reasons = reason_counts.most_common(5)

        reasons = [r[0] for r in top_reasons]
        counts = [r[1] for r in top_reasons]

        plt.figure(figsize=(8,8))
        wedges, texts, autotexts = plt.pie(
            counts, labels=reasons, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors,
            textprops={'fontsize': 12}
        )
        plt.title('Top 5 Post-Purchase Dissonance Reasons\n(by % of Negative Comments)', fontsize=14)
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        return buf.read()
