from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (dictionary)
users = {}
next_id = 1


# Home Route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to User Management REST API"})


# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id]), 200


# POST - Add new user
@app.route("/users", methods=["POST"])
def add_user():
    global next_id

    data = request.json

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and Email required"}), 400

    users[next_id] = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"]
    }

    next_id += 1

    return jsonify({"message": "User created successfully"}), 201


# PUT - Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify({"message": "User updated successfully"}), 200


# DELETE - Remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
