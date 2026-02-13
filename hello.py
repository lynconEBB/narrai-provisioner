from flask import Flask, render_template, Response, redirect, request

app = Flask(__name__)
PORTAL_URL = "http://narrai-provision.com/login"

@app.route('/login')
def index():
    return "<h1>Bem-vindo ao NarrAI</h1>"

#Linux
@app.route('/')
@app.route('/check_network_status.txt')
# Windows
@app.route('/connecttest.txt')
@app.route('/redirect')
@app.route('/ncsi.txt')
# Android
@app.route('/generate_204')
@app.route('/gen_204')
# Apple
@app.route('/hotspot-detect.html')
@app.route('/success.txt')
def catch_all():
    return redirect(PORTAL_URL, code=302)