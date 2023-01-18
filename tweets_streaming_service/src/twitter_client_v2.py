import logging

import tweepy
import yaml
import json

def json_pretty_print(dictionary):
    print(json.dumps(
        dictionary,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    ))
class TwitterClient():


    def __init__(self, keys_yml_path):
        with open(keys_yml_path, 'r') as file:
            account_dict = yaml.safe_load(file)['account_details']
            bearer_token = account_dict['bearer_token']
            api_key = account_dict['api_key']
            api_key_secret = account_dict['api_key_secret']
            access_token = account_dict['access_token']
            access_token_secret = account_dict['access_token_secret']
            app_id = account_dict['app_id']
            pin = account_dict['pin']

        self.auth = tweepy.OAuth1UserHandler(
            api_key, api_key_secret, access_token, access_token_secret
        )

        self.client = tweepy.Client(bearer_token=bearer_token, return_type=dict)

    def search_tweets(self, query: str):
        all_fields = [
            "attachments",
            "author_id",
            "context_annotations",
            "conversation_id",
            "created_at",
            "entities",
            "geo",
            "id",
            "in_reply_to_user_id",
            "lang",
            "possibly_sensitive",
            "public_metrics",
            "referenced_tweets",
            "reply_settings",
            "source",
            "text",
            "withheld"
        ]
        minimum_fields = [
            'id',
            'text'
        ]
        all_tweets = []
        next_token = None

        while(len(all_tweets)<20):
            response = self.client.search_recent_tweets(query=query,
                                                        tweet_fields=all_fields,
                                                        next_token=next_token,
                                                        max_results=10)
            result_count = response['meta']['result_count']
            if result_count > 0:
                all_tweets += response['data']
                logging.info(f" Tweets collected: {len(all_tweets)}")
                if 'next_token' in response['meta'].keys():
                    next_token = response['meta']['next_token']
                else:
                    logging.info(f"Next token not found")
                    break
        # for tweet in all_tweets:
        #     print(tweet)
        json_pretty_print(all_tweets)
        logging.info(f"overall tweets collected: {len(all_tweets)}")


    def get_user(self, username: str):
        a = self.client.get_user(username=username)
        json_pretty_print(a)

    def get_user_tweets(self, id: str = None):
        tweets = self.client.get_users_tweets(id = "1496886348338405382")
        json_pretty_print(tweets)