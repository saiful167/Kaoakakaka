from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/fetch', methods=['POST'])
def fetch_video():
    try:
        data = request.get_json()
        video_url = data.get('q')

        if not video_url:
            return jsonify({"status": "error", "message": "No URL provided"}), 400

        api_url = "https://tikdownloader.io/api/ajaxSearch"
        payload = {'q': video_url, 'lang': 'en'}
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        response = requests.post(api_url, data=payload, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Vercel-এর জন্য জরুরি
def handler(event, context):
    return app(event, context)

