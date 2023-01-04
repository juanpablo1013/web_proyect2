from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

dataBase = SQLAlchemy()
dataBaseName = "database.db"




def create_app():
    '''
    Set the base app configuration to create the web page
    return: the app ready to start
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dataBaseName}' #storage
    dataBase = SQLAlchemy(app)
    dataBase.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    #import .models as models
    from .models import User, Note

    createDataBase(app)
    
    return app

def createDataBase(app):
    '''
    Check if the data base alredy exist with the path module and if it dosen't, it is going to create it. This to avoid override the data base.
    param app: this is the template app
    '''
    if not path.exists('web_proyect/' + dataBaseName):
        dataBase.create_all(app=app)
        print('Created Database')








