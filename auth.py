# Import packages
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
import json
from models import User
 
f = open('./utils/accounts.json')
data = json.load(f)
f.close()

accountsJSON = data.keys()
user1 = User()
auth = Blueprint('auth', __name__) 

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
                
        userDetails = [i for i in data["data"] if email in i['email']]
        print(userDetails[0]['password']==str(password))
        
        user1.name = userDetails[0]['name']
        user1.password = userDetails[0]['password']
        user1.email = userDetails[0]['email']
        user1.id = userDetails[0]['id']

        if len(userDetails) == 0:
            flash('Please sign up before!')
            return redirect(url_for('auth.signup'))
        elif userDetails[0]["password"] != password: # not check_password_hash(
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) 

        login_user(user1, remember=remember)
        return redirect(url_for('main.profile', name = user1.name))

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method=='GET': 
        return render_template('signup.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        userDetails = [i for i in data["data"] if email in i['email']]
        
        if len(userDetails) != 0:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        else:
            id = len(data) + 1
            data['data'].append({"email": email, "name": name, "password": password, 'id':id})
            with open('./utils/accounts.json', 'w') as f:
                json.dump(data, f)
                f.close()
            
        return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    