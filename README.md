# PP0002_Heart-Diesease-Project
This project is a binary classification project which predicts if a person has a heart disease based on health data provided. 

    
**Problem Statement:** 
The In a statement,
> Given clinical parameters about a patient, can we predict whether or not they have heart disease?


## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Technology Stack](#tech-stack)
4. [Data Preparation](#data-preparation)
5. [Model Training](#model-training)
6. [Model Evaluation](#evaluating-multiple-models)
7. [Deployment](#deployment)
    - [Flask Web App](#Flask-web-app)
    - [Azure Deployment](#azure-deployment)
    - [AWS Elastic Beanstalk Deployment](#aws-elastic-beanstalk-deployment)
9.  [Update Workflows](#update-workflows)
10. [Usage](#usage)
11. [Contributing](#contributing)
12. [License](#license)
13. [Acknowledgments](#acknowledgments)
14. [Future Planned Updates](#future-work/advancements)


## Project Overview
The first version of the notebook is the work along file from the ZTM ML Data Science bootcamp. 

The current version of the project extends the work done in the bootcamp by carrying out the following additional steps and capabilities such as:

* Experiment with additional classification models and hyperparameters
* Convert project structure to modular programming using OOP
* Deploy as a Flask Web App
* Classification results sent to email
* Prediction data and results saved to a database
* Deploy the web application to the Cloud.

**Current Objectives**
* Enhance the approach used in the initial project from ZTM ML bootcamp
* Improve on the experiments carried out
* Implement as a modular programmed application using best practices such as Object-Oriented Programming etc.
* Deploying the application to both Azure and AWS. The goal is to create a robust, scalable solution that can be accessed and used via web services on both cloud platforms.
* Ultimately deploy the app in a custom domain 
  
## Project Structure
```
├── app
│   ├── data
│   │   ├── heart-diesease.csv
│   ├── main
│   │   ├── components
│   │   │   ├── __initi__.py
│   │   │   ├── data_cleaning.py
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_transformation.py
│   │   │   ├── model_training.py
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   ├── config_entity.py
│   │   │   ├── config.yaml
│   │   │   ├── configuration.py
│   │   │   ├── params.yaml
│   │   ├── constants
│   │   │   ├── __init__.py
│   │   ├── pipeline
│   │   │   ├── __init__.py
│   │   │   ├── stage_01_data_ingestion.py
│   │   │   ├── stage_02_data_cleaning.py
│   │   │   ├── stage_03_data_transformation.py
│   │   │   ├── stage_04_model_training.py
│   │   │   ├── stage_05_prediction_pipeline.py
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── exception.py
│   │   ├── forms.py
│   │   ├── logging.py
│   │   ├── views.py
│   ├── notebooks
│   │   ├── Heart Disease Classification Project_Research.ipynb
│   ├── static
│   │   ├──bootstrap.min.css
│   │   ├──fontawesome.min.css
│   │   ├──style copy.css
│   │   ├──style.css    
│   ├── templates
│   │   ├──mail
│   │   │   ├──iresults.html
│   │   ├──404.html
│   │   ├──500.html
│   │   ├──base.html
│   │   ├──index.html
│   │   ├──prediction.html
│   │   ├──results.html
│   ├──utils
│   │   ├── __init__.py
│   │   ├── common.py
│   ├── __init__.py
│   ├── db_models.py 
│   ├── email.py 
├── artifacts
│   ├── data_cleaning 
│   │   ├── clean_heart-disease.csv    
│   ├── data_ingestion
│   │   ├── loaded_heart-disease.csv  
│   ├── data_transformation
│   │   ├── X_test.csv
│   │   ├── X_train.csv
│   │   ├── y_test.csv
│   │   ├── y_train.csv
│   ├── best_model.pkl
│   ├── preprocessor.pkl
├── logs
├── migrations
├── tests
├── venv
├── __init__.py
├── .env
├── .gitignore
├── config.py
├── heart.py
├──  README.md
├── requirements.txt
├── setup.py

```
## Tech Stack
### Dependencies
```
- python 3.12
- pandas
- numpy
- scikit-learn
- plotly
- matplotlib
- seaborn
- lightgbm
- xgboost
- dill
- flask
- flask-wtf
- flask-bootstrap
- flask-mail
- flask-moment
- flask_sqlalchemy
- psycopg2
- flask_fontawesome
- Flask-Migrate
- ensure
- python-box
- pyYAML
- python-dotenv
- jupyter
- email_validator
- Github (action)
- Azure Web App
- AWS Elastic Beanstalk

```
### Step-by-Step Implementation
 **Install the required packages:**
    ```
    pip install -r requirements.txt
    ```

## Data Preparation
### Data Sources
- The original data if from the Cleveland data from the UCI machine Learning Repository. https://archive.ics.uci.edu/ml/datasets/heart+disease

- There is also a version on Kaggle. https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset 

### Data Cleaning, Preprocessing and Transformation
The following steps were carried out of this dataset to clean and transform it for use:
- Missing Values:
    * There is no missing values in the dataset
- There was no requirement for transformation as well as there dataset were already encoded for its categorical features
    
      
## Final Data Dictionary 

<table border="1">
        <thead>
            <tr>
                <th>S/N</th>
                <th>Feature</th>
                <th>Description</th>
                <th>Data Class</th>
                <th>Data Type</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Age</td>
                <td>The Age of patient in years</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
            
                <td>2</td>
                <td>yrs_since_last_funding</td>
                <td>The number of years since the company received any external funding.</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
                <td>3</td>
                <td>degree_length</td>
                <td>Number of years between the start and completion date of a degree programme by the promoter</td>
                <td>interval</td>
                <td>int</td>
            </tr>
            <tr>
                <td>4</td>
                <td>per_exp_at_coy_start</td>
                <td>The number of years between the year the promoter graduated and when the organisation was founded.</td>
                <td>interval</td>
                <td>int</td>
            </tr>
            <tr>
                <td>5</td>
                <td>sponsor</td>
                <td>The number of events the organization or promoter participated in as a sponsor.</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
                <td>6</td>
                <td>speaker</td>
                <td>The number of events the organization or promoter participated in as a speaker.</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
                <td>7</td>
                <td>organizer</td>
                <td>The number of events the organization or promoter participated in as an organizer</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
                <td>8</td>
                <td>oexhibitor</td>
                <td>The number of events the organization or promoter participated in as an exhibitor</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
                <td>9</td>
                <td>employee_count</td>
                <td>count of employees of the organization.</td>
                <td>numeric</td>
                <td>int</td>
            </tr>
            <tr>
                <td>10</td>
                <td>total_funding_usd</td>
                <td>The total amount of external funding received by the company</td>
                <td>numeric</td>
                <td>float</td>
            </tr>
            <tr>
                <td>11</td>
                <td>organization_description</td>
                <td>full description about the company</td>
                <td>text</td>
                <td>string</td>
            </tr>
            <tr>
                <td>12</td>
                <td>people_description</td>
                <td>full description about the promoter</td>
                <td>text</td>
                <td>string</td>
            </tr>
            <tr>
                <td>13</td>
                <td>status</td>
                <td>status or state of the organization</td>
                <td>categorical</td>
                <td>string</td>
            </tr>
            <tr>
                <td>14</td>
                <td>category_list</td>
                <td>main category type of the organisationr</td>
                <td>categorical</td>
                <td>string</td>
            </tr>
            <tr>
                <td>15</td>
                <td>category_groups_list</td>
                <td>grouped category type of the organization</td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
            <tr>
                <td>16</td>
                <td>primary_role</td>
                <td>Roles as either company, investor or school </td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
            <tr>
                <td>17</td>
                <td>gender</td>
                <td>gender identifier for the promoter</td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
            <tr>
                <td>18</td>
                <td>featured_job_title</td>
                <td>job title for the promoter</td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
            <tr>
                <td>19</td>
                <td>institution_name</td>
                <td>educational institute attended by the promoter</td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
             <tr>
                <td>20</td>
                <td>degree_type</td>
                <td>degree awarded to the promoter</td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
             <tr>
                <td>21</td>
                <td>subject</td>
                <td>specialty of the degree awarded to the promoter</td>
                <<td>categorical</td>
                <td>string</td>
            </tr>
             <tr>
                <td>22</td>
                <td>degree_is_completed</td>
                <td>confirmation that the degree programme is completed by the promoter</td>
                <<td>boolean</td>
                <td>string</td>
            </tr>
             <tr>
                <td>23</td>
                <td>success</td>
                <td>(1) for successful company and (0) for unsuccessful company</td>
                <<td>label</td>
                <td>int</td>
            </tr>           
        </tbody>
    </table>
				

## Model Training
### Model Selection
The following models were selected after using recommendations from researching classification models and subsequent experimenting:

- Logistic regression
- Support Vector Machine Classifier (SVC)
- Random Forest Classifier
- XGBoost
- LightGBM

### Training the Model
- Loading the Configuration
First, load the  model training configuration. This configuration includes settings like paths to the training, validation, and test data, as well as the machine learning models and their parameters.
- Loading the Data
Next, load the datasets:
    * Training Data: Used to train the models.
    * Validation Data: Used to tune and validate the models during the training process.
    * Test Data: Used to evaluate the final model's performance.
- Splitting the Data
Split each dataset into:
    * Input Features (X): The data that our model will learn from (e.g., company details, financials).
    * Target Labels (y): The actual outcomes we want to predict (e.g., whether a startup succeeds or fails).

### Evaluating Multiple Models
Evaluated several machine learning models to see which one performs the best. 

Each model is tested using the training and validation data. Used a helper function based on ‘GridSearchCV’ called evaluate_models to check how well each model performs and store the results. 
- Selecting the Best Model
Looked at the performance scores of all the models and choose the one with the highest score. If no model achieves a score of at least 0.6 (out of 1.0), the application raises an error indicating that no suitable model was found.
- Saving the Best Model
Once the best model is identified, it is saved to a file to be used later to make predictions.

## Deployment
### Flask Web App
- The Flask web framework was used to share the web application for use. A simple web app with a form to collect data points and return the prediction was developed. 
### Azure Deployment
Deployment to Azure App Service was done using Github action for CI/CD

Use the link below to access the web app:

### AWS Elastic Beanstalk Deployment
Deploy to AWS Elastic Beanstalk:

## Update Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py

## Usage
### Accessing the Deployed Model
- Upon launching the application, the default page is the about page.
- Use the predictor tab to access the prediction page and provide values for all the data endpoints for the company using the input boxes, dropdowns etc.
- Click the submit button for a prediction of the success of the company
  
## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License 

## Acknowledgments
The project code, structure, best practices etc. were inspired and learnt from a myriad of open sources such as :
- Coursework from the M.Sc programme at Cardiff Metropolitan University
- Youtube videos of Kris Naik such as
- Books and literature such as
- YouTube and many other resources such as
- Udemy training such as
- Github repositories and resources such as
And many Medium.com articles.

## Future Work/Advancements

1. Create a viable workaround for the Twitter scrapper to scrape 2000000+ profiles
2. Add a Facebook scrapping module 
3. Update the data source to be a database such as MongoDB
4. Connect to updated data feed from Crunchbase to continually train the model as part of the pipeline

