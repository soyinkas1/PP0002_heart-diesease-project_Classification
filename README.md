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
  
## Project Structure
```
├── artifacts
│   ├── data_cleaning 
│   ├── data_ingestion
│   ├── data_transformation
│   ├── best_model
├── config
│   ├── config.yaml
│   ├── params.yaml
├── data
│   ├── acquisitions.csv
│   ├── category_groups.csv
│   ├── checksum.csv
│   ├── degrees.csv
│   ├── event_appearances.csv
│   ├── events.csv
│   ├── funding_rounds.csv
│   ├── funds.csv
│   ├── investment_partners.csv
│   ├── investments.csv
│   ├── ipos.csv
│   ├── jobs.csv
│   ├── org_parents.csv
│   ├── organizations_description.csv
│   ├── organizations.csv
│   ├── people_descriptions.csv
│   ├── people.csv
├── logs
├── notebooks
│   ├── 01_EDA_Data Cleaning_v2.ipynb
│   ├── 02_EDA_Transformation.ipynb
│   ├── 03_Model_Training.ipynb
│   ├── Experiments.ipynb
├── src
│   ├── components
│   │   ├── __initi__.py
│   │   ├── data_cleaning.py
│   │   ├── data_enrinchment.py
│   │   ├── data_ingestion.py
│   │   ├── data_scraping.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── config 
│   │   ├── __init__.py
│   │   ├── configuration.py
│   ├── constants
│   │   ├── __init__.py
│   ├── entity
│   │   ├── __init__.py
│   │   ├── config_entity.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_data_cleaning.py
│   │   ├── stage_03_data_scrapping.py
│   │   ├── stage_04_data_enrichment.py
│   │   ├── stage_05_data_transformation.py
│   │   ├── stage_06_model_trainer.py
│   │   ├── stage_07_prediction_pipeline.py
│   ├──utils
│   │   ├── __init__.py
│   │   ├── common.py
│   ├── __init__.py
│   ├── chromedriver.exe
│   ├── exception.py
│   ├── logger.py
├── static
│   ├──style.css
├── templates
│   ├──base.html
│   ├──index.html
│   ├──predictor.html
│   ├──results.html
│   ├──training.html
├── venv
├── .env
├── .gitignore
├── app.py
├── main.py
├──  README.md
├── requirements.txt
├── setup.py

```
## Tech Stack
### Dependencies
```
- python 3.8+
- pandas
- numpy
- scikit-learn 
- plotly
- textBlob
- selenium
- matplotlib
- seaborn
- lightgbm
- xgboost
- dill
- flask
- flask-wtf
- flask-bootstrap
- ensure
- python-box
- pyYAML
- python-dotenv
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
- Secondary historical information on startup companies was sourced from Crunchbase, a rich database containing details on founders, employee profiles, industry specifics, and funds raised, resulting in a dataset of 2,589,999 company entries.
- To enrich this data, social media information was integrated using a Twitter bot developed with the Python Selenium library, which scraped follower counts, accounts followed, and recent tweets, along with engagement metrics. Sentiment analysis of tweet comments was performed, with polarity and subjectivity scores added as features for a machine learning model.
- However, current restrictions on X (formerly Twitter) requiring sign-ins for each scrape have rendered this approach impractical for over 1,000,000 profiles, leading to the commenting out of the scraping and sentiment analysis pipeline.
- The raw data is provided in .csv file format and available in the ‘data’ folder. There are 17 CSV files which were sourced from the Crunchbase database. 

### Data Cleaning, Preprocessing and Transformation
The following steps were carried out of this dataset to clean and transform it for use:
- Missing Values:
    * Numerical values were filled with zero. 
    * String (addresses and other objects) values were filled with ‘not known’ or ‘False’ as applicable
    * Missing dates were either filled with estimates (e.g finish date = 4 years from start date) or with current date so derived dates will be zero 
- Table Merging:
    * The tables were merged using the organization table as the bedrock or backbone dataset. 
- Data type Correction:
    * Correct data types were cast for integers, floats and dates.
- Drop duplicates
- Feature Creation:
    * ***exp_at_coy_start*** – The number of years of experience of the promoter at the start of the company. This is calculated from the difference in the `completed_on` column from 'degrees' table and the ‘founded_on’ column from the `organizations` table. Negative values represent situations when the degree was completed after the company started and were imputed with zero.
    * ***degree_length*** - This is the course period of the degree programme. It was assumed as 4 years to impute missing values in the `completed_on` rows which had a date value in the `started_on` column. This is calculated as the difference in the `started_on` and `completed_on` columns of the `degree` table.
    * ***years_since_last_fundings*** - This is the number of years since the company last received external funding. This is calculated as the difference in the current date and `last_funding_on` column.
    * ***yrs_of_operation*** - This is the number of years the company has been operating. This is calculated as the difference in `closed_on` and `founded_on` columns.
    * ***sponsor*** – This is the number of events the organization or promoter participated in as a sponsor. It was created from the `events` and `events_description` tables.
    * ***speaker***, – This is the number of events the organization or promoter participated in as a speaker. It was created from the `events` and `events_description` tables.
    * ***exhibitor*** – This is the number of events the organization or promoter participated in as an exhibitor. It was created from the `events` and `events_description` tables.
    * ***organizer*** – This is the number of events the organization or promoter participated in as an organizer. It was created from the `events` and `events_description` tables.
    * ***Success*** – This is created based on several criteria to classify a company as successful or not successful. E.g. companies employees above 20 are successful, type of funding (IPO) etc.
- Drop unneeded columns:
    * Some columns were dropped outrightly as they do not add value to the analysis while others dropped after utilising them to derive more valuable features.
- Renaming and Rearrange of columns:
    * Some columns were renamed to create consistency and remove ambiguity 
    * Columns were then rearranged to keep numerical, categorical and text features together.
- Column transformation:
    * Column transformation of the numerical, categorical and text features were transformed using StandardScaler, OneHotEncoding and TFiDVectorization
    * The column transformed is saved after fitting with the training data  `processor.pkl`  for transforming prediction data.
      
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
                <td>yrs_of_operation</td>
                <td>The number of years the company has been in operations</td>
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

