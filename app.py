# app.py
from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_URL = 'https://api.deepseek.com/v1/chat/completions'

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        headers = {
            'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Forward the request to DeepSeek API
        response = requests.post(
            DEEPSEEK_URL,
            headers=headers,
            json=request.json
        )
        
        return jsonify(response.json())
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to process request'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
