# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is the homepage of the simple Flask application for AWS Elastic Beanstalk.'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us at contact@example.com.'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
