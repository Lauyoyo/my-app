from flask import Flask, request, jsonify
from github import GithubIntegration
import hmac
import hashlib
import os
from dotenv import load_dotenv

# Load environment variable
load_dotenv()

app = Flask(__name__)

# Read a configuration from an environment variable
APP_ID = os.getenv("APP_ID")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY", "").replace("\\n", "\n")

# Validate environment variables
if not APP_ID or not WEBHOOK_SECRET or not PRIVATE_KEY:
    raise ValueError("❌ APP_ID, WEBHOOK_SECRET, or GITHUB_PRIVATE_KEY is not set or invalid")

print("✅ All environment variables loaded successfully.")


# Initialize the GitHub API client
def get_github_client():
    try:
        integration = GithubIntegration(APP_ID, PRIVATE_KEY.encode())
        return integration
    except Exception as e:
        raise ValueError(f"Failed to initialize GitHub client: {str(e)}")

# Verify the Webhook signature
def verify_signature(payload, signature):
    hash_object = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    return hmac.compare_digest(signature, expected_signature)

# Webhook endpoint
@app.route("/webhook", methods=["POST"])
def handle_webhook():
    # Verify signature
    signature = request.headers.get("X-Hub-Signature-256")
    payload = request.data

    if not signature or not verify_signature(payload, signature):
        return jsonify({"error": "Invalid signature"}), 401

    # Process event
    event = request.headers.get("X-GitHub-Event")
    payload_json = request.json

    try:
        # Feature 1: Monitor folder changes (when code is pushed)
        if event == "push":
            print(f"📁 [Monitor folder] Push event detected, submitter: {payload_json['pusher']['name']}")

        # Feature 2: Issue triggers calculator
        elif event == "issues" and payload_json.get("action") == "opened":
            issue_body = payload_json["issue"]["body"].strip()

            if issue_body.startswith("compute:"):
                expression = issue_body.replace("compute:", "").strip()
                try:
                    result = eval(expression)
                    reply = f"✅ Calculation result: {result}"
                except Exception as e:
                    reply = f"❌ Calculation failed: {str(e)}"

            elif issue_body.startswith("Guess number:"):
                number_to_guess = 42  # Fixed sample answer
                try:
                    guess = int(issue_body.replace("Guess number:", "").strip())
                    if guess == number_to_guess:
                        reply = "🎉 Congratulations, you guessed right!"
                    else:
                        reply = f"❌ Guess wrong! The correct answer is {number_to_guess}."
                except ValueError:
                    reply = "⚠️ Please enter a valid number!"

            else:
                reply = "🤔 Unknown command. Please use 'compute:' or 'Guess number:'"

            # Reply to the issue via GitHub API
            repo_name = payload_json["repository"]["full_name"]
            issue_number = payload_json["issue"]["number"]

            # Create GitHub client and post comment
            integration = get_github_client()
            repo = integration.get_repo(repo_name)
            issue = repo.get_issue(issue_number)
            issue.create_comment(reply)

        # Feature 3: Hello World (when the App is installed)
        elif event == "installation" and payload_json.get("action") == "created":
            print("✅ Hello, World! App Installed.")

        else:
            print("⚠️ No matching event found, skipping processing.")

    except Exception as e:
        print(f"❌ An error occurred while processing an event: {str(e)}")

    return jsonify({"status": "success"})

# Health check endpoint
@app.route('/')
def home():
    return "Flask app is running!"

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)