#  from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     # print request headers
#     print(f"Headers: {request.headers}")
#     print(f"Content-Type: {request.content_type}")

#     # Check Content-Type
#     if request.content_type != 'application/json':
#         return jsonify({"error": "Invalid Content-Type"}), 415

#     # Parsing JSON data
#     try:
#         data = request.json
#         print(f"Received data: {data}")
#     except Exception as e:
#         print(f"Error parsing JSON: {e}")
#         return jsonify({"error": "Failed to parse JSON"}), 400

#     return jsonify({"message": "Webhook received", "data": data}), 200

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=3000)


from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Webhooks handle routing
@app.route('/webhook', methods=['POST'])
def webhook():
    # Gets the GitHub event type
    event = request.headers.get('X-GitHub-Event')
    data = request.json

    # Handling ping events
    if event == 'ping':
        print("Received ping event")
        return jsonify({"message": "Ping event received"}), 200

    # Deal with issues
    if event == 'issues':
        issue_title = data.get('issue', {}).get('title', '')

    # Fire the corresponding Python script based on the Issue title
    if "Run Calculator" in issue_title:
        script = "src/calculator.py"
    elif "Run Guess" in issue_title:
        script = "src/guess_number.py"
    elif "Run Hello" in issue_title:
        script = "src/hello_world.py"
    elif "Run Monitor" in issue_title:
        script = "src/monitor_directory.py"
    else:
        return jsonify({"error": "Unknown command"}), 400

    # Run the corresponding Python script
    try:
        result = subprocess.run(["python", script], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
    except Exception as e:
        return jsonify({"error": f"Failed to run script: {str(e)}"}), 500

    # Return execution result
    return jsonify({
        "message": "Script executed",
        "output": output,
        "error": error
    }), 200



# Launching Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
