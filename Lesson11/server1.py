#сервер для завдання 1/2
from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json().get('message')
    if message.lower() == 'привіт':
        response = 'Привіт! Як справи?'
    elif message.lower() == 'як тебе звати?':
        response = 'Доброго вечору, я з України, я python-бот. А як тебе?'
    elif 'Україна' in message.lower():
        response = 'Слава Україні! Героям Слава!'
    elif 'Україна' in message.lower():
            response = 'Слава Україні! Героям Слава!'
    else:
        response = 'Слава Україні!'
    messages.append({'user': message, 'bot': response})
    return jsonify({'status': 'OK', 'response': response})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
