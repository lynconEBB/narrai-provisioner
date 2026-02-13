from flask import Blueprint, redirect, request, current_app

user_bp = Blueprint('user', __name__)

@user_bp.route('/login')
def index():
    return "<h1>Bem-vindo ao NarrAI</h1>"
