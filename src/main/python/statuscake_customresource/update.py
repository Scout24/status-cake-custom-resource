import requests

def update_status_cake(event):
    properties = event['ResourceProperties']
    test_id = 1234
    parameters = {'TestID': test_id}
    headers = {'API': properties['ApiKey'], 'Username': properties['UserName']}
    r = requests.put('https://www.statuscake.com/API/Tests/Update', data=parameters, headers=headers)
    response = r.text


