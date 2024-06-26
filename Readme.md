1. Run Airflow using 'docker-compose up'
2. Create Plugins:
    - Mongo loader
    - Finnhub loader
    - Sentiment Analysis
    - Postgres loader
3. Create python code to extract from Finnhub and load to MongoDB
4. Create python code taht Get data from MongoDB and dop sent Sentiment Analysis then load the result to postgres
5. Run code 'docker exec -it airflow_webserver bash'
6. Run code 'python /opt/airflow/plugins/finnhub_mongodb_loader.py'
7. Run code 'python /opt/airflow/plugins/sentiment_analysis_loader.py'
8. Postgres data load validation 'psql -h postgres -U airflow -d data_warehouse'

