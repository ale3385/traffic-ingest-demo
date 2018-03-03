# Install Steps

<a href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/ranshers/traffic-ingest-demo&page=editor&open_in_editor=README.md">
<img alt="Open in Cloud Shell" src ="http://gstatic.com/cloudssh/images/open-btn.png"></a>

1. Authenticate into account, gcloud auth login
2. Setup project folder, gcloud config set project gcp-traffic-demo
3. Install all required packages into local lib folder: pip install -r requirements.txt -t lib
4. To deploy App Engine app, run: gcloud app deploy app.yaml
5. To deploy App Engine CRON, run: gcloud app deploy cron.yaml


