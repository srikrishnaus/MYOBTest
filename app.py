from flask import Flask, render_template, make_response, jsonify
import urllib.request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to test Server'


@app.route('/greet')
def say_hello():
    return 'Hello from Server'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'page not found'}), 404)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/metadata')
def return_metadata():
    data = {'message': 'Created', 'code': 'SUCCESS'}
    return jsonify(Version='1.0', description='pre-interview technical test')


