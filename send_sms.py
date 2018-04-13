import requests

msg = raw_input('Enter your Message: ')
number = raw_input('Enter the Phone number: ')


payload = {'number': number, 'msg': msg}

r = requests.post("http://textbelt.com/text", data = payload)

if r.json()['success']:
    print('Success!!')
else:
    print('Error!')