# Agricultural Data Pipeline

## Project Overview
This project aims to build a comprehensive data pipeline that ingests agricultural data from various sources, processes it, and provides insights through visualizations. The pipeline includes data ingestion, ETL processes, data storage, and visualization components.

## Key Components

### Data Ingestion
- **fetch_weather_data.py**: Fetches weather data from an external API and processes it for further use.
- **fetch_crop_yield_data.py**: Retrieves crop yield data from an external API and prepares it for ingestion.
- **upload_to_s3.py**: Uploads the fetched data to an AWS S3 bucket for storage.

### ETL Processes
- **airflow_dags/weather_etl_dag.py**: Defines an Apache Airflow DAG for orchestrating the ETL process related to weather data.
- **airflow_dags/crop_yield_etl_dag.py**: Defines an Apache Airflow DAG for orchestrating the ETL process related to crop yield data.
- **data_cleaning.py**: Contains functions to clean and preprocess the ingested data using Python libraries like Pandas.
- **data_transformation.py**: Transforms the cleaned data into a suitable format for analysis.
- **load_to_postgres.py**: Loads the transformed data into a PostgreSQL database.

### API Integration
- **api/app.py**: Contains the main application code for the API, including route definitions and integration with the data processing components.
- **api/requirements.txt**: Lists the dependencies required for the API, such as Flask or FastAPI.

### Data Analysis and Visualization
- **analysis/sql_queries.sql**: Contains SQL queries used for data analysis, such as aggregations and joins.
- **analysis/data_analysis.ipynb**: A Jupyter notebook used for exploratory data analysis and visualization of the agricultural data.
- **visualization/power_bi_dashboard.pbix**: A Power BI dashboard that visualizes insights from the agricultural data.
- **visualization/tableau_dashboard.twb**: A Tableau dashboard that visualizes insights from the agricultural data.

### Performance Tuning and Optimization
- **scripts/optimize_queries.sql**: Contains SQL scripts for optimizing database queries.
- **scripts/create_indexes.sql**: Contains SQL scripts for creating indexes in the PostgreSQL database to improve query performance.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install the required Python packages listed in `requirements.txt`.
3. Set up your AWS credentials for S3 access.
4. Configure the PostgreSQL database connection in the relevant scripts.
5. Run the data ingestion scripts to fetch and store data.
6. Use Apache Airflow to schedule and manage the ETL processes.
7. Access the API to retrieve processed data for analysis and visualization.

## Usage Guidelines
- Ensure that all external API keys and credentials are securely managed.
- Follow best practices for data handling and storage.
- Regularly update the dependencies and monitor the performance of the pipeline.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.