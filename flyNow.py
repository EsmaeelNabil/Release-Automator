import os
import sys

import BuildManager


def main():
    print(sys.argv)
    comment = " "
    if len(sys.argv) > 1:
        comment = sys.argv[1]

    print(os.getcwd())
    command = f'python3 /home/esmaeel/PycharmProjects/pythonProject/uploader.py -u {BuildManager.build_and_get_apk_path()} {comment}'
    os.system(command)
    # apk_path =


if __name__ == '__main__':
    main()
