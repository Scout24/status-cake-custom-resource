import requests
import json


def delete_status_cake(event):
    properties = event['ResourceProperties']
    parameters = {'TestID': event['PhysicalResourceId']}
    headers = {'API': properties['ApiKey'], 'Username': properties['UserName']}
    requests.delete('https://www.statuscake.com/API/Tests/Details', data=parameters, headers=headers)

    output = {'StackId': event['StackId'], 'RequestId': event['RequestId'],
              'LogicalResourceId': event['LogicalResourceId'], 'PhysicalResourceId': str(event['PhysicalResourceId']),
              'Status': 'SUCCESS'}

    requests.put(event['ResponseURL'], data=json.dumps(output))
