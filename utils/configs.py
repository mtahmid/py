import os

# For local testing, remove firefox to avoid test running twice on chromedriver
# TO DO: point firefox to execute local geckodriver
browsers = ['chrome']

client = dict(
    user=os.environ['UI_LOGIN_USER'],
    password=os.environ['UI_LOGIN_PASSWORD']
)

url = os.getenv('PYMETRICS_HOST', 'https://staging.pymetrics.com')
