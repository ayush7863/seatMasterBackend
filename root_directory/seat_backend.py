# from pymongo import MongoClient
from flask import Flask, jsonify, request,json
from flask_cors import CORS
from db import db
from models import User , Movie , Show



app = Flask(__name__)
CORS(app)

# Register route


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if the username already exists
    existing_user = User.objects(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'})

    # Create a new user instance based on the received data
    user = User(
        username=data['username'],
        password=data['password'],
        user_status=data.get('user_status', True),
        gender=data.get('gender', 'Other'),
        membership_type=data.get('membership_type', 'Regular'),
        bio=data.get('bio', ''),
        date_of_birth=data.get('date_of_birth'),


    )
    user.save()

    return jsonify({'message': 'User registered successfully'})

# @app.route("/adminLogin",methods=['POST'])
# def AdminLogin():
#     data=request.get_json()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    # role = data['role']  # Assuming 'role' field is provided in the request data

    # Perform login logic and verify credentials
    user = db.users.find_one({'username': username, 'password': password})

    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username, password, or role'})

# @app.route('/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     user = User(**data)
#     user.save()
#     return jsonify({'message': 'User created successfully'})

# Read User
@app.route('/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    movie = Movie(**data)
    movie.save()
    return jsonify(movie.to_json()), 201  # Convert to JSON here

@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.objects().all()

    # Convert each Movie to a dictionary and then to JSON
    movies_data = [json.loads(movie.to_json()) for movie in movies]

    return jsonify(movies_data), 200
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = User.objects(username=username).first()
    if user:
        user_data = {
            'username': user.username,
            'password': user.password,
            'user_status': user.user_status,
            'gender': user.gender,
            'membership_type': user.membership_type,
            'bio': user.bio,
            'date_of_birth': user.date_of_birth.strftime('%Y-%m-%d'),
            # 'role': user.role
        }
        return jsonify(user_data)
    else:
        return jsonify({'message': 'User not found'})


# Update User
@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    user = User.objects(username=username).first()
    if user:
        data = request.get_json()
        user.update(**data)
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

# Delete User


@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    user = User.objects(username=username).first()
    if user:
        user.delete()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'})


if __name__ == '__main__':
    app.run(debug=True)
