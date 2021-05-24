from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):

        return redirect('/')
