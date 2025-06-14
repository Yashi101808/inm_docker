from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd

router = APIRouter()

# ✅ Hardcoded file path (update if needed)
FILE_PATH = "Indian-Namkeen-Market-SWOT-Analysis-main/PhysicalKPICSV/KPI9.csv"

@router.get("/kpi9-observed-terms")
async def list_observed_terms():
    try:
        # Load the CSV
        df = pd.read_csv(FILE_PATH)

        # ✅ Rename columns based on your structure
        df.columns = ["term/slang", "meaning/context", "source platform"]

        # Drop empty rows
        df.dropna(how="all", inplace=True)

        # Build the output
        output = []
        for _, row in df.iterrows():
            output.append({
                "Term/Slang": row["term/slang"],
                "Meaning/Context": row["meaning/context"],
                "Source Platform": row["source platform"]
            })

        return {
            "Representation: List of observed terms": output
        }

    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"error": f"❌ File not found at: {FILE_PATH}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"❌ Internal Error: {str(e)}"})
