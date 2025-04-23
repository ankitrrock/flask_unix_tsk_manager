from flask import Blueprint, request, jsonify
from app.models import db, Task
from datetime import datetime, timezone

task_bp = Blueprint('mtask_bp', __name__)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()

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
    tasks = Task.query.all()
    return jsonify([
        {
            "id": task.id,
            "name": task.name,
            "status": task.status,
            "created_at": task.created_at.isoformat()
        } for task in tasks
    ])


# ✅ GET Task by ID
@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "id": task.id,
        "name": task.name,
        "status": task.status,
        "created_at": task.created_at.isoformat()
    })


# ✅ DELETE Task by ID
@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": f"Task {task_id} deleted successfully"}), 200
