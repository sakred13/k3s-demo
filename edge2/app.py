from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/unprocessedText', methods=['POST'])
def unprocessed_text():
    text = request.json['text']
    # Make a POST request to master-pod
    response = requests.post('http://cloud-service:5000/processedText', json={'text': text})
    return ('', 200)

@app.route('/capitalizeText', methods=['POST'])
def capitalize_text():
    text = request.json['text'].upper()
    # Make a POST request to master-pod
    response = requests.post('http://cloud-service:5000/processedText', json={'text': text})
    return ('', 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
