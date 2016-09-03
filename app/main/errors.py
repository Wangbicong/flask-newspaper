from flask import render_template
from . import main_blueprint


@main_blueprint.errorhandler(404)
def error_404():
    return render_template('404.html', 404)