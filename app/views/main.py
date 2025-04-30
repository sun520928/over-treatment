from flask import Blueprint, request, render_template, redirect

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index/')
def index():
    return render_template('base.html')