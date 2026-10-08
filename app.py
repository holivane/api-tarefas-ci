from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "title": data["title"]}
    tasks.append(task)
    return task, 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks)
