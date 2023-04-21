import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Створюємо файл логів
file_handler = logging.FileHandler('server.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json().get('message')
    if message.lower() == 'слава україні':
        response = 'Героям слава'
    elif message.lower() == 'слава нації':
        response = 'Смерть ворогам'
    elif message.lower() == 'Україна':
        response = 'Понад усе!'
    else:
        response = 'Ви Українець? Пароль?'
    messages.append({'user': message, 'bot': response})
    logger.info('User sent message: %s', message)
    logger.info('Bot responded with: %s', response)
    return jsonify({'status': 'OK', 'response': response})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)