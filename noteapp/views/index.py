from flask import Blueprint, render_template

bp = Blueprint("noteapp", __name__, template_folder='templates')


@bp.route('/helloworld')
def helloWorld():
   return "Hello World"

@bp.route('/')
def renderHome():
    return render_template('layout.html')
