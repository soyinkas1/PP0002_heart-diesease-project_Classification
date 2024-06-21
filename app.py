from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, InputRequired

import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv

from sklearn.preprocessing import StandardScaler
# from src.pipeline.stage_07_prediction_pipeline import CustomData, PredictPipeline
from app.main.config.configuration import ConfigurationManager
from app.main.config.config_entity import DataTransformationConfig

app = Flask(__name__)



config = ConfigurationManager()
predict_config = config.get_prediction_pipeline_config()
webform_config = config.get_webform_config()


class WebForm(FlaskForm):
    
    
    email = StringField("Email Address (text)", validators=[DataRequired()], 
                                          render_kw={"placeholder": "Provide the email address that the prediction will be sent to"})
    age = IntegerField('Age',default=0 ,validators=[InputRequired()])
    sex = SelectField('Sex', choices=list(zip(webform_config.category_list, 
                                                                  webform_config.category_list)), validate_choice=True)
    cp = IntegerField('Number of Years Since Last Funding', default=0 ,validators=[InputRequired()])
    trestbps = IntegerField("Promoter's Degree Length (Years)", default=0 ,validators=[InputRequired()])
    chol = IntegerField("Promoter's Years of Experience at Start of Company", default=0 ,validators=[InputRequired()])
    fbs = IntegerField('Number of Events as a sponsor', default=0 ,validators=[InputRequired()])
    restecg = IntegerField('Number of Events as a speaker', default=0 ,validators=[InputRequired()])
    thalach = IntegerField('Number of Events as an organizer', default=0 ,validators=[InputRequired()])
    exang = IntegerField('Number of Events as an exhibitor', default=0 ,validators=[InputRequired()])
    oldpeak = FloatField('Total Funding in USD', default=0.00 ,validators=[InputRequired()])
    slope = IntegerField('Company Employee Count', default=1 ,validators=[InputRequired()])
    ca = IntegerField('Company Employee Count', default=1 ,validators=[InputRequired()])
    thal = IntegerField('Company Employee Count', default=1 ,validators=[InputRequired()])


    
    status = SelectField('status', choices=[('acquired', 'acquired'), ('operating', 'operating'), ('ipo', 'ipo'), ('closed','closed')], 
                         validate_choice=True)
   
    category_groups_list = SelectField('Category Group', choices=list(zip(webform_config.category_groups_list, 
                                                                                webform_config.category_groups_list)), validate_choice=True)
    primary_role = SelectField('Company Primary Role', choices=[('company', 'company'), ('investor', 'investor'), ('school', 'school')], 
                               validate_choice=True)
    gender = SelectField('Promoter Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validate_choice=True)
    featured_job_title = SelectField('Job Title', choices=list(zip(webform_config.featured_job_title_list, 
                                                                            webform_config.featured_job_title_list)), validate_choice=True)
    institution_name = SelectField("Promoter's Institution Name", choices=list(zip(webform_config.institution_name_list, 
                                                                        webform_config.institution_name_list)), validate_choice=True)
    degree_type = SelectField("Promoter's Degree Type", choices=list(zip(webform_config.degree_type_list, 
                                                              webform_config.degree_type_list)), validate_choice=True)
    subject = SelectField("Promoter's Degree subject", choices=list(zip(webform_config.subject_list, 
                                                      webform_config.subject_list)), validate_choice=True)
    degree_is_completed = SelectField('Degree is completed?', choices=[('Yes'), ('No')], validate_choice=True)
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    form = WebForm()
    if form.validate_on_submit():
        # name = form.name.data
        # form.name.data = ''
        data = CustomData(
        yrs_of_operation = form.yrs_of_operation.data,
        yrs_since_last_funding = form.yrs_since_last_funding.data,
        degree_length = form.degree_length.data,
        per_exp_at_coy_start = form.per_exp_at_coy_start.data,
        sponsor = form.sponsor.data,
        speaker = form.speaker.data,
        organizer = form.organizer.data,
        exhibitor = form.exhibitor.data,
        employee_count = form.employee_count.data,
        total_funding_usd = form.total_funding_usd.data,
        organization_description = form.organization_description.data,
        people_description = form.people_description.data,
        status = form.status.data,
        category_list = form.category_list.data,
        category_groups_list = form.category_groups_list.data,
        primary_role = form.primary_role.data,
        gender = form.gender.data,
        featured_job_title = form.featured_job_title.data,
        institution_name = form.institution_name.data,
        degree_type = form.degree_type.data,
        subject = form.subject.data,
        degree_is_completed = form.degree_is_completed.data,
        
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        
     
        obj = PredictPipeline(config=predict_config)
        predict = obj.predict(pred_df)

        return render_template('results.html', predict=predict)
    
    else:

        return render_template('predictor.html', form=form)
    
@app.route('/train', methods=['GET'])
def training():
    
    os.system("python main.py")

    return render_template('training.html')

    