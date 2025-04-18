from app import app
from flask import request, render_template, jsonify
import requests

@app.route('/')
def index():
    return render_template('index.html')

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = requests.post(OLLAMA_URL, json={
        "model": "gemma3:12b",
        "prompt": user_input,
        "stream": False
    })
    return jsonify({"response": response.json()["response"]})