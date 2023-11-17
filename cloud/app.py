from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

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
