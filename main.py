'''
This file is the main file that runs user login. Once the user logs into the website this python script is executed.
Whatever is the user's name and session and also the metric to watch, is fetched by this file. Once all the details are recieved from the user via the webpage, this script will call the main API (app.py) and app.py will returns the corresponding values to the user
'''



# Import packages 
from flask import Blueprint, render_template, flash, Flask,request
from flask_login import login_required, current_user
from __init__ import create_app
import requests
import os 
import matplotlib.pyplot as plt

# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile/<name>',methods =["GET","POST"]) # profile page that return 'profile'
#@login_required
def profile(name):
    sessions = [session_name.split(".")[0] for session_name in os.listdir("data\\"+name) if session_name.endswith(".json")]
    print(sessions)
    if request.method == 'POST':
        url = "http://127.0.0.1:3000/" 
        username = name
        session = request.form["session"]
        metric = request.form["metric"] 

        try:
            response = requests.get(url=url, data= {'username':username,'session':session,'metric':metric}) 
            resp1 = response.text.split("= ")[0]
            imgpath=response.text.split("= ")[1]
            print(resp1,imgpath)
            return render_template('profile.html', name = name, sessions=sessions, out=resp1,
                                  imgurl = imgpath)
        except:
            return render_template('profile.html',out= "No logs in this session")
        
    
    else:
        print("get") 
        return render_template('profile.html',name = name, sessions=sessions)

app = create_app() 
if __name__ == '__main__':
    app.debug = False
    app.run(port = 5000)
