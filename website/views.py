from flask import Blueprint, render_template


views = Blueprint("views1",__name__)

@views.route('/')
def home():
    '''
    render the template for the page home
    return: the page home with his html structure
    '''
    return render_template("home.html")