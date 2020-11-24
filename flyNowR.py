import json
import os
import sys
import argparse

import AuthManager
import BuildManager
import SlackNotifier
import fileUtils
import uploader
from printer import *

root = os.path.dirname(__file__)
config = json.load(open(f'{root}/config.json'))
enabled = 1
not_provided = 0


def main():
    parser = argparse.ArgumentParser(prog='flyNow.py', usage='%(prog)s [options]')
    parser.add_argument('-m', '--message', nargs='?', default='',
                        help='Notification content string default will be file name if message is empty')
    parser.add_argument('-r', '--rename', nargs='?', default=not_provided,
                        help='rename APK if provided with 1 ')
    parser.add_argument('-n', '--notify', nargs='?', help='Enable or disable slack notification, default is enabled',
                        default=enabled)
    parser.add_argument('-rc', '--receiver', nargs='?', default=config["receiver"],
                        help='slack receiver channel hock url will be used from config if not provided.')

    parser.print_help()
    args = parser.parse_args()
    # print(args)

    # slack channel hock channel
    printWarning(f" default receiver channel hock url will be used from config.json if receiver is not provided \n"
                 f"       used channel --> {args.receiver}")

    use_file_name_as_message = False
    # message that will be sent
    if args.message is None or args.message == "":
        use_file_name_as_message = True
        printWarning(f'file name will be used as a message')

    # build
    apk_path = BuildManager.build_and_get_apk_path()

    # rename Apk if rename provided
    if args.rename != not_provided:
        apk_path = fileUtils.renameApk(apk_path, args.rename)

    # upload
    if apk_path is not None:
        # Authenticate
        service = AuthManager.authenticate_if_needed()
        # upload the apk and get the file url
        upload_path = uploader.upload_file(service=service, file_path=apk_path, shareable=True)
        if upload_path is not None:
            # is slack notification enable send message with download url
            if args.notify == enabled:
                SlackNotifier.notify(
                    message=f'{fileUtils.getApkName(apk_path)} {args.message}',
                    download_url=upload_path,
                    receiver=args.receiver
                )


if __name__ == '__main__':
    main()
