from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.get_json().get('message')
    if message.lower() == 'привіт':
        response = 'Привіт! Як справи?'
    elif message.lower() == 'як тебе звати?':
        response = 'Мене звати Чат-бот. А як тебе?'
    elif 'погода' in message.lower():
        response = 'Зараз сонячно і тепло!'
    else:
        response = 'Дякую за повідомлення!'
    messages.append({'user': message, 'bot': response})
    return jsonify({'status': 'OK', 'response': response})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
