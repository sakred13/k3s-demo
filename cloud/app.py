from flask import Flask, request, jsonify

app = Flask(__name__)

unprocessed_texts = []
processed_texts = []

@app.route('/unprocessedText', methods=['POST'])
def unprocessed_text():
    text = request.json['text']
    unprocessed_texts.append(text)
    return ('', 200)

@app.route('/processedText', methods=['POST'])
def processed_text():
    text = request.json['text']
    processed_texts.append(text)
    return ('', 200)

@app.route('/getTexts', methods=['GET'])
def get_texts():
    return jsonify({
        'Unprocessed Text from Edge 1': unprocessed_texts,
        'Processed Text from Edge 2': processed_texts
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
