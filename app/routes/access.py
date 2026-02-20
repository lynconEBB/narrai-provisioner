from flask import Blueprint, redirect, request, current_app, render_template
import app.services.access_service as access_service

access_bp = Blueprint('access', __name__)

@access_bp.route('/login')
def index():
    return render_template("access.html")
