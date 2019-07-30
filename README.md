# AutoML_Tables
Another POC of GCP AutoML Tables

## Objective
The AutoML Tables in Google Cloud AI Platform is an intuitive and ease-to-use supervised learning service, to build and deploy state of the art machine learning model with structured (tabular) data.

The objective of this repo is to validate the capabilities of AutoML Tables for all business users.

We will use Chicago Taxi Trip dataset, to predict the Chicago taxi fare in AutoML Tables. We will focus on testing the following capabilities: easy-to-build models, easy-to-deploy and scale models, and flexible user options.

## Data pre-processing 
Source: (https://www.kaggle.com/chicago/chicago-taxi-trips-bq)

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

## The Dataset

reference code: <br/>
*dataset.py* --- A Python Scripts, aim to import training dataset to AutoML Tables.

### Create an empty AutoML Dataset
```bash
# create a dataset named 'train'
python dataset.py create_dataset --dataset_name train > /tmp/create_dataset_output

# save info for further execution
dataset_id="$(cat /tmp/create_dataset_output | grep -oP '(?<=Dataset id: ).*')"
dataset_name="$(cat /tmp/create_dataset_output | grep -oP '(?<=Dataset name: ).*')"

# check if 'data_id' is saved successfully 
echo $dataset_id
```
### List exisiting dataset in AutoML Tables
```bash
python dataset.py list_datasets
```
### Import training dataset
```bash
python dataset.py import_data --dataset_id $dataset_id --path "[Enter your GCP Bucket or BigQuery path here]"
```
### Schema Review
```bash
python dataset.py schema_review --dataset_name "$dataset_name" 
```
### List table spec info
```css
python dataset.py list_table_specs --dataset_id $dataset_id > /tmp/list_table_specs_output

# save 'table_Spec_id' for further execution
table_spec_id="$(cat /tmp/list_table_specs_output | grep -oP '(?<=Table spec id: ).*')" 
echo $table_spec_id
```
### List column spec info
```bash
python dataset.py list_column_specs --dataset_id $dataset_id --table_spec_id $table_spec_id > /tmp/list_column_specs_output

# save 'target_col_spec_id'
target_col_spec_id="$(cat /tmp/list_column_specs_output | grep -oP '(?<=target_column_spec_id: ).*')"
echo $target_col_spec_id
```
### Get dataset
```bash
python dataset.py get_dataset --dataset_id $dataset_id 
```
### Get table spec info
```bash
python dataset.py get_table_spec --dataset_id $dataset_id --table_spec_id $table_spec_id
```
### Update dataset
```bash
python dataset.py update_dataset --dataset_id $dataset_id --target_column_spec_id $target_col_spec_id
```
### list model
```bash
python model.py list_models
```
### Train model
```bash
python model.py create_model --dataset_id $dataset_id --model_name [Enter your model name here] --train_budget_milli_node_hours [Enter node hours here] > /tmp/create_model_output

operation_full_id="$(cat /tmp/create_model_output | grep -oP '(?<=Training operation name: ).*')"
echo $operation_full_id
```
### Get operation status
```bash
python model.py get_operation_status --operation_full_id "$operation_full_id"
```
### Get Model id
```bash
python model.py list_models > /tmp/list_model_output

# save the most recent model id
model_id="$(cat /tmp/list_model_output | grep -oP '(?<=Model id: ).*')"
echo $model_id
```
### Get model
```bash
python model.py get_model --model_id $model_id
```
### List model evaluation id
```bash
python model.py list_model_evaluations --model_id $model_id > /tmp/list_model_evaluation_output

# save the most recent model evaluation id
model_evaluation_id="$(cat /tmp/list_model_evaluation_output | grep -oP '(?<=Model evaluation id: ).*')"
echo $model_evaluation_id
```
### Display model evaluation
```bash
python model.py get_model_evaluation --model_id $model_id --model_evaluation_id $model_evaluation_id

python model.py display_evaluation --model_id $model_id
```
### Deploy model
```bash
python model.py deploy_model --model_id $model_id
```
### Batch prediction
```bash
python predict.py batch_predict --model_id $model_id --input_path [Enter the path store the test dataset] --output_path [Declare an output path in GCP Bucket or BigQuery]
```
### Online prediction
```bash
python predict.py predict --model_id $model_id --file_path [Enter the path store the test dataset]
```

 

## reference:
1. https://cloud.google.com/automl-tables/docs/
2. https://github.com/GoogleCloudPlatform/python-docs-samples/tree/tables/tables/automl
