Spotify Data Engineering Pipeline (Medallion Architecture)
This project demonstrates a robust, local End-to-End Data Engineering Pipeline using the Medallion Architecture. It simulates a production-grade workflow by moving data through Bronze, Silver, and Gold layers, focusing on data quality, professional logging, and error handling.

🚀 Project Overview
The goal of this project is to take raw Spotify track data and transform it into actionable business insights. This setup serves as a local prototype for a future migration to Azure Data Factory and Azure Databricks.

Key Features:
Medallion Architecture: Logical separation of data into Raw (Bronze), Cleaned (Silver), and Aggregated (Gold) layers.

Professional Logging: Implemented centralized logging with UTF-8 encoding to track pipeline health and audit trails.

Error Handling: Robust try-except blocks to ensure the pipeline handles missing files or data inconsistencies gracefully.

Production Standards: Clean project structure, virtual environment management, and Git version control.

🏗️ Architecture & Workflow
Bronze (Ingestion): Stores the raw, untouched .csv data as the "Source of Truth."

Silver (Transformation): * Standardizes artist and track naming conventions.

Performs data type enforcement and feature engineering (e.g., is_popular flag).

Gold (Analytics): * Aggregates data by artist to calculate KPIs like Average Popularity and Total Track Count.

Produces business-ready CSVs for BI tools like Power BI or Tableau.

📂 Project Structure

      spotify-azure-de-project/
      ├── data_lake/
      │   ├── bronze/          # Raw data files
      │   ├── silver/          # Cleaned/Standardized data
      │   └── gold/            # Business-ready summaries
      ├── transform_data.py    # Bronze to Silver logic
      ├── generate_gold_summary.py # Silver to Gold logic
      ├── pipeline.log         # Automated audit logs
      ├── .gitignore           # Prevents environment/data bloat in Git
      └── README.md            # Project documentation
🛠️ How to Run
Clone the repository:

  git clone https://github.com/AdrianHWO/spotify-azure-de-project.git
  cd spotify-azure-de-project

Set up the environment:

  python -m venv venv
  .\venv\Scripts\activate
  pip install pandas

Execute the Pipeline:

  python transform_data.py
  python generate_gold_summary.py

Check the Logs:
Open pipeline.log to view the execution history and timestamps.

📈 Future Roadmap
[ ] Migrate storage to Azure Blob Storage.

[ ] Automate ingestion using Azure Data Factory.

[ ] Implement advanced transformations using PySpark in Azure Databricks.

[ ] Connect the Gold layer to a Power BI dashboard.
