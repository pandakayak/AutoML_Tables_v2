# This script is a demo to perform basic operations on GCP AutoML Tables model training. #
# Reference: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/tables/tables/automl/automl_tables_predict.py #

import argparse
import os


def predict(project_id, compute_region, model_id, file_path):
    """
    Make a prediction.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    # file_path: path of the data which will make prediction
    """

    from google.cloud import automl_v1beta1 as automl
    import pandas as pd
    import json

    automl_client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = automl_client.model_path(
        project_id, compute_region, model_id
    )

    # Create client for prediction service.
    prediction_client = automl.PredictionServiceClient()
    params = {}
    
    #prepare the payload, each row is one payload
    df = pd.read_csv(file_path)
    df = df.drop('price_per_mile', axis=1)
    df = df.values
    
    for i in range(len(df)):
        values = df[i].tolist()
        payload = {
            "row": {
              "values": values
            }
        }
        
        data = {}
        data['payload'] = payload
        
        print(data)
        
        with open('request.json', 'w') as outfile:  
            json.dump(data, outfile)
                
        # Query model
        import subprocess

        bashCommand = "curl -X POST -H 'Content-Type: application/json' \
        -H \"Authorization: Bearer $(gcloud auth application-default print-access-token)\" \
        https://automl.googleapis.com/v1beta1/projects/hackathon1-183523/locations/us-central1/models/TBL2266814744474157056:predict \
        -d @request.json"
        output = subprocess.call(bashCommand, shell=True)
        print(output)



def batch_predict(project_id, compute_region, model_id, input_path, output_path):
    """
    Make a batch of predictions.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    # input_path: path of the data which will make prediction
    # output_path: path to store the prediction
    """

    from google.cloud import automl_v1beta1 as automl
    import csv

    automl_client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = automl_client.model_path(
        project_id, compute_region, model_id
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
        output_uris = output_path.split(",").strip()
        output_config = {"gcs_destination": {"output_uris": output_uris}}

    # Query model
    response = prediction_client.batch_predict(
        model_full_id, input_config, output_config)
    print("Making batch prediction... ")
    try:
        result = response.result()
    except:
        # Hides Any to BatchPredictResult error.
        pass
    print("Batch prediction complete.\n{}".format(response.metadata))    
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    predict_parser = subparsers.add_parser("predict", help='online prediction')
    predict_parser.add_argument("--model_id")
    predict_parser.add_argument("--file_path")

    batch_predict_parser = subparsers.add_parser("batch_predict", help='batch prediction')
    batch_predict_parser.add_argument("--model_id")
    batch_predict_parser.add_argument("--input_path")
    batch_predict_parser.add_argument("--output_path")

    args = parser.parse_args()

    project_id = "hackathon1-183523"
    compute_region = "us-central1"
    
    if args.command == "predict":
        predict(
            project_id,
            compute_region,
            args.model_id,
            args.file_path
        )

    if args.command == "batch_predict":
        batch_predict(
            project_id,
            compute_region,
            args.model_id,
            args.input_path,
            args.output_path,
        )

