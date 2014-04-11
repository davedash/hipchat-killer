import argparse
import uuid
import requests


parser = argparse.ArgumentParser()
parser.add_argument('key')
parser.add_argument('file')
args = parser.parse_args()



url = ("https://api.hipchat.com/v1/users/update?"
       "format=json&auth_token={}".format(args.key))

response = requests.get(url)
data = response.json()

with open(args.file) as f:
    for line in f.readlines():
        email, user_id = line.strip().split(',')
        # We're going to reset everyone's nick too
        nick, _ = email.split('@')
        print "Resetting {}".format(nick)
        password = uuid.uuid4()
        data = {'user_id': user_id, 'mention_name': nick, 'password': password}
        response = requests.post(url, data)
