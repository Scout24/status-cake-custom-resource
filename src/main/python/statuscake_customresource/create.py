import requests
import json


def create_status_cake(event):
    parameters = {'WebsiteName': 'www.autoscout24.de', 'WebsiteURL': 'www.autoscout24.de', 'CheckRate': 900}
    headers = {'API': 'xxxx', 'Username': 'xxxx'}
    r = requests.put('https://www.statuscake.com/API/Tests/Update', data=parameters, headers=headers)
    response = r.text

    output = {
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'PhysicalResourceId': 'failed'
    }
    response_json = json.loads(response)
    InsertID = response_json['InsertID']
    output['PhysicalResourceId'] = response_json['InsertID']

