from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def dashboard():
    allUsers = User.getAllUsers()
    return render_template('dashboard.html', users= allUsers)


@app.route('/createUser', methods=['POST'])
def createUser():
    data = {
        'email': request.form['email'],
        'name': request.form['name'],
        'lastName': request.form['lastName']
    }
    User.create_user(data)
    return redirect('/showuser')
@app.route('/showuser')
def showuser():
    allUsers = User.getAllUsers()
    return render_template('showuser.html', users= allUsers)

@app.route('/updateusers/<int:id>')
def updateUsers(id):
    data = {
        'user_id': id,
        }
    user = User.get_user_by_id(data)
    return render_template('updateusers.html', user= user)


@app.route('/updateuser/<int:id>', methods= ['POST'])
def updateUser(id):
    data = {
        'user_id': id,
        'email': request.form['email'],
        'name': request.form['name'],
        'lastName': request.form['lastName']
    }
    user = User.update_users(data)
    return redirect(request.referrer)

@app.route('/usersinfo/<int:id>')
def usersinfo(id):
    data = {
        'user_id': id,
        }
    user = User.get_user_by_id(data)
    return render_template('usersinfo.html', user= user)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'user_id': id,
    }
    User.delete_users(data)
    return redirect(request.referrer)