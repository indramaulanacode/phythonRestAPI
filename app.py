from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory data storage (in production, use a database)
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "created_at": "2024-01-01T00:00:00"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "created_at": "2024-01-02T00:00:00"}
]

# Helper function to find user by ID
def find_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)

# Helper function to get next user ID
def get_next_user_id():
    return max([user["id"] for user in users], default=0) + 1

# Root endpoint
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the RESTful API",
        "version": "1.0.0",
        "endpoints": {
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Create new user",
            "PUT /users/<id>": "Update user by ID",
            "DELETE /users/<id>": "Delete user by ID"
        }
    })

# GET /users - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    # Optional query parameters for pagination
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    start = (page - 1) * limit
    end = start + limit
    
    paginated_users = users[start:end]
    
    return jsonify({
        "data": paginated_users,
        "total": len(users),
        "page": page,
        "limit": limit,
        "total_pages": (len(users) + limit - 1) // limit
    })

# GET /users/<id> - Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        return jsonify({"data": user})
    return jsonify({"error": "User not found"}), 404

# POST /users - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validate required fields
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    # Check if email already exists
    if any(user['email'] == data['email'] for user in users):
        return jsonify({"error": "Email already exists"}), 400
    
    # Create new user
    new_user = {
        "id": get_next_user_id(),
        "name": data['name'],
        "email": data['email'],
        "created_at": datetime.now().isoformat()
    }
    
    users.append(new_user)
    
    return jsonify({
        "message": "User created successfully",
        "data": new_user
    }), 201

# PUT /users/<id> - Update user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Update user fields
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        # Check if new email already exists (excluding current user)
        if any(u['email'] == data['email'] and u['id'] != user_id for u in users):
            return jsonify({"error": "Email already exists"}), 400
        user['email'] = data['email']
    
    user['updated_at'] = datetime.now().isoformat()
    
    return jsonify({
        "message": "User updated successfully",
        "data": user
    })

# DELETE /users/<id> - Delete user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users.remove(user)
    
    return jsonify({
        "message": "User deleted successfully",
        "data": user
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)