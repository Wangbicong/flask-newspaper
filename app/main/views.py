from flask import render_template, redirect, session, url_for, flash, current_app
from . import main_blueprint
from .forms import NameForm
from ..mails import send_email


@main_blueprint.route('/', methods=['get', 'post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name and old_name != form.name.data:
            flash('You changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                   'mail/new_user', username=session.get('name'))
        return redirect(url_for('main.index'))
    return render_template('main.html', form=form, name=session.get('name'))
