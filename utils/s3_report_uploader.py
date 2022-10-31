import boto3
import glob
import os


reports = glob.glob("./reports/*.html")
latest_report = max(reports, key=os.path.getctime)
fname = os.path.basename(latest_report)
s3 = boto3.client('s3')

try:
    s3.upload_file(
        latest_report, 'pymetrics-ui-test-results', fname)
    print('Successfully uploaded ' + latest_report +
          ' to bucket pymetrics-ui-test-results')
except Exception as e:
    print(e)
