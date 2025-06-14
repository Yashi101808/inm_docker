from fastapi import APIRouter, FastAPI
import pandas as pd

app = FastAPI()
router = APIRouter()

@router.get("/execute_kpi13/")
async def execute_kpi13():
    try:
        # Fixed path to your KPI13 CSV file on server
        csv_path = "Indian-Namkeen-Market-SWOT-Analysis-main/PhysicalKPICSV/KPI13.csv"  # Change this path to your actual file location
        
        # Read CSV
        df = pd.read_csv(csv_path)

        # Assign column headers
        df.columns = [
            "sample content",
            "discovery channel category",
            "reason",
            "no.of mentions",
            "discovery types",
            "remarks"
        ]

        # Drop fully empty rows
        df.dropna(how='all', inplace=True)

        # Convert 'no.of mentions' to numeric
        df["no.of mentions"] = pd.to_numeric(df["no.of mentions"], errors="coerce").fillna(0).astype(int)

        # Group and summarize
        summary = df.groupby("discovery channel category").agg({
            "no.of mentions": "sum",
            "reason": lambda x: ', '.join(x.dropna().unique()),
            "discovery types": lambda x: ', '.join(x.dropna().unique()),
            "remarks": lambda x: ', '.join(x.dropna().unique())
        }).reset_index()

        # Final output formatting
        output = []
        for _, row in summary.iterrows():
            output.append({
                "discovery_channel": row["discovery channel category"],
                "total_mentions": int(row["no.of mentions"]),
                "key_reasons": row["reason"],
                "discovery_types": row["discovery types"],
                "remarks": row["remarks"]
            })

        return {
            "message": "✅ KPI 13 discovery summary generated successfully.",
            "result": output
        }

    except Exception as e:
        return {"error": f"❌ Error processing KPI 13: {str(e)}"}
