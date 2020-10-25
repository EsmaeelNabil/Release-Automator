#!/usr/bin/python
import json
import os
import sys
from googleapiclient.http import MediaFileUpload
import AuthManager
import SlackNotifier

config = json.load(open('/home/esmaeel/PycharmProjects/pythonProject/config.json'))


def get_files(service):
    # Gets a List of files in your google drive
    results = service.files().list(pageSize=100, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], f'https://drive.google.com/file/d/{item["id"]}'))


def upload_file(service, file_path, app_version):
    filename = os.path.basename(file_path)
    print(filename)

    file_metadata = {'name': filename}
    media = MediaFileUpload(file_path, chunksize=1024 * 1024, resumable=True)
    print('Uploading ........')
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()

    download_url = f'https://drive.google.com/file/d/{file.get("id")}'
    print("File Uploaded :", download_url)

    # make it visible to anyone with a link if enabled in config.json .
    if config['change_permission']:
        service.permissions().create(body={"role": "reader", "type": "anyone"}, fileId=file.get('id')).execute()

    # ability for disabling slack notifications from config.json.
    if config["enable_slack_notification"]:
        SlackNotifier.notify(app_version, download_url)
        print("Slack Channel Updated Successfully.")


def main():
    if sys.argv[1] == '-list':
        service = AuthManager.authenticate_if_needed()
        get_files(service)

    elif sys.argv[1] == '-u':
        service = AuthManager.authenticate_if_needed()
        file = sys.argv[2]
        file_version = sys.argv[3]
        upload_file(service, file, file_version)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("python3 uploader.py : \nfor UPLOAD : -u <FILE-PATH> <NAME> \nfor FILES list: -list")
        sys.exit(2)
    else:
        main()
