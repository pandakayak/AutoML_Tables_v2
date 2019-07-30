#!/bin/bash

export PROJECT_ID="hackathon1-183523"
export REGION_NAME="us-central1"

python dataset.py create_dataset --dataset_name train > /tmp/create_dataset_output

dataset_id="$(cat /tmp/create_dataset_output | grep -oP '(?<=Dataset id: ).*')"

dataset_name="$(cat /tmp/create_dataset_output | grep -oP '(?<=Dataset name: ).*')"

echo $dataset_id

python dataset.py import_data --dataset_id $dataset_id --path "bq://hackathon1-183523.demo3_v2.train"

python dataset.py schema_review --dataset_name "$dataset_name" 

python dataset.py list_datasets

python dataset.py list_table_specs --dataset_id $dataset_id > /tmp/list_table_specs_output

table_spec_id="$(cat /tmp/list_table_specs_output | grep -oP '(?<=Table spec id: ).*')" 

echo $table_spec_id

python dataset.py list_column_specs --dataset_id $dataset_id --table_spec_id $table_spec_id > /tmp/list_column_specs_output

python dataset.py get_dataset --dataset_id $dataset_id 

python dataset.py get_table_spec --dataset_id $dataset_id --table_spec_id $table_spec_id

target_col_spec_id="$(cat /tmp/list_column_specs_output | grep -oP '(?<=target_column_spec_id: ).*')"

echo $target_col_spec_id

python dataset.py update_dataset --dataset_id $dataset_id --target_column_spec_id $target_col_spec_id

python model.py list_models

python model.py create_model --dataset_id $dataset_id --model_name test_demo --train_budget_milli_node_hours 5000 > /tmp/create_model_output

operation_full_id="$(cat /tmp/create_model_output | grep -oP '(?<=Training operation name: ).*')"

echo $operation_full_id

python model.py get_operation_status --operation_full_id "$operation_full_id"

python model.py list_models > /tmp/list_model_output

model_id="$(cat /tmp/list_model_output | grep -oP '(?<=Model id: ).*')"

echo $model_id

python model.py get_model --model_id $model_id

python model.py list_model_evaluations --model_id $model_id > /tmp/list_model_evaluation_output

model_evaluation_id="$(cat /tmp/list_model_evaluation_output | grep -oP '(?<=Model evaluation id: ).*')"

echo $model_evaluation_id

python model.py get_model_evaluation --model_id $model_id --model_evaluation_id $model_evaluation_id

python model.py display_evaluation --model_id $model_id

python model.py deploy_model --model_id $model_id

python predict.py batch_predict --model_id $model_id --input_path "bq://hackathon1-183523.demo3_v2.test" --output_path "bq://hackathon1-183523"

python predict.py predict --model_id $model_id --file_path 'test.csv'

curl -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  https://automl.googleapis.com/v1beta1/projects/hackathon1-183523/locations/us-central1/models/$model_id:predict \
  -d @request.json