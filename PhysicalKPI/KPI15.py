from fastapi import APIRouter, FastAPI
import pandas as pd

app = FastAPI()
router = APIRouter()

@router.get("/execute_kpi_gifting/")
async def execute_kpi_gifting():
    try:
        # Fixed CSV path — update to your actual file location
        csv_path = "Indian-Namkeen-Market-SWOT-Analysis-main/PhysicalKPICSV/KPI15.csv"

        # Read CSV file
        df = pd.read_csv(csv_path)

        # Extract only the first 4 columns
        df_cleaned = df.iloc[:, :4]

        # Rename columns
        df_cleaned.columns = [
            'description',
            'analysis/findings',
            'specific example/observations',
            'source'
        ]

        # Drop fully empty rows
        df_cleaned.dropna(how='all', inplace=True)

        # Build structured JSON output
        summary = []
        for _, row in df_cleaned.iterrows():
            summary.append({
                "📝 Description": row['description'],
                "🔍 Findings": row['analysis/findings'],
                "💬 Observation": row['specific example/observations'],
                "📡 Source": row['source']
            })

        return {
            "message": "✅ KPI 15 file processed successfully.",
            "total_records": len(summary),
            "summary": summary
        }

    except Exception as e:
        return {"error": f"❌ Error processing file: {str(e)}"}
