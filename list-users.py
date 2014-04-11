import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('key')
args = parser.parse_args()

url = ("https://api.hipchat.com/v1/users/list?"
       "format=json&auth_token={}".format(args.key))

response = requests.get(url)
data = response.json()
for user in data['users']:
    print "{},{}".format(user['email'], user['user_id'])
