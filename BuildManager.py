import os
import shutil


def valid_android_project():
    valid_files = ['app/build/outputs/apk/debug', 'build', 'gradle', 'gradlew']
    can_build = []
    for file in valid_files:
        if not os.path.exists(file):
            can_build.append(False)
            print("Run this script in root ANDROID STUDIO PROJECT.")
        else:
            can_build.append(True)

    if False in can_build:
        return False
    else:
        return True


def delete_old_build(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def build_and_get_apk_path():
    if valid_android_project():
        call_location = os.getcwd()

        print("\n")
        print("Building started for", os.path.basename(call_location))

        watch_path = f'{call_location}/app/build/outputs/apk/debug'
        delete_old_build(watch_path)

        build_status = os.system("./gradlew assembleDebug")
        if build_status == 0:
            print("\n")
            print("Apk Generated Successfully at : ", watch_path, "\n")
            return watch_path + "/app-debug.apk"
        else:
            print("build failed !!!")
