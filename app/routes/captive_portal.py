import os
from flask import Blueprint, redirect

captive_bp = Blueprint('captive', __name__)

#Linux
@captive_bp.route('/')
@captive_bp.route('/check_network_status.txt')
# Windows
@captive_bp.route('/connecttest.txt')
@captive_bp.route('/redirect')
@captive_bp.route('/ncsi.txt')
# Android
@captive_bp.route('/generate_204')
@captive_bp.route('/gen_204')
# Apple
@captive_bp.route('/hotspot-detect.html')
@captive_bp.route('/success.txt')
def catch_all():
    return redirect(os.getenv("APP_URL"), code=302)
