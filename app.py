
#This is Passthrough Server which translates incoming POST calls via webhook
#to any REST API!
#Author: TS
#Date: 11-05-2025
import logging
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

#BASE_URL = "https://681ddf27c1c291fa6631fe9f.mockapi.io/MRE/"

@app.route('/webhook_2_any_rest', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    serverurl = data.get("baseurl", "")
    httpverb = data.get("httpverb", "").upper()
    endpoint = data.get("endpoint", "")
    content = data.get("content", {})

    app.logger.info(f"Received webhook: verb={httpverb}, endpoint={endpoint}, content={content}")

    if not httpverb or not endpoint or not serverurl:
        app.logger.warning("Missing httpverb or endpoint or baseurl in the payload")
        return jsonify({"error": "Missing httpverb or endpoint or baseurl"}), 400

    url = f"{serverurl.rstrip('/')}{endpoint.lstrip('/')}"
    try:
        response = requests.request(httpverb, url, json=content)
        app.logger.info(f"Forwarded request to {url} with status {response.status_code}")
        return jsonify({
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "body": response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
        }), response.status_code
    except Exception as e:
        app.logger.error(f"Error during request forwarding: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
