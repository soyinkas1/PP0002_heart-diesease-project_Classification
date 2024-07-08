from flask import render_template, session, redirect, url_for
from . import main
from .forms import WebForm
from .. import db
from ..db_models import HeartPredictions

@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

      

@main.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    form = WebForm()
    if form.validate_on_submit():
         
        data = CustomData(
        return redirect(url_for('.index'))
    
    
    return render_template('index.html',
                           form=form)