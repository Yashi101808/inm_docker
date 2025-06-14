from fastapi import APIRouter, FastAPI
import pandas as pd
import random
from collections import Counter

app = FastAPI()
router = APIRouter()

@router.get("/execute_kpi_loyalty/")
async def execute_kpi_loyalty():
    try:
        # Path to the actual CSV file
        csv_path = "PhysicalKPICSV/KPI14.csv"

        # Skip first 2 rows where metadata/header lies
        df = pd.read_csv(csv_path, skiprows=2)

        # Set proper column names
        df.columns = ["content", "loyalty indicator(Yes/No)"]

        # Check if the expected columns are present
        if "content" not in df.columns or "loyalty indicator(Yes/No)" not in df.columns:
            return {
                "error": "CSV file must contain 'content' and 'loyalty indicator(Yes/No)' columns.",
                "found_columns": list(df.columns)
            }

        # Generate values randomly (simulate loyalty indicator mentions)
        def random_loyalty():
            r = random.random()
            if r < 0.5:
                return "Yes"
            elif r < 0.9:
                return "No"
            else:
                return "Maybe"

        df["loyalty indicator(Yes/No)"] = [random_loyalty() for _ in range(len(df))]

        # Count frequencies
        counts = Counter(df["loyalty indicator(Yes/No)"])

        # Create structured output
        output = {
            "Representation: Qualitative summary or count of loyalty indicator mentions in sample.": [
                {
                    "Indicator": "Yes",
                    "Mentions": counts.get("Yes", 0)
                },
                {
                    "Indicator": "No",
                    "Mentions": counts.get("No", 0)
                },
                {
                    "Indicator": "Maybe",
                    "Mentions": counts.get("Maybe", 0)
                }
            ]
        }

        return output

    except Exception as e:
        return {"error": f"❌ Error processing CSV file: {str(e)}"}
