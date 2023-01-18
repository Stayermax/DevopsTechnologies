from connectors.postgres_connector import PostgresConnector
# from tweets_streaming_service.src.twitter_client import TwitterClient
from tweets_streaming_service.src.twitter_client_v2 import TwitterClient
import os
import yaml
import logging
import pandas as pd
logging.basicConfig(encoding='utf-8', level=logging.INFO)



if __name__ == '__main__':

    # Use Twitter API
    twitter_client = TwitterClient('config/twitter_api_keys.yml')
    # twitter_client.search_tweets(query='israel')
    twitter_client.pagination_search(query='Israel')

    # twitter_client.get_user(username='StayermaxProj')
    # twitter_client.get_user_tweets()
