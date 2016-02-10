import requests

def update_status_cake(event):
    test_id = 12345
    parameters = {'TestID': test_id, 'WebsiteName': 'autoscout24'}
    headers = {'API': 'xxx', 'Username': 'xxx'}
    r = requests.put('https://www.statuscake.com/API/Tests/Update', data=parameters, headers=headers)
    response = r.text
    print(response)


event=dict()
update_status_cake(event)

