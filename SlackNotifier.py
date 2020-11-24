import json
import datetime
import os

import requests

root = os.path.dirname(__file__)
config = json.load(open(f'{root}/config.json'))


def notify(message, download_url, receiver):
    current_date = datetime.datetime.today().strftime('%d-%b-%Y')
    # RECEIVER

    author = config["author"]
    body = {
        'text': f'{message} \n'
                f'date : {current_date}: <{download_url}|Download> \n'
                f'Author : {author}\n',
        'username': 'Android Release Bot',
        'icon_emoji': ':rocket:'
    }
    bod = json.dumps(body)
    print(requests.post(receiver, bod).text)
