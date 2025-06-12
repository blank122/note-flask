from flask import Blueprint, request, jsonify
from ..models.account import Account
from ..extensions import db
from flask_jwt_extended import create_access_token
from datetime import datetime
from ..models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if email already exists
    if Account.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    # Create new user
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        birthdate=data['birthdate'],
    )
    db.session.add(user)
    db.session.flush()  # Assigns an ID to `user` without committing

    # Create new account and link to the user
    account = Account(
        email=data['email'],
        created_at=datetime.utcnow(),
        user_id=user.id  # Grab the auto-generated ID
    )
    account.set_password(data['password'])

    db.session.add(account)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "user_id": user.id}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Account.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/hello', methods=['GET'])
def hello_api():
    return jsonify({"message": "Hello from Flask API Note-app-flask!"}), 200