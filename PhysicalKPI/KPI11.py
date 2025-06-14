from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd

router = APIRouter()

# ✅ Path to the KPI 11 file
FILE_PATH = "Indian-Namkeen-Market-SWOT-Analysis-main/PhysicalKPICSV/KPI11.csv"

@router.get("/kpi11-sentiment-summary")
async def sentiment_summary():
    try:
        # Load the file
        df = pd.read_csv(FILE_PATH)

        # Column containing sentiment
        sentiment_column = "11. International Consumer Sentiment Variance"

        # Ensure column exists
        if sentiment_column not in df.columns:
            return JSONResponse(status_code=400, content={"error": f"❌ Column '{sentiment_column}' not found in CSV."})

        # Clean and normalize
        df[sentiment_column] = df[sentiment_column].astype(str).str.strip().str.capitalize()

        # Calculate distribution
        sentiment_distribution = df[sentiment_column].value_counts(normalize=True) * 100

        # Format output
        result = {sentiment: f"{pct:.2f}%" for sentiment, pct in sentiment_distribution.items()}

        return {
            "Representation: International Consumer Sentiment Distribution (%)": result
        }

    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"error": f"❌ File not found at: {FILE_PATH}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"❌ Internal Server Error: {str(e)}"})
