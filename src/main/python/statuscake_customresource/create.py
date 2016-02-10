import requests
import json


def create_status_cake(event):
    properties = event['ResourceProperties']
    parameters = {'WebsiteName': properties['websiteName'], 'WebsiteURL': properties['websiteUrl'], 'CheckRate': properties['checkRate']}
    headers = {'API':  properties['apiKey'], 'Username': properties['userName']}
    r = requests.put('https://www.statuscake.com/API/Tests/Update', data=parameters, headers=headers)
    response = r.text

    output = {
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'PhysicalResourceId': 'failed'
    }
    response_json = json.loads(response)
    output['Status'] = 'SUCCESS'
    output['PhysicalResourceId'] = response_json['InsertID']

