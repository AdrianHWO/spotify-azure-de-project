import pandas as pd
import os
import logging

# Use the SAME log file so all steps are in one place
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("pipeline.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def generate_gold_layer():
    logger.info("🚀 Pipeline Started: Silver to Gold aggregation.")

    silver_path = "data_lake/silver/spotify_cleaned_data.csv"
    if not os.path.exists(silver_path):
        logger.error("❌ Silver data missing! Run transform_data.py first.")
        return

    try:
        df = pd.read_csv(silver_path)

        # Logic: Group by artist for the summary
        gold_summary = (
            df.groupby("artist")
            .agg(
                total_tracks=("track_name", "count"),
                avg_popularity=("popularity", "mean"),
            )
            .reset_index()
        )

        output_path = "data_lake/gold/artist_performance_summary.csv"
        gold_summary.to_csv(output_path, index=False)

        logger.info(
            f"✅ Success: Gold summary created with {len(gold_summary)} artists."
        )

    except Exception as e:
        logger.error(f"💥 Gold Layer Error: {str(e)}")


if __name__ == "__main__":
    generate_gold_layer()
