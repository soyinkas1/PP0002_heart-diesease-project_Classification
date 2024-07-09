# from flask import Flask, redirect, render_template, url_for
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField, SelectField
# from wtforms.validators import DataRequired, InputRequired

# import numpy as np
# import pandas as pd
# import os
# from dotenv import load_dotenv

# from sklearn.preprocessing import StandardScaler
# # from src.pipeline.stage_07_prediction_pipeline import CustomData, PredictPipeline
# from app.main.config.configuration import ConfigurationManager
# from app.main.config.config_entity import DataTransformationConfig

# app = Flask(__name__)



# config = ConfigurationManager()
# predict_config = config.get_prediction_pipeline_config()
# webform_config = config.get_webform_config()
# print(webform_config)

# class WebForm(FlaskForm):
    
    
#     email = StringField("Email Address (text)", validators=[DataRequired()], 
#                                           render_kw={"placeholder": "Provide the email address that the prediction will be sent to"})
#     age = IntegerField('Age in years',default=0 ,validators=[InputRequired()])
#     sex = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     cp = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     trestbps = IntegerField("Resting blood pressure (in mm Hg on admission to the hospital)", default=0 ,validators=[InputRequired()])
#     chol = IntegerField("Serum cholestoral in mg/dl", default=0 ,validators=[InputRequired()])
#     fbs = SelectField('(Fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     restecg = SelectField('Resting electrocardiographic results', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     thalach = IntegerField('Maximum heart rate achieved', default=0 ,validators=[InputRequired()])
#     exang = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     oldpeak = FloatField('ST depression induced by exercise relative to rest', default=0.00 ,validators=[InputRequired()])
#     slope = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     ca = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)
#     thal = SelectField('Sex (1 = male; 0 = female)', choices=[('1', 'male'), ('0', 'female')], validate_choice=True)



# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predictdata', methods=['GET', 'POST'])
# def predict_datapoint():
#     form = WebForm()
#     if form.validate_on_submit():
#         # name = form.name.data
#         # form.name.data = ''
#         data = CustomData(
#         yrs_of_operation = form.yrs_of_operation.data,
#         yrs_since_last_funding = form.yrs_since_last_funding.data,
#         degree_length = form.degree_length.data,
#         per_exp_at_coy_start = form.per_exp_at_coy_start.data,
#         sponsor = form.sponsor.data,
#         speaker = form.speaker.data,
#         organizer = form.organizer.data,
#         exhibitor = form.exhibitor.data,
#         employee_count = form.employee_count.data,
#         total_funding_usd = form.total_funding_usd.data,
#         organization_description = form.organization_description.data,
#         people_description = form.people_description.data,
#         status = form.status.data,
#         category_list = form.category_list.data,
#         category_groups_list = form.category_groups_list.data,
#         primary_role = form.primary_role.data,
#         gender = form.gender.data,
#         featured_job_title = form.featured_job_title.data,
#         institution_name = form.institution_name.data,
#         degree_type = form.degree_type.data,
#         subject = form.subject.data,
#         degree_is_completed = form.degree_is_completed.data,
        
#         )
#         pred_df=data.get_data_as_data_frame()
#         print(pred_df)

        
     
#         obj = PredictPipeline(config=predict_config)
#         predict = obj.predict(pred_df)

#         return render_template('results.html', predict=predict)
    
#     else:

#         return render_template('predictor.html', form=form)
    
# @app.route('/train', methods=['GET'])
# def training():
    
#     os.system("python main.py")

#     return render_template('training.html')

    