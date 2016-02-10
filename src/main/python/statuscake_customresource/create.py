import requests
import json


def create_status_cake(event):
    properties = event['ResourceProperties']
    parameters = {'WebsiteName': properties['WebsiteName'], 'WebsiteURL': properties['WebsiteUrl'],
                  'CheckRate': properties['CheckRate']}
    headers = {'API': properties['ApiKey'], 'Username': properties['UserName']}
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
    print(event)
    print(output)

    requests.put(event['ResponseURL'], data=json.dumps(output))
