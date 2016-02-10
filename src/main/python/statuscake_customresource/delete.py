import requests


def delete_status_cake(event):
    properties = event['ResourceProperties']
    test_id = 12345
    parameters = {'TestID': test_id}
    headers = {'API': properties['apiKey'], 'Username': properties['userName']}
    r = requests.delete('https://www.statuscake.com/API/Tests/Details', data=parameters, headers=headers)
    response = r.text



