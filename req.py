import requests 
import threading
import random
import json 
config_file_path = './config.json'
with open(config_file_path, 'r') as file:
    config = json.load(file)


response = requests.get(url = config.get('poll_url'), timeout=10)
for line in response.text.split('\n'):
    if(config.get('item_name') in line) and 'this' in line:
        option_data = json.loads(line.split('Keys(')[1].split('))')[0])
poll_id = option_data['id']
for item in option_data['poll_options']:
    if(config.get('item_name') in item['value']):
        item_id = item['id']
        item_poll_id = item['uuid']
data = {
    "pv": item_poll_id,
    "v": {
        "id": "",
        "name": "",
        "pollVotes": [
            {
                "id": item_id,
                "value": 1
            }
        ],
        "voteType": "add",
        "token": "",
        "isEmbed": False
    },
    "h": False,
    "ht": False,
    "token": None,
    "st": None
}


def vote():
    for i in range(config.get('vote_count')):
        s = requests.Session()
        response1 = s.get(url = config.get('poll_url'), timeout=10)
        headers = {
        'Cookie': 'session='+response1.cookies.get_dict()['session']
        }
        cookies = {'session': response1.cookies.get_dict()['session']}
        response = s.post(url = f'https://api.strawpoll.com/v3/polls/{poll_id}/vote', json=data, cookies=cookies, headers=headers, verify=False, timeout=10)
        print(response.json())






threads = []

# Create and start threads in a loop
for _ in range(config.get('threads_count')):
    thread = threading.Thread(target=vote)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()