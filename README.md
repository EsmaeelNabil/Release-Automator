## Google Drive Python Script.

- this scrip is made for `uploading` files and `notifying` a `slack channel` or `slack conversation`
using `slack Incoming WebHocks`.

- you will need those files in the repo to run the script:
  * `config.json` create it like this and get the receiver from : [Slack WebHocks](https://api.slack.com/messaging/webhooks)
  #####
  ```json
  {
  "enable_slack_notification": true,
  "change_permission": true,
  "receiver": "get this url from Slack incoming web hocks"
  }
    ```
  #####
   * `credentials.json` get it from [Google Python Drive Api](https://developers.google.com/drive/api/v3/quickstart/python) by enabling drive api and downloading the file.  
   #####
  ```json
  {
  "installed": {
    "client_id": "",
    "project_id": "release-bot-uplo-1603483784769",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "",
    "redirect_uris": [
      "urn:ietf:wg:oauth:2.0:oob",
      "http://localhost"
    ]
  }
  }
  ```
  #####
  
  
  #### Usage
  ######
  - `python3 uploader.py -u <filepath> <version or name>` for uploading a file, you should specify a name for the slack notification, `python3 uploader -u <filepath> "name" ` `""` as an empty string