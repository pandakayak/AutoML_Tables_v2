# AutoML_Tables
Another POC of GCP AutoML Tables

## Objective
The AutoML Tables in Google Cloud AI Platform is an intuitive and ease-to-use supervised learning service, to build and deploy state of the art machine learning model with structured (tabular) data.

The objective of this repo is to validate the capabilities of AutoML Tables for all business users.

We will use Chicago Taxi Trip dataset, to predict the Chicago taxi fare in AutoML Tables. We will focus on testing the following capabilities: easy-to-build models, easy-to-deploy and scale models, and flexible user options.

## Data pre-processing [Source: (https://www.kaggle.com/chicago/chicago-taxi-trips-bq)]

Reference code: 
* *data_prep.py* --- A Python Scripts, aim to perform data cleaning and feature selections. 
https://github.com/pandakayak/AutoML_Tables_v2/blob/master/data_prep.py

* *data_pre-processing.ipynb* --- A Jupyter Notebook, used to implement data_prep.py. 
https://github.com/pandakayak/AutoML_Tables_v2/blob/master/data_pre-processing.ipynb

### Raw Data

Ride data since after year 2016, were extracted from BigQuery using SQL.

### Data Exploratory

Notes of the Chicago Open Street Map: 
green: less frequent<br/>
yellow: more frequent than green, but less frequent than orange<br/>
orange: more frequent than yellow, but less frequent than red<br/>
red: most frequent => popular location<br/>

***Q1: Which regions have most pickups?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p1.PNG" width="800" height="400" /> 

==> Downtown and airport areas have the most pickups.

***Q2: Which regions have most dropoff?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p2.PNG" width="800" height="400" /> 

==> Downtown and airport areas have the most dropoffs.

***Q3: What region has more expensive pickup?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p3.PNG" width="800" height="400" /> 

==> Non-downtown and airport areas have the most pickups.

***Q4: What region has more expensive dropoff?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p4.PNG" width="800" height="400" /> 

==> Non-downtown and airport areas have the most dropoffs.

***Q5: When are the peak hours and off-peak hours for taking taxi?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p5.PNG" width="600" height="300" /> 

==> Daytime hours have the most pickups and dropoffs.

***Q6: What is the peak day and off-peak day in a month for taking taxi?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p6.PNG" width="600" height="300" /> 

==> No clear pattern found according to the visualization.

***Q7: When are the peak day and off-peak day in a week for rides? In terms of pickup***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p7.PNG" width="600" height="300" /> 

==> Friday is the peak day.

***Q8: When are the peak day and off-peak day in a year for price? In terms of pickup? Does holiday affect the taxi demands?***
Year 2016
![alt text](https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p8_16.PNG)
Year 2017
![alt text](https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p8_17.PNG)
Year 2018
![alt text](https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p8_18.PNG)
Year 2019
![alt text](https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p8_19.PNG)

==> The taxi demands in US holidays seem lower than normal days.

***Q9: When are the peak day and off-peak day in a year for price? In terms of pickup? Does holiday affect the taxi demands?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p9.PNG" width="500" height="360" /> 

***Q10: When are the peak day and off-peak day in a year for price? In terms of pickup? Does holiday affect the taxi demands?***

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p10_1.PNG" width="600" height="300" /> 
<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p10_2.PNG" width="600" height="300" /> 

==> Long-distance trips always occur in night time.

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p10_3.PNG" width="600" height="300" /> 
<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p10_4.PNG" width="600" height="300" />

==> No clear patter found.

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p10_5.PNG" width="600" height="300" /> 

==> There is trend of the avg trip miles, followed by the day order each year.

***Summary of data exploratory***
1. It confirms that location will affect the fare price, and the popular pickup/dropoff location always has lowest fare price, except airport.<br/>
2. Time-related feature do show patterns to fare price, and may contain outliers. <br/>

### Outlier detection (Apply Isolation Forest Algorithm)

**Isolation Forest Score Distribution**

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p11.PNG" width="600" height="300" /> 

**Before outliers detection**

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p12.PNG" width="300" height="300" /> 

**After outliers detection**

<img src="https://github.com/pandakayak/AutoML_Tables_v2/blob/master/image/p13.PNG" width="300" height="300" /> 

==> **Data Removing Criterion: remove the rows in the dataset which the outlier score is larger than 0.04 and smaller than 0.1.**

**After proper feature selection, finally got a training dataset(27,589 rows) and a test dataset(2421 rows) with 11 features(columns).**

### Training & Test Datasets
We used 10 features to predict the fare price per mile (in dollars). 

Predictor Features:

* start_hour: the hour the trip starts
* end_hour: the hour the trip ends
* pickup_latitude: pickup latitude
* pickup_longitude: pickup logtitude, associated with pickup latitude
* dropoff_latitude: dropoff latitude
* dropoff_longitude: dropoff longtitude, associated with dropoff latitude
* dayOfWeek: day of a week (Monday-Sunday: 1-7)
* trip_miles: the distance of each ride, calculated by mile
* trip_seconds: the duration of each ride, claculated by second
* dayOfYear: the day order in a year, from 1-365

#### Training Data (The ride data from year 2016 to the end of 2018)
The training dataset imported from Google BigQuery consists of 27,589 rows by 11 columns (10 predictors + 1 target).

#### Test Data (The 2019 ride data)

2421 rows by 11 columns. 
 
## The Model
The .ipynb file contains 7 sessions


1. Implement by data_prep.py and data_cleaning.ipynb <br/>
   --- *data_prep.py*: A Python scripts, included necessary define functions to clean the raw data; <br/>
   --- *data_cleaning.ipynb*: A Jupyter Notebook, used to execute data_prep.py to prepare train and test datasets.
### session 1: The data--gathering and preparing
1. extracted data from GCP BigQuery as 2 Pandas dataframe, named train and test
2. general data analysis lookup
3. ploted distribution graph to check if test dataset is consitent with train dataset in some features

### session 2: Importing training set to AutoML Tables
1. created a service account key in GCP console, saved the key in JSON file. Reference: https://cloud.google.com/iam/docs/creating-managing-service-account-keys
2. created an AutoML client with a GCP project id and compute engine region
3. created and imported train dataset to GCP AutoML Tables
```css
# create dataset in AutoML

dataset_display_name = 'demo3_chicago_taxi_fare' 
create_dataset_response = client.create_dataset(
    location_path,
    {'display_name': dataset_display_name, 'tables_dataset_metadata': {}})
dataset_name = create_dataset_response.name
create_dataset_response
```
```css
# get training data path

dataset_bq_input_uri = '$[bigquery dir here], removed by security reason'

# Define input configuration.
input_config = {
    'bigquery_source': {
        'input_uri': dataset_bq_input_uri
    }
}
```
```css
# Import training data table into AutoML dataset 

import_data_response = client.import_data(dataset_name, input_config)

# Wait until import is done.
import_data_result = import_data_response.result()
import_data_result
```
4. reviewed schema and change it if necessary, declare target and features
```css
# Schema review

import google.cloud.automl_v1beta1.proto.data_types_pb2 as data_types

# List table specs
list_table_specs_response = client.list_table_specs(dataset_name)
table_specs = [s for s in list_table_specs_response]

# List column specs
table_spec_name = table_specs[0].name
list_column_specs_response = client.list_column_specs(table_spec_name)
column_specs = {s.display_name: s for s in list_column_specs_response}
[(x, data_types.TypeCode.Name(
  column_specs[x].data_type.type_code)) for x in column_specs.keys()]
  ```
  ```css
  # Update dataset - split features and target

label_column_name = 'fare_dollars' 
label_column_spec = column_specs[label_column_name]
label_column_id = label_column_spec.name.rsplit('/', 1)[-1]
print('Label column ID: {}'.format(label_column_id))

# Define the values of the fields to be updated.
update_dataset_dict = {
    'name': dataset_name,
    'tables_dataset_metadata': {
        'target_column_spec_id': label_column_id
    }
}

update_dataset_response = client.update_dataset(update_dataset_dict)
update_dataset_response
  ```

### session 3:  Managing and training AutoML Tables model
created a model training in AutoML Tables, and set training budget no longer than 5 hours
```css
model_display_name = 'demo3_model' # give model a random name

# the time budge is 5 hours
model_dict = {
    'display_name': model_display_name,
    'dataset_id': dataset_name.rsplit('/', 1)[-1],
    'tables_model_metadata': {'train_budget_milli_node_hours': 5000}
}

create_model_response = client.create_model(location_path, model_dict)
print('Dataset import operation: {}'.format(create_model_response.operation))
```

### session 4: training performance
printed out general metrics of the AutoML Tables model, such as MSE, MAE, MAPE, R_sqaured, feature importance
```css
# general regression metric results

metrics= [x for x in client.list_model_evaluations(model_name)][-1]
metrics.regression_evaluation_metrics
```
```css
# raw feature importance

model = client.get_model(model_name)
feat_list = [(x.feature_importance, x.column_display_name) for x in model.tables_model_metadata.tables_model_column_info]
feat_list.sort(reverse=True)
feat_list[:15]
```

### session 5: making batch prediction
1. used the test set already uploaded to BigQuery
2. declared path to store predictions(either Cloud Storage or BigQuery)
```css # make prediction and store result in BigQuery 

input_path = '$[bigquery dir here], removed by security reason'
output_path = '$[bigquery dir here], removed by security reason'

from google.cloud import automl_v1beta1 as automl
import csv

automl_client = automl.AutoMlClient()

# Get the full path of the model.
model_full_id = automl_client.model_path(
    project_id, location, model_id
)

# Create client for prediction service.
prediction_client = automl.PredictionServiceClient()

if input_path.startswith('bq'):
    input_config = {"bigquery_source": {"input_uri": input_path}}
else:
    # Get the multiple Google Cloud Storage URIs.
    input_uris = input_path.split(",").strip()
    input_config = {"gcs_source": {"input_uris": input_uris}}

if output_path.startswith('bq'):
    output_config = {"bigquery_destination": {"output_uri": output_path}}
else:
    # Get the multiple Google Cloud Storage URIs.
    output_config = {"gcs_destination": {"output_uri_prefix": output_path}}

# Query model
response = prediction_client.batch_predict(
    model_full_id, input_config, output_config)

print("Making batch prediction... ")
try:
    result = response.result()
except:
    pass
print("Batch prediction complete.\n{}".format(response.metadata))
```

### session 6: evaluating predictions
1. the prediction result is store in nested table (need to unnest the result in Pandas)
this is the result originally in BigQuery: 
```css 
[{'tables': {'prediction_interval': {'end': 23.365476608276367,'start': 5.482821464538574},'value': 9.624988555908203}}]
```
the 'value' is the prediction that we are looking for

2. compared the prediction with the actual fare price, with the metrics such as MSE, MAE, MAPE, R_sqaured
3. plot the predictions and actual values in a graph to compare visually
![alt text](https://github.com/pandakayak/AutoML_Tables/blob/master/plot1.PNG)

### session 7: making online prediction
1. firstly, we need to deploy the model in GCP AutoML Tables, to enable online prediction
```css
! curl -X POST \
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
https://automl.googleapis.com/v1beta1/projects/hackathon1-183523/locations/us-central1/models/TBL4988132411498823680:deploy
```
2. created a sample to make prediction, in JSON file
3. enable online prediction with GCP command
```css 
! curl -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  https://automl.googleapis.com/v1beta1/projects/hackathon1-183523/locations/us-central1/models/TBL4988132411498823680:predict \
  -d @request.json
  ```
4. undelopyed the model
```css 
! curl -X POST \
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
https://automl.googleapis.com/v1beta1/projects/hackathon1-183523/locations/us-central1/models/TBL4988132411498823680:undeploy
```
## reference:
1. https://cloud.google.com/automl-tables/docs/
2. https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/tables/automl/notebooks
