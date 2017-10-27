# coding: utf8
from BaseClient import BaseClient
import requests
import sys

class GetUserID(BaseClient):
    def __init__(self, username):
        self.username = username
    method = "users.get"
    http_method = "?user_ids="

    def generate_url(self):
        return '{0}{1}{2}'.format(BaseClient.generate_url(self),self.http_method,self.username)

    def get_data(self):
        r = requests.get(self.generate_url()).json()
        try:
            if r["response"][0]["deactivated"]:
                print("this page was banned or not exist")
                sys.exit()
        except Exception:
            return r["response"][0]["uid"]
