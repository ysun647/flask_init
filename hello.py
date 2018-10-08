import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    # print("The type of the username is ", type(username))
    return "User %s" % username

@app.route('/hello')
def hello_world():
    return 'hello world'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    print("The type of post_id is", type(post_id))
    return "Post %d" % post_id

if __name__ == '__main__':
    # set up IP address and port
    # host = os.getenv("IP", "0.0.0.0")
    # port = int(os.getenv("PORT", 5000))

    # debug mode, should be false at production env
    app.debug = True
    app.run()