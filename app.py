from flask import Flask, url_for
 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
 
@app.route("/index")
def index():
    return "Index Page"

@app.route("/user/<username>")
def show_user_profile(username):
    return 'User %s' % username

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)
    # with app.test_request_context():
    #     print(url_for('hello'))
    #     print(url_for('index'))
    #     print(url_for('index', next='/'))
    #     print(url_for('show_user_profile', username="김홍교"))
