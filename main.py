from connectors.postgres_connector import PostgresConnector
# from tweets_streaming_service.src.twitter_client import TwitterClient
from tweets_streaming_service.src.twitter_client_v2 import TwitterClient
import os
import yaml
import logging
import pandas as pd
logging.basicConfig(encoding='utf-8', level=logging.INFO)

if __name__ == '__main__':
    # Import DataFrame to server
    # with open('configs/db_configs.yml', 'r') as file:
    #     db_configuration = yaml.safe_load(file)['twitter_db']
    # pg_connector = PostgresConnector(db_configuration)
    # for filename in os.listdir('data'):
    #     db_name = filename.strip('.csv').lower()
    #     df = pd.read_csv('data/Tweet.csv')
    #     pg_connector.insert_df_to_table(df, db_name)

    # Use Twitter API
    twitter_client = TwitterClient('tweets_streaming_service/config/twitter_api_keys.yml')
