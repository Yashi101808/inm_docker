from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

# 📁 Update this path as needed for your environment
FILE_PATH = "Indian-Namkeen-Market-SWOT-Analysis-main/PhysicalKPICSV/KPI2.csv"

@router.get("/generate-graph")
async def generate_graph():
    try:
        # Load CSV
        df = pd.read_csv(FILE_PATH)

        # Rename columns for clarity
        df.rename(columns={
            df.columns[0]: 'Month',
            df.columns[1]: 'buy haldiram online',
            df.columns[2]: 'haldiram price',
            df.columns[3]: 'haldiram near me'
        }, inplace=True)

        # Clean and parse datetime
        df = df[df['Month'].notna() & (df['Month'].str.lower() != 'month')]
        df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
        df.dropna(subset=['Month'], inplace=True)
        df.set_index('Month', inplace=True)

        # Convert all other columns to numeric
        df = df.apply(pd.to_numeric, errors='coerce')

        # Plotting
        plt.figure(figsize=(14, 7))
        for column in df.columns:
            plt.plot(df.index, df[column], label=column)

        plt.title("Trends of Purchase-Intent Keywords Over Time", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Search Interest / Volume", fontsize=12)
        plt.legend(title="Keywords", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()

        # Stream as image
        img_stream = BytesIO()
        plt.savefig(img_stream, format='png')
        plt.close()  # Close figure to free memory
        img_stream.seek(0)

        return StreamingResponse(img_stream, media_type="image/png")

    except FileNotFoundError:
        return {"error": f"❌ File not found: {FILE_PATH}"}
    except Exception as e:
        return {"error": f"❌ Internal error: {str(e)}"}
