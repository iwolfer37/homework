import requests
import time

while True:
    message = input('Введіть повідомлення: ')
    requests.post('http://localhost:5000/send_message', json={'message': message})
    time.sleep(1)
    response = requests.get('http://localhost:5555/get_messages')
    messages = response.json().get('messages')
    for message in messages:
        print(message)