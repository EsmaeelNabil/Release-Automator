import json
import datetime
import requests

config = json.load(open('/home/esmaeel/PycharmProjects/pythonProject/config.json'))


def notify(version, download_url, custom_message=""):
    current_date = datetime.datetime.today().strftime('%d-%b-%Y')
    # RECEIVER
    url = config["receiver"]
    body = {
        'text': f'{version} is ready in : {current_date}: <{download_url}|Download> \nAuther : Esmaeel Nabil\n{custom_message}',
        'username': 'Android Muhla Release Bot',
        'icon_emoji': ':rocket:'
    }
    bod = json.dumps(body)
    print(requests.post(url, bod).text)
