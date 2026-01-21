from flask import Flask, jsonify, request
import requests
import threading
import time

app = Flask(__name__)

# Global variable to store current Bitcoin price
bitcoin_price = {"price": 0, "timestamp": None}
price_lock = threading.Lock()

def update_bitcoin_price():
    """Fetch Bitcoin price from CoinGecko API every second"""
    while True:
        try:
            response = requests.get(
                'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
            )
            if response.status_code == 200:
                data = response.json()
                price = data.get('bitcoin', {}).get('usd', 0)
                with price_lock:
                    bitcoin_price['price'] = price
                    bitcoin_price['timestamp'] = time.time()
        except Exception as e:
            print(f"Error fetching Bitcoin price: {e}")
        
        time.sleep(1)  # Update every second

# Start background thread for price updates
price_thread = threading.Thread(target=update_bitcoin_price, daemon=True)
price_thread.start()

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/user', methods=['GET'])
def get_user():
    return jsonify({
        "username": "john_doe",
        "user_id": 12345,
        "email": "john_doe@example.com"
    })

@app.route('/about')
def about():
    return "About Page"

@app.route('/bitcoin-price', methods=['GET'])
def get_bitcoin_price():
    with price_lock:
        return jsonify({
            "currency": "bitcoin",
            "price_usd": bitcoin_price['price'],
            "timestamp": bitcoin_price['timestamp']
        })

if __name__ == '__main__':
    app.run(debug=True)

