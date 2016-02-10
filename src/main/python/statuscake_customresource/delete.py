import requests
import json


def delete_status_cake(event):
    properties = event['ResourceProperties']
    test_id = 12345
    parameters = {'TestID': test_id}
    headers = {'API': properties['ApiKey'], 'Username': properties['UserName']}
    r = requests.delete('https://www.statuscake.com/API/Tests/Details', data=parameters, headers=headers)
    response = r.text

    output = {'StackId': event['StackId'],
              'RequestId': event['RequestId'],
              'LogicalResourceId': event['LogicalResourceId'],
              'PhysicalResourceId': event['PhysicalResourceId']}
    output['Status'] = 'SUCCESS'

    requests.put(event['ResponseURL'], data=json.dumps(output))
