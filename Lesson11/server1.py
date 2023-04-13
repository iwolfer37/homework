#сервер для завдання 1/2
from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json().get('message')
    if message.lower() == 'Слава нації':
        response = 'Смерть ворогам'
    elif 'нації' in message.lower():
        response = 'Смерть ворогам'
    else:
        response = 'Героям Слава!!'
    messages.append({'user': message, 'bot': response})
    return jsonify({'status': 'OK', 'response': response})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
