from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []


@app.get("/api/tasks")
def list_tasks():
    return jsonify(tasks), 200


@app.post("/api/tasks")
def add_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "deadline": data.get("deadline"),
        "done": False,
    }
    tasks.append(task)
    return jsonify(task), 201
