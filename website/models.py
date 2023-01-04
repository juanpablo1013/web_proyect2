from . import dataBase #import from the web package (note for me)
from flask_login import UserMixin #Module to help user get in
from sqlalchemy.sql import func #to get the time at the moment of saving
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Note(dataBase.Model):
    id = dataBase.Column(dataBase.Integer, primary_key = True)
    dataNote = dataBase.Column(dataBase.String(5000))
    date = dataBase.Column(dataBase.DateTime(timezone = True), default= func.now())#add the exact date time
    #dataBase = SQLAlchemy()
    user_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('user.id'))

class User(dataBase.Model, UserMixin):
    id = dataBase.Column(dataBase.Integer, primary_key = True)#unique identifier for each user
    email = dataBase.Column(dataBase.String(40), unique = True)
    password  = dataBase.Column(dataBase.String(15))
    first_name  = dataBase.Column(dataBase.String(10))
    dataBase = SQLAlchemy()
    notes = dataBase.relationship('Note')

