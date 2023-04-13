import requests

url = 'http://127.0.0.1:8080/wordcount'
data = {'text': 'це тестовий текст для підрахунку слів'}

response = requests.post(url, data=data)

if response.ok:
    wordcount = response.json().get('wordcount')
    print(f'Кількість слів: {wordcount}')
else:
    print('Помилка запиту')
