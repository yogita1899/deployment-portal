from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/register-service', methods=['POST'])
def register_service():

    data = request.get_json(force=True)

    print("Received data:", data)

    service_name = data.get('service_name')
    team_name = data.get('team_name')
    repo_url = data.get('repo_url')

    if not service_name or not team_name or not repo_url:
        return jsonify({"error": "Missing required fields"}), 400

    print("Service:", service_name)
    print("Team:", team_name)
    print("Repo:", repo_url)

    return jsonify({
        "message": "Service registered successfully",
        "service": service_name
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)