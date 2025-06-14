from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()
router = APIRouter()

# ✅ Define file path
FILE_PATH = "PhysicalKPICSV/KPI1.csv"

@router.get("/rising-search-queries")
async def get_rising_queries():
    try:
        # ✅ Step 1: Load CSV and skip first 2 rows
        df = pd.read_csv(FILE_PATH, skiprows=2)

        # ✅ Step 2: Standardize the 'Percentage.1' column
        if 'Percentage.1' not in df.columns or 'Top' not in df.columns:
            return JSONResponse(status_code=400, content={"error": "Required columns not found in the CSV."})

        df['Percentage.1'] = df['Percentage.1'].astype(str).str.strip().str.lower()

        # ✅ Step 3: Filter for breakout search terms
        breakout_df = df[df['Percentage.1'] == 'breakout']

        # ✅ Step 4: Get unique rising search queries
        top_queries = breakout_df['Top'].dropna().drop_duplicates().tolist()

        return {
            "🔥 Top Rising Related Search Queries": top_queries
        }

    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"error": f"❌ File not found at: {FILE_PATH}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"❌ Internal Server Error: {str(e)}"})
