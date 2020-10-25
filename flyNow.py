import os
import sys

import BuildManager

root = os.path.dirname(__file__)


def main():
    comment = " "
    if len(sys.argv) > 1:
        comment = sys.argv[1]

    uploader_path = f'{root}/uploader.py'
    command = f'python3 {uploader_path} -u {BuildManager.build_and_get_apk_path()} {comment}'
    os.system(command)


if __name__ == '__main__':
    main()
