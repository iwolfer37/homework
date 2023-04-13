from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wordcount', methods=['POST'])
def word_count():
    data = request.get_json()
    phrase = data['phrase']
    word_count = len(phrase.split())
    return {'word_count': word_count}

if __name__ == '__main__':
    app.run(port=8080)

