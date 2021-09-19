from app import app
from flask import render_template


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auto_detail')
def auto_detail():
    return render_template('auto_detail.html')

@app.route('/create_auto')
def create_auto():
    return render_template('create_auto.html')

@app.route('/rental_log')
def rental_log():
    return render_template('rental_log.html')