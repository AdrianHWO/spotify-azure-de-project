import pandas as pd
import requests
import io


def extract_mock_data():
    print("Connecting to Sample Data Source...")
    url = "https://raw.githubusercontent.com/datasets/top-spotify-songs/master/data/top50.csv"

    try:
        response = requests.get(url)
        # Load the data - using ISO-8859-1 for music characters
        df = pd.read_csv(io.StringIO(response.text), encoding="ISO-8859-1")

        # --- THE ULTIMATE FIX: RENAME BY POSITION ---
        # Column 0 is usually an ID, Column 1 is Track, Column 2 is Artist
        new_names = {df.columns[1]: "track_name", df.columns[2]: "artist"}

        # If there's a column for popularity (usually column 4 or 5), we grab that too
        if len(df.columns) > 4:
            new_names[df.columns[4]] = "popularity"

        df = df.rename(columns=new_names)

        # Keep only our renamed columns
        cols_to_keep = [
            col for col in ["track_name", "artist", "popularity"] if col in df.columns
        ]
        df = df[cols_to_keep]

        print("--- Success! Local Data Captured ---")
        print(df.head())

        # Save this to your folder so we can use it in Azure
        df.to_csv("spotify_raw_data.csv", index=False)
        print("\nFile 'spotify_raw_data.csv' created successfully.")

    except Exception as e:
        print(f"Still hitting an error: {e}")
        print(
            "\nLet's try a backup: Just creating a tiny dummy file so we can move to Azure."
        )
        dummy_data = {
            "track_name": ["Song A", "Song B"],
            "artist": ["Artist X", "Artist Y"],
            "popularity": [80, 90],
        }
        pd.DataFrame(dummy_data).to_csv("spotify_raw_data.csv", index=False)
        print("Emergency 'spotify_raw_data.csv' created instead.")


if __name__ == "__main__":
    extract_mock_data()
