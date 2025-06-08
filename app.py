from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests
import socket
import json

load_dotenv()

app = Flask(__name__)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-train-route', methods=['POST'])
def get_train_route():
    data = request.get_json()
    train_number = data.get('trainNumber')
    
    if not train_number:
        return jsonify({'error': 'Train number is required'}), 400
    
    url = os.getenv('RAPIDAPI_URL')
    headers = {
        'X-RapidAPI-Key': os.getenv('RAPIDAPI_KEY'),
        'X-RapidAPI-Host': os.getenv('RAPIDAPI_HOST')
    }
    
    try:
        response = requests.get(f"{url}/train/{train_number}", headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        if not data or 'stations' not in data:
            return jsonify({'error': 'Invalid response from API'}), 500
            
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API Error: {str(e)}'}), 500
    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON response from API'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get-live-status', methods=['POST'])
def get_live_status():
    data = request.get_json()
    train_number = data.get('trainNumber')
    date = data.get('date')
    
    url = os.getenv('RAPIDAPI_URL')
    headers = {
        'X-RapidAPI-Key': os.getenv('RAPIDAPI_KEY'),
        'X-RapidAPI-Host': os.getenv('RAPIDAPI_HOST')
    }
    
    try:
        response = requests.get(f"{url}/status/{train_number}/{date}", headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    local_ip = get_local_ip()
    app.run(host=local_ip, port=5000, debug=True)
