from flask import render_template, redirect, session, url_for, flash
from . import main_blueprint
from forms import NameForm


@main_blueprint.route('/', methods=['get', 'post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash('You changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('main.html', form=form, name=session.get('name'))
