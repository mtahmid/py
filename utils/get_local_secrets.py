import os

import csv


def hasSecrets():
    return os.path.exists(os.getcwd() +
                          '/secrets/in-use/secrets.csv')


def extractSecrets(csvfile):
    testSecrets = {}
    reader = csv.DictReader(csvfile, delimiter=',')
    for record in reader:
        testSecrets[record['test_key']] = {
            'test_key': record['test_key'],
            'success': record['success'],
            'invite_link': record['invite_link'],
            'username': record['username'],
            'password': record['password']
        }
    return testSecrets
