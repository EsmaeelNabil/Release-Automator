import os


def getApkName(apk_path):
    return os.path.basename(apk_path).replace(".apk", "")


# rename a file if provided with a valid path and name
def renameApk(old_path, new_name):
    if old_path is not None and new_name is not None:
        old_name = f'{os.path.basename(old_path)}'
        # print('old_name', old_name)
        old_path_without_file = old_path.replace(old_name, "")
        # print('old_path_without_file', old_path_without_file)
        new_path = f'{old_path_without_file}{new_name}.apk'
        # print('new_path', new_path)
        os.rename(old_path, new_path)
        return new_path
    else:
        return old_path

# print(renameFile('muhla v5.apk', "muhla v999"))
