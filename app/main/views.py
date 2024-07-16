from flask import render_template, session, redirect, url_for
from . import main
from .forms import WebForm
from .. import db
from ..db_models import HeartPredictions
from app.main.pipeline.stage_05_prediction_pipeline import CustomData, PredictPipeline
from app.main.config.configuration import ConfigurationManager
from .. import email


config = ConfigurationManager()
predict_config = config.get_prediction_pipeline_config()

@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

      

@main.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    form = WebForm()
    if form.validate_on_submit():
        # Collect data imput from webform      
        data = CustomData(
            email=form.email.data,
            age=form.age.data,
            sex=form.sex.data,
            cp=form.cp.data,
            trestbps=form.trestbps.data,
            chol=form.chol.data,
            fbs=form.fbs.data,
            restecg=form.restecg.data,
            thalach=form.thalach.data,
            exang=form.exang.data,
            oldpeak=form.oldpeak.data,
            slope=form.slope.data,
            ca=form.ca.data,
            thal=form.thal.data,
            target=1
        )

        # Create DataFrame for prediction 
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
   
        # Make prediction using data supplied 
        obj = PredictPipeline(config=predict_config)
        predict = obj.predict(pred_df)

        # Update the results to database
        database_df = data.get_data_for_database()
        database_df['target'] = predict
        data.add_to_database(database_df)

        # Email results 
        email.send_email(database_df['email'].iloc[0], 'results',
'mail/results', predict=predict)

        return render_template('results.html', predict=predict)

    else:

        return render_template('prediction.html', form=form)