from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired


# from src.pipeline.stage_07_prediction_pipeline import CustomData, PredictPipeline
from app.main.config.configuration import ConfigurationManager



config = ConfigurationManager()
webform_config = config.get_webform_config()



class WebForm(FlaskForm):
     
    
    
    email = StringField("Email Address (text)", validators=[DataRequired()], 
                                          render_kw={"placeholder": "Provide the email address that the prediction will be sent to"})
    age = IntegerField('Age in years',default=0 ,validators=[InputRequired()])
    sex = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    cp = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    trestbps = IntegerField("Resting blood pressure (in mm Hg on admission to the hospital)", default=0 ,validators=[InputRequired()])
    chol = IntegerField("Serum cholestoral in mg/dl", default=0 ,validators=[InputRequired()])
    fbs = SelectField('(Fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    restecg = SelectField('Resting electrocardiographic results', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    thalach = IntegerField('Maximum heart rate achieved', default=0 ,validators=[InputRequired()])
    exang = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    oldpeak = FloatField('ST depression induced by exercise relative to rest', default=0.00 ,validators=[InputRequired()])
    slope = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    ca = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
    thal = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)


    