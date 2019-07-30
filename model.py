# This script is a demo to perform basic operations on GCP AutoML Tables model training. #
# Reference: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/tables/tables/automl/automl_tables_model.py #

import argparse
import os

def create_model(project_id, compute_region, dataset_id, model_name, train_budget_milli_node_hours):
    
    """
    Create a model.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_name: create a name to model
    # train_budget_milli_node_hours: 1000=1hr
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, compute_region)

    # Sets an (optional) maximum train time, 1000 = 1 hour.
    tables_model_metadata = {}
    if train_budget_milli_node_hours:
        tables_model_metadata.update(
            {'train_budget_milli_node_hours': train_budget_milli_node_hours}
        )

    # Set model name, dataset source, and metadata.
    my_model = {
        "display_name": model_name,
        "dataset_id": dataset_id,
        "tables_model_metadata": tables_model_metadata,
    }

    # Create a model with the model metadata in the region.
    response = client.create_model(project_location, my_model)

    print("Training model...")
    print("Training operation name: {}".format(response.operation.name))
    print("Training completed: {}".format(response.result()))
    
    return response



def get_operation_status(operation_full_id):
    
    """
    Get operation status.
    #operation_full_id ='projects/<projectId>/locations/<region>/operations/<operationId>'
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the latest state of a long-running operation.
    response = client.transport._operations_client.get_operation(
        operation_full_id
    )

    print("Operation status: {}".format(response))
    

    
    
def list_models(project_id, compute_region, filter_=None):
    """
    List all models.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    """

    from google.cloud import automl_v1beta1 as automl
    from google.cloud.automl_v1beta1 import enums

    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, compute_region)

    # List all the models available in the region by applying filter.
    response = client.list_models(project_location, filter_)

    print("List of models:")
    for model in response:
        # Retrieve deployment state.
        if model.deployment_state == enums.Model.DeploymentState.DEPLOYED:
            deployment_state = "deployed"
        else:
            deployment_state = "undeployed"

        # Display the model information.
        print("Model name: {}".format(model.name))
        print("Model id: {}".format(model.name.split("/")[-1]))
        print("Model display name: {}".format(model.display_name))
        metadata = model.tables_model_metadata
        print("Target column display name: {}".format(
            metadata.target_column_spec.display_name))
        print("Training budget in node milli hours: {}".format(
            metadata.train_budget_milli_node_hours))
        print("Training cost in node milli hours: {}".format(
            metadata.train_cost_milli_node_hours))
        print("Model create time:")
        print("\tseconds: {}".format(model.create_time.seconds))
        print("\tnanos: {}".format(model.create_time.nanos))
        print("Model deployment state: {}".format(deployment_state))
        print("\n")
        
        break
        
        
        
def get_model(project_id, compute_region, model_id):
    """
    Get model details.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    """

    from google.cloud import automl_v1beta1 as automl
    from google.cloud.automl_v1beta1 import enums

    client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = client.model_path(project_id, compute_region, model_id)

    # Get complete detail of the model.
    model = client.get_model(model_full_id)

    # Retrieve deployment state.
    if model.deployment_state == enums.Model.DeploymentState.DEPLOYED:
        deployment_state = "deployed"
    else:
        deployment_state = "undeployed"

    # Display the model information.
    print("Model name: {}".format(model.name))
    print("Model id: {}".format(model.name.split("/")[-1]))
    print("Model display name: {}".format(model.display_name))
    print("Model metadata:")
    print(model.tables_model_metadata)
    print("Model create time:")
    print("\tseconds: {}".format(model.create_time.seconds))
    print("\tnanos: {}".format(model.create_time.nanos))
    print("Model deployment state: {}".format(deployment_state))
    

    

def list_model_evaluations(project_id, compute_region, model_id, filter_=None):
    """
    List model evaluations.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = client.model_path(project_id, compute_region, model_id)

    # List all the model evaluations in the model by applying filter.
    response = client.list_model_evaluations(model_full_id, filter_)

    print("List of model evaluations:")
    for evaluation in response:
        print("Model evaluation name: {}".format(evaluation.name))
        print("Model evaluation id: {}".format(evaluation.name.split("/")[-1]))
        print("Model evaluation example count: {}".format(
            evaluation.evaluated_example_count))
        print("Model evaluation time:")
        print("\tseconds: {}".format(evaluation.create_time.seconds))
        print("\tnanos: {}".format(evaluation.create_time.nanos))
        print("\n")
        
        break
        
        

def get_model_evaluation(project_id, compute_region, model_id, model_evaluation_id):
    """
    Get model evaluation.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    # model_evaluation_id: 
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the model evaluation.
    model_evaluation_full_id = client.model_evaluation_path(
        project_id, compute_region, model_id, model_evaluation_id
    )

    # Get complete detail of the model evaluation.
    response = client.get_model_evaluation(model_evaluation_full_id)

    print(response)
    


def display_evaluation(project_id, compute_region, model_id, filter_=None):
    """
    Display evaluation.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = client.model_path(project_id, compute_region, model_id)

    # List all the model evaluations in the model by applying filter.
    response = client.list_model_evaluations(model_full_id, filter_)

    # Iterate through the results.
    for evaluation in response:
        # There is evaluation for each class in a model and for overall model.
        # Get only the evaluation of overall model.
        if not evaluation.annotation_spec_id:
            model_evaluation_id = evaluation.name.split("/")[-1]

    # Resource name for the model evaluation.
    model_evaluation_full_id = client.model_evaluation_path(
        project_id, compute_region, model_id, model_evaluation_id
    )

    # Get a model evaluation.
    model_evaluation = client.get_model_evaluation(model_evaluation_full_id)

    regression_metrics = model_evaluation.regression_evaluation_metrics
    if str(regression_metrics):
        print("Model regression metrics:")
        print("Model RMSE: {}".format(regression_metrics.root_mean_squared_error))
        print("Model MAE: {}".format(regression_metrics.mean_absolute_error))
        print("Model MAPE: {}".format(
            regression_metrics.mean_absolute_percentage_error))
        print("Model R^2: {}".format(regression_metrics.r_squared))
        



def deploy_model(project_id, compute_region, model_id):
    """
    Deploy model.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = client.model_path(project_id, compute_region, model_id)

    # Deploy model
    response = client.deploy_model(model_full_id)

    print("Model deployed.")



def undeploy_model(project_id, compute_region, model_id):
    """
    Undeploy model.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # model_id: 'table id+today's day'
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the model.
    model_full_id = client.model_path(project_id, compute_region, model_id)

    # Deploy model
    response = client.undeploy_model(model_full_id)

    print("Model undeployed.")

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # create model
    create_model_parser = subparsers.add_parser(
        "create_model", help='create a model'
    )
    create_model_parser.add_argument("--dataset_id")
    create_model_parser.add_argument("--model_name")
    create_model_parser.add_argument("--train_budget_milli_node_hours", type=int,)
    create_model_parser.add_argument("--optimization_objective")

    # get status
    get_operation_status_parser = subparsers.add_parser("get_operation_status", help='get operation status')
    get_operation_status_parser.add_argument("--operation_full_id")

    # list existing models
    list_models_parser = subparsers.add_parser("list_models", help='list of existing model')
    list_models_parser.add_argument("--filter_")

    # get model
    get_model_parser = subparsers.add_parser("get_model", help='get the AutoMl Tables model')
    get_model_parser.add_argument("--model_id")

    # model evaluation
    list_model_evaluations_parser = subparsers.add_parser("list_model_evaluations", help='list model evaluation')
    list_model_evaluations_parser.add_argument("--model_id")
    list_model_evaluations_parser.add_argument("--filter_")

    # get evaluation
    get_model_evaluation_parser = subparsers.add_parser("get_model_evaluation", help='get model evaluation')
    get_model_evaluation_parser.add_argument("--model_id")
    get_model_evaluation_parser.add_argument("--model_evaluation_id")

    # display evaluation
    display_evaluation_parser = subparsers.add_parser("display_evaluation", help='display model evaluation')
    display_evaluation_parser.add_argument("--model_id")
    display_evaluation_parser.add_argument("--filter_")

    # deploy model
    deploy_model_parser = subparsers.add_parser("deploy_model", help='deploy model')
    deploy_model_parser.add_argument("--model_id")

    # undeploy model
    undeploy_model_parser = subparsers.add_parser("undeploy_model", help='undeploy model')
    undeploy_model_parser.add_argument("--model_id")

    project_id = "hackathon1-183523"
    compute_region = "us-central1"

    args = parser.parse_args()

    if args.command == "create_model":
        create_model(
            project_id,
            compute_region,
            args.dataset_id,
            args.model_name,
            args.train_budget_milli_node_hours
        )
        
    if args.command == "get_operation_status":
        get_operation_status(args.operation_full_id)
        
    if args.command == "list_models":
        list_models(project_id, compute_region, args.filter_)
        
    if args.command == "get_model":
        get_model(project_id, compute_region, args.model_id)
        
    if args.command == "list_model_evaluations":
        list_model_evaluations(
            project_id, compute_region, args.model_id, args.filter_
        )
        
    if args.command == "get_model_evaluation":
        get_model_evaluation(
            project_id, compute_region, args.model_id, args.model_evaluation_id
        )
        
    if args.command == "display_evaluation":
        display_evaluation(
            project_id, compute_region, args.model_id, args.filter_
        )
        
    if args.command == "deploy_model":
        deploy_model(project_id, compute_region, args.model_id)
        
    if args.command == "undeploy_model":
        undeploy_model(project_id, compute_region, args.model_id)





