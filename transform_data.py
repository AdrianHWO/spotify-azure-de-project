import pandas as pd
import os
import logging

# 1. SETUP LOGGING
# This creates a file called 'pipeline.log' and also prints to your terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),  # Saves to a file
        logging.StreamHandler(),  # Still prints to terminal
    ],
)

logger = logging.getLogger(__name__)


def transform_bronze_to_silver():
    logger.info("🚀 Pipeline Started: Bronze to Silver transformation.")

    try:
        # Load the raw data
        input_path = "data_lake/bronze/spotify_raw_data.csv"
        if not os.path.exists(input_path):
            logger.error(f"❌ Missing File: {input_path} not found!")
            return

        df = pd.read_csv(input_path)
        logger.info(f"📥 Successfully loaded {len(df)} rows from Bronze.")

        # DATA CLEANING
        df["artist"] = df["artist"].str.upper()
        df["track_name"] = df["track_name"].str.title()
        df["is_popular"] = df["popularity"] > 85

        # Save to Silver folder
        output_path = "data_lake/silver/spotify_cleaned_data.csv"
        df.to_csv(output_path, index=False)

        logger.info(f"✅ Success: Cleaned data saved to {output_path}")

    except Exception as e:
        logger.error(f"💥 Critical Error during transformation: {str(e)}")


if __name__ == "__main__":
    transform_bronze_to_silver()
