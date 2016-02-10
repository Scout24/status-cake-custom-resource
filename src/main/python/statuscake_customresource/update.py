import requests
import json

def update_status_cake(event):
    properties = event['ResourceProperties']
    parameters = {'WebsiteName': properties['WebsiteName'], 'WebsiteURL': properties['WebsiteUrl'],
                  'CheckRate': properties['CheckRate'], 'TestID': event['PhysicalResourceId']}
    headers = {'API': properties['ApiKey'], 'Username': properties['UserName']}
    r = requests.put('https://www.statuscake.com/API/Tests/Update', data=parameters, headers=headers)
    response = r.text
    response_json = json.loads(response)

    output = {'StackId': event['StackId'], 'RequestId': event['RequestId'],
              'LogicalResourceId': event['LogicalResourceId'], 'PhysicalResourceId': str(response_json['InsertID']),
              'Status': 'SUCCESS'}

    requests.put(event['ResponseURL'], data=json.dumps(output))


