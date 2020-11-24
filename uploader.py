#!/usr/bin/python
import json
import os
import sys
from googleapiclient.http import MediaFileUpload
import AuthManager
import SlackNotifier
from printer import printy, print_ok

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


def upload_file(service, file_path, shareable=True):
    filename = os.path.basename(file_path)
    print(filename)

    file_metadata = {'name': filename}
    media = MediaFileUpload(file_path, chunksize=1024 * 1024, resumable=True)
    printy('Uploading ..........................')
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()

    if file.get("id") is not None:
        download_url = f'https://drive.google.com/file/d/{file.get("id")}'
        print_ok(f' APk Uploaded Successfully at : {download_url}')
        # make it visible to anyone with a link if enabled in config.json .
        if shareable:
            service.permissions().create(body={"role": "reader", "type": "anyone"}, fileId=file.get('id')).execute()
        return download_url
    else:
        return None
