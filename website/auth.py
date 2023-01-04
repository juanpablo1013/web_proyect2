from xmlrpc.client import boolean
from flask import Blueprint, render_template, request, flash
from .models import User

auth = Blueprint("views",__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    render the template for the page login
    return: the page loging with his html structure
    '''
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    '''
    render the template for the page of logout
    return: the page logout with his html structure
    '''
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    '''
    render the template for the page sign_up and define specific conditions to create a new user
    return: the page sign_up with his html structure
    '''
    if request.method == 'POST':
    
        email = request.form.get('email')
        firstName = request.form.get('firtName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #Conditions to validate sign up
        if len(email) < 2:
            flash('Email must be greater than 2 characters', category='error')
            pass
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters', category='error')
            pass
        elif password1 != password2:
            flash('There is no coincidence between the passwords', category='error')
            pass
        elif len(password1) < 7:
            flash('The security of your password is low, passwords must have more than 7 characters', category='error')
            pass
        else:
            #new_user = User(email=email,firstName = firstName, password1 = password)
            flash('Your account have been created, Thanks for trust in us! ', category='success')
            # add user to database

    return render_template("sign_up.html")