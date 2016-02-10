import requests


def delete_status_cake(event):
    test_id = 12345
    parameters = {'TestID': test_id}
    headers = {'API': 'xxxx', 'Username': 'xxxx'}
    r = requests.delete('https://www.statuscake.com/API/Tests/Details', data=parameters, headers=headers)
    response = r.text
    print(response)


event = dict()
delete_status_cake(event)