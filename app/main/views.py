from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..db_models import Predictions

@main.route('/', methods=['GET', 'POST'])
def index():
    form =NameForm()
    if form.validate_on_submit():

        return redirect(url_for('.index'))
    
    
    return render_template('index.html',
                           form=form)