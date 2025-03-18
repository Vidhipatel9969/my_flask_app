from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# In-memory storage
feedback_data = []
projects = [
    {"title": "Project 1", "description": "E-commerce Platform"},
    {"title": "Project 2", "description": "Social Media Analytics"}
]

class FeedbackForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=2, max=50)])
    email = StringField('Email', [validators.Email()])
    message = TextAreaField('Message', [validators.Length(min=10, max=500)])

# Internal API Endpoints
@app.route('/api/projects')
def get_projects():
    return jsonify(projects)

@app.route('/api/feedback')
def get_feedback():
    return jsonify(feedback_data)

# External API Integration
@app.route('/github-proxy')
def github_proxy():
    response = requests.get('https://api.github.com/users/yourusername/repos')
    return jsonify(response