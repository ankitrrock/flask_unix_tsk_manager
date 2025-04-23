from flask import Blueprint, request, jsonify
from app.models import db, Task
from datetime import datetime, timezone

task_bp = Blueprint('mtask_bp', __name__)

# Hardcoded token for demo purposes
VALID_TOKEN = "0000"

# Auth helper
def is_token_valid(data):
    token = data.get("access_token")
    return token == VALID_TOKEN

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()

    if not is_token_valid(data):
        return jsonify({'error': 'Invalid access token'}), 401

    name = data.get('name')
    if not name:
        return jsonify({'error': 'Task name is required'}), 400

    task = Task(
        name=name,
        status="created",
        created_at=datetime.now(timezone.utc)
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "id": task.id,
        "name": task.name,
        "status": task.status,
        "created_at": task.created_at.isoformat()
    }), 201


@task_bp.route('/tasks', methods=['GET'])
def list_tasks():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()
    if not is_token_valid(data):
        return jsonify({'error': 'Invalid access token'}), 401

    tasks = Task.query.all()
    return jsonify([
        {
            "id": task.id,
            "name": task.name,
            "status": task.status,
            "created_at": task.created_at.isoformat()
        } for task in tasks
    ])


@task_bp.route('/tasks/<int:task_id>', methods=['POST'])
def get_task(task_id):
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()
    if not is_token_valid(data):
        return jsonify({'error': 'Invalid access token'}), 401

    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "name": task.name,
        "status": task.status,
        "created_at": task.created_at.isoformat()
    })


@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()
    if not is_token_valid(data):
        return jsonify({'error': 'Invalid access token'}), 401

    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": f"Task {task_id} deleted successfully"}), 200
