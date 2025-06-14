from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()
router = APIRouter()

# Replace with your actual file path
FILE_PATH = "PhysicalKPICSV/KPI7.csv"

@router.get("/comparison-points")
async def get_comparison_points():
    try:
        # Load the CSV file
        df = pd.read_csv(FILE_PATH)

        # Ensure minimum expected columns
        if df.shape[1] < 3:
            return {"error": "❌ Expected at least 3 columns: Sample Text, Brand, Comparison Type."}

        # Automatically identify the first 3 columns
        sample_col = df.columns[0]
        brand_col = df.columns[1]
        type_col = df.columns[2]

        # Clean and convert to string
        df[sample_col] = df[sample_col].astype(str)
        df[brand_col] = df[brand_col].astype(str)
        df[type_col] = df[type_col].astype(str)

        # Build the output list
        result_list = []
        for _, row in df.iterrows():
            result_list.append({
                "Sample Text": row[sample_col],
                "Comparison Brand": row[brand_col],
                "Comparison Type": row[type_col]
            })

        return {
            "List of frequently mentioned comparison points": result_list
        }

    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"error": f"❌ File not found at: {FILE_PATH}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"❌ Internal Server Error: {str(e)}"})
