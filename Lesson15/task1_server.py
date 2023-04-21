import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json().get('message')
    if message.lower() == 'Героям слава':
        response = 'Слава нації'
    elif 'ворогам' in message.lower():
        response = 'Україна'
    else:
        response = 'Слава Україні!!'
    messages.append({'user': message, 'bot': response})
    logger.info('User sent message: %s', message)
    logger.info('Bot responded with: %s', response)
    return jsonify({'status': 'OK', 'response': response})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
