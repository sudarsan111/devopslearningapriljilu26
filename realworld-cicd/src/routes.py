from flask import Blueprint, jsonify, request
from . import models

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.get("/")
def health():
    return jsonify({"status": "ok", "service": "task-manager"})

@tasks_bp.get("/tasks")
def list_tasks():
    return jsonify([t.to_dict() for t in models.get_all()])

@tasks_bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    if not title:
        return jsonify({"error": "title is required"}), 400
    task = models.create(title=title, description=data.get("description", ""))
    return jsonify(task.to_dict()), 201

@tasks_bp.get("/tasks/<task_id>")
def get_task(task_id: str):
    task = models.get_by_id(task_id)
    if task is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(task.to_dict())

@tasks_bp.put("/tasks/<task_id>")
def update_task(task_id: str):
    data = request.get_json(silent=True) or {}
    allowed = {k: v for k, v in data.items() if k in ("title", "description", "done")}
    task = models.update(task_id, **allowed)
    if task is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(task.to_dict())

@tasks_bp.delete("/tasks/<task_id>")
def delete_task(task_id: str):
    if not models.delete(task_id):
        return jsonify({"error": "not found"}), 404
    return "", 204
