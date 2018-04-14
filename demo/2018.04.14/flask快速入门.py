#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/4/12 0012 14:53
# @author  : zza
# @Email   : 740713651@qq.com

from flask import Flask, redirect, url_for, abort, render_template, request, flash

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'


@app.route('/a/')
def home():
    return '<h1>Hello World322!</h1>'



@app.route('/login2/')
def login2():
    abort(404)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'aaa' or \
                request.form['password'] != 'aaa':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0')
