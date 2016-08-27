from flask import render_template, redirect, session, url_for, flash, current_app
from . import main_blueprint
from .forms import NameForm


@main_blueprint.route('/', methods=['get', 'post'])
def index():

    return render_template('main.html')
