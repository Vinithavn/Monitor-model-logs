# Importing packages 
from flask import Flask
from flask_login import LoginManager
import json

def create_app():
    f = open('./utils/accounts.json')
    dataDict = json.load(f)
    f.close()

    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'secret-key-goes-here' 
    
    login_manager = LoginManager() # Create a Login Manager instance
    login_manager.login_view = 'auth.login' # define the redirection path when login required and we attempt to access without being logged in
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return [i['id'] for i in dataDict["data"] if user_id == i['id']]
    
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
    