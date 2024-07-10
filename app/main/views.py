from flask import render_template, session, redirect, url_for
from . import main
from .forms import WebForm
from .. import db
from ..db_models import HeartPredictions
from app.main.pipeline.prediction_pipeline import CustomData, PredictPipeline
from app.main.config.configuration import ConfigurationManager


config = ConfigurationManager()
predict_config = config.get_prediction_pipeline_config()

@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

      

@main.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    form = WebForm()
    if form.validate_on_submit():
         
        data = CustomData(
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
            thal=form.thal.age
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

                
            
        obj = PredictPipeline(config=predict_config)
        predict = obj.predict(pred_df)

        return render_template('results.html', predict=predict)

    else:

        return render_template('prediction.html', form=form)