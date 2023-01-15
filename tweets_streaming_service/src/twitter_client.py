import pandas as pd
from pytwitter import Api
import yaml

class TwitterClient():
    def __init__(self, keys_yml_path):
        with open(keys_yml_path, 'r') as file:
            bearer_token = yaml.safe_load(file)['account_details']['bearer_token']
        self.api = Api(bearer_token=bearer_token)
        print(self.api.get_me())

