from fastapi import APIRouter, FastAPI
import pandas as pd
from textblob import TextBlob

app = FastAPI()
router = APIRouter()

def get_sentiment(text: str) -> str:
    if not isinstance(text, str) or text.strip() == "":
        return "Neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

@router.get("/execute_kpi12/")
async def analyze_kpi12_sentiment():
    try:
        csv_path = "PhysicalKPICSV/KPI12.csv"
        df = pd.read_csv(csv_path)

        # Rename first two columns just in case
        df.columns = ['content', 'feedback'] + list(df.columns[2:])

        if 'content' not in df.columns:
            return {"error": "CSV must contain a 'content' column."}

        # Apply sentiment analysis
        df['Computed Sentiment'] = df['content'].apply(get_sentiment)

        # Filter to only Positive and Negative
        filtered_df = df[df['Computed Sentiment'].isin(['Positive', 'Negative'])]

        total = len(filtered_df)
        positive_count = len(filtered_df[filtered_df['Computed Sentiment'] == 'Positive'])
        negative_count = len(filtered_df[filtered_df['Computed Sentiment'] == 'Negative'])

        if total == 0:
            return {"message": "No Positive or Negative sentiments found in content."}

        positive_percent = round((positive_count / total) * 100, 2)
        negative_percent = round((negative_count / total) * 100, 2)

        return {
            "Representation: Summary of positive and negative sentiment percentages.": {
                "Positive": f"{positive_percent}%",
                "Negative": f"{negative_percent}%"
            }
        }

    except Exception as e:
        return {"error": f"❌ Error processing KPI 12 file: {str(e)}"}
