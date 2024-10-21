from flask import Flask, request, render_template, redirect, abort, url_for, session
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def default_index():
    return render_template('index.html', text=f'You need to enter your name after slash in url box above!')

@app.route("/<something>")
def index(something=None):
    if something == 'evgenz':
        return redirect(url_for('login', username = something))  
    return render_template('index.html', text=f'There no such page or name as {something}')
    

@app.route('/authenticated/<username>', methods = ['GET', 'POST'])
def login(username):
    if request.method == 'POST':
        return f'{username}, you are post'
    else:
        return f'{username}, you are not post'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug=False)