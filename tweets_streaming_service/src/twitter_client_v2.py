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

        auth = tweepy.OAuth1UserHandler(
            api_key, api_key_secret, access_token, access_token_secret
        )

        client = tweepy.Client(bearer_token=bearer_token, return_type=dict)
        a = client.search_recent_tweets(query='israel', tweet_fields=['attachments'])
        json_pretty_print(a)

        # a = client.get_user(username="GretaThunberg")
        # json_pretty_print(a)

        # self.api.GetUser(screen_name='StayermaxProj')