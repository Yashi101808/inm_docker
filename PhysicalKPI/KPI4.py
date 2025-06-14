from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

# ✅ Update your file path
FILE_PATH = "Indian-Namkeen-Market-SWOT-Analysis-main/PhysicalKPICSV/KPI4.csv"

@router.get("/kpi4-psychographic-themes")
async def generate_kpi4_graph():
    try:
        df = pd.read_csv(FILE_PATH, skiprows=2)
        df.columns = ["Psychographic Theme", "Frequency"]
        df.dropna(inplace=True)
        df["Frequency"] = df["Frequency"].astype(int)
        df_sorted = df.sort_values(by="Frequency", ascending=False)

        plt.figure(figsize=(10, 6))
        plt.barh(df_sorted["Psychographic Theme"], df_sorted["Frequency"], color='skyblue')
        plt.xlabel("Frequency")
        plt.title("Psychographic Themes in Haldiram Reviews & Social Posts")
        plt.gca().invert_yaxis()
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()

        img_bytes = BytesIO()
        plt.savefig(img_bytes, format='png')
        plt.close()
        img_bytes.seek(0)

        return StreamingResponse(img_bytes, media_type="image/png")

    except FileNotFoundError:
        return {"error": f"❌ File not found at: {FILE_PATH}"}
    except Exception as e:
        return {"error": f"❌ Internal error: {str(e)}"}
