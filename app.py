from flask import Flask, request, jsonify
import hmac
import hashlib
import subprocess
import os

app = Flask(__name__)
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET', 'your_webhook_secret')


@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256")
    if not signature:
        return jsonify({"error": "Missing signature"}), 400

     # Computational hash
    body = request.data
    hash_object = hmac.new(WEBHOOK_SECRET.encode(), body, hashlib.sha256)
    expected_signature = 'sha256=' + hash_object.hexdigest()
    

    if not hmac.compare_digest(signature, expected_signature):
        return jsonify({"error": "Invalid signature"}), 401

    # Handling GitHub events
    event = request.headers.get('X-GitHub-Event')
    payload = request.json

    if event == 'issues' and 'issue' in payload:
        issue_title = payload['issue'].get('title', 'No title')
        print(f"New issue created: {issue_title}")

    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)


