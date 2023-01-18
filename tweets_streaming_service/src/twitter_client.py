import pandas as pd
from pytwitter import Api
from pytwitter import StreamApi
import yaml

class StreamApiPrint(StreamApi):
    def on_tweet(self, tweet):
        print(tweet)
        return tweet

class TwitterClient():
    def __init__(self, keys_yml_path):
        with open(keys_yml_path, 'r') as file:
            account_dict = yaml.safe_load(file)['account_details']
            bearer_token = account_dict['bearer_token']
            api_key = account_dict['api_key']
            api_key_secret = account_dict['api_key_secret']
            app_id = account_dict['app_id']
            pin = account_dict['pin']
        self.api = Api(bearer_token=bearer_token,
                       consumer_key = api_key,
                       consumer_secret = api_key_secret,
                       oauth_flow=True)
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

        # found_tweeets = self.api.search_tweets(query="Israel", tweet_fields=all_fields, query_type='recent')
        # print(found_tweeets)
        # if found_tweeets is not None:
        #     print(found_tweeets.includes)
        #     for tweet in found_tweeets.data:
        #         print(tweet.id)
        #         print(tweet.text)
        #         print(tweet.author_id)
        #         print(tweet.geo)
        #         print(tweet.lang)
        #         print(tweet.public_metrics)
        #         print(type(tweet.attachments))
        #         print(f'====')

        a = self.api.get_tweets("1615787373304123392", tweet_fields=all_fields).data[0]
