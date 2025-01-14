from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index")
def index():
    return "<p>Index Page</p>"

#HTTP Methods
#Flask. By default, a route only answers to GET requests
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
#Rendering Templates
#https://jinja.palletsprojects.com/templates/
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route("/projects/")
def projects():
    return "<p>The project page</p>"

'''
@app.route("/name/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
'''
    
@app.route('/user/<username>')
def profile(username):
    #show the user profile for that user
    return f'{escape(username)}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'

#stampa sul terminale i valori restituiti dalla funzione di reversin url
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('static', filename='css/templates.css'))
