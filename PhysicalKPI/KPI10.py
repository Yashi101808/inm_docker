from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os
import traceback

app = FastAPI()
router = APIRouter()

@router.get("/execute_kpi10/")
async def execute_kpi10():
    file_path = "PhysicalKPICSV/KPI10.csv"
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return JSONResponse(status_code=404, content={"error": "CSV file not found at path."})

        # Try reading CSV, specify encoding (if needed), and skip first 2 rows
        df = pd.read_csv(file_path, skiprows=2, encoding='utf-8')

        # Debug info: check shape and head
        print(f"Dataframe shape: {df.shape}")
        print(df.head())

        # Check number of columns before renaming
        if df.shape[1] < 6:
            return JSONResponse(status_code=400, content={"error": "CSV does not have expected 6 columns after skipping rows."})

        # Rename columns
        df.columns = [
            'KPI Sub-Category',
            'Description',
            'Analysis/Findings',
            'Specific Example/Observations',
            'Source',
            'Extra'
        ]

        # Drop 'Extra' column safely if exists
        if 'Extra' in df.columns:
            df.drop(columns=['Extra'], inplace=True)

        # Convert to list of dicts for JSON response
        result = df.to_dict(orient="records")

        return {
            "Representation: Qualitative summary of price/promotion sensitivity observed.": result
        }

    except Exception as e:
        tb = traceback.format_exc()
        print(f"Exception:\n{tb}")
        return JSONResponse(status_code=500, content={"error": "Internal Server Error", "details": str(e)})
