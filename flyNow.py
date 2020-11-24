import os
import sys
import argparse

import BuildManager

root = os.path.dirname(__file__)


def main():
    parser = argparse.ArgumentParser(prog='flyNow.py', usage='%(prog)s [options]')
    parser.add_argument('--m', nargs='?', help='foo help')
    parser.add_argument('--channel', nargs='?', help='foo help')

    args = parser.parse_args()
    print(args)
    # comment = " "
    # if len(sys.argv) > 1:
    #     comment = sys.argv[1]
    #
    # uploader_path = f'{root}/uploader.py'
    # command = f'python3 {uploader_path} -u {BuildManager.build_and_get_apk_path()} {comment}'
    # os.system(command)

    # def main():
    # comment = " "
    # if len(sys.argv) > 1:
    #     comment = sys.argv[1]
    #
    # uploader_path = f'{root}/uploader.py'
    # command = f'python3 {uploader_path} -u {BuildManager.build_and_get_apk_path()} {comment}'
    # os.system(command)


if __name__ == '__main__':
    main()
