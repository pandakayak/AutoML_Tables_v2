# This script is a demo to perform basic operations on GCP AutoML Tables dataset. #
# Reference: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/tables/tables/automl/automl_tables_dataset.py #

import argparse
import os

def create_dataset(project_id, compute_region, dataset_name):
    
    """
    Create an empty dataset.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_name: giving the dataset a name
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, compute_region)

    # Set dataset name and metadata of the dataset.
    my_dataset = {
        "display_name": dataset_name,
        "tables_dataset_metadata": {}
    }

    # Create a dataset with the dataset metadata in the region.
    dataset = client.create_dataset(project_location, my_dataset)

    # Display the dataset information.
    print("Dataset name: {}".format(dataset.name))
    print("Dataset id: {}".format(dataset.name.split("/")[-1]))
    print("Dataset display name: {}".format(dataset.display_name))
    print("Dataset metadata:")
    print("\t{}".format(dataset.tables_dataset_metadata))
    print("Dataset example count: {}".format(dataset.example_count))
    print("Dataset create time:")
    print("\tseconds: {}".format(dataset.create_time.seconds))
    print("\tnanos: {}".format(dataset.create_time.nanos))
    
    return dataset

    
def list_datasets(project_id, compute_region, filter_=None):
    """
    List all existing datasets in AutoML Tables.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # A resource that represents Google Cloud Platform location.
    project_location = client.location_path(project_id, compute_region)

    # List all the datasets available in the region by applying filter.
    response = client.list_datasets(project_location, filter_)

    print("List of datasets:")
    for dataset in response:
        # Display the dataset information.
        print("Dataset name: {}".format(dataset.name))
        print("Dataset id: {}".format(dataset.name.split("/")[-1]))
        print("Dataset display name: {}".format(dataset.display_name))
        metadata = dataset.tables_dataset_metadata
        print("Dataset primary table spec id: {}".format(
            metadata.primary_table_spec_id))
        print("Dataset target column spec id: {}".format(
            metadata.target_column_spec_id))
        print("Dataset target column spec id: {}".format(
            metadata.target_column_spec_id))
        print("Dataset weight column spec id: {}".format(
            metadata.weight_column_spec_id))
        print("Dataset ml use column spec id: {}".format(
            metadata.ml_use_column_spec_id))
        print("Dataset example count: {}".format(dataset.example_count))
        print("Dataset create time:")
        print("\tseconds: {}".format(dataset.create_time.seconds))
        print("\tnanos: {}".format(dataset.create_time.nanos))
        print("\n")

        
        
def list_table_specs(project_id, compute_region, dataset_id, filter_=None):
    """
    List all table specs.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by executing list_datasets
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the dataset.
    dataset_full_id = client.dataset_path(
        project_id, compute_region, dataset_id
    )

    # List all the table specs in the dataset by applying filter.
    response = client.list_table_specs(dataset_full_id, filter_)

    print("List of table specs:")
    for table_spec in response:
        # Display the table_spec information.
        print("Table spec name: {}".format(table_spec.name))
        print("Table spec id: {}".format(table_spec.name.split("/")[-1]))
        print("Table spec time column spec id: {}".format(
            table_spec.time_column_spec_id))
        print("Table spec row count: {}".format(table_spec.row_count))
        print("Table spec column count: {}".format(table_spec.column_count))
        
        
        
        
def list_column_specs(project_id, compute_region, dataset_id, table_spec_id, filter_=None):
    """
    List all column specs.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    # table_spec_id: a long format numeric id, can retrieve by executing list_table_specs
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the table_spec.
    table_spec_full_id = client.table_spec_path(
        project_id, compute_region, dataset_id, table_spec_id
    )

    # List all the column specs in the table spec by applying filter.
    response = client.list_column_specs(table_spec_full_id, filter_)
    
    column_spec_id_dic = {}

    print("List of column specs:")
    for column_spec in response:
        # Display the column_spec information.
        print("Column spec name: {}".format(column_spec.name))
        print("Column spec id: {}".format(column_spec.name.split("/")[-1]))
        column_spec_id_dic[column_spec.display_name] = column_spec.name.split("/")[-1]
        print("Column spec display name: {}".format(column_spec.display_name))
        print("Column spec data type: {}".format(column_spec.data_type))
        
    print("target_column_spec_id: {}".format(column_spec_id_dic['price_per_mile']))
    



        
def get_dataset(project_id, compute_region, dataset_id):
    """
    Get the dataset.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the dataset.
    dataset_full_id = client.dataset_path(
        project_id, compute_region, dataset_id
    )

    # Get complete detail of the dataset.
    dataset = client.get_dataset(dataset_full_id)

    # Display the dataset information.
    print("Dataset name: {}".format(dataset.name))
    print("Dataset id: {}".format(dataset.name.split("/")[-1]))
    print("Dataset display name: {}".format(dataset.display_name))
    print("Dataset metadata:")
    print("\t{}".format(dataset.tables_dataset_metadata))
    print("Dataset example count: {}".format(dataset.example_count))
    print("Dataset create time:")
    print("\tseconds: {}".format(dataset.create_time.seconds))
    print("\tnanos: {}".format(dataset.create_time.nanos))
    
    
    
    
def get_table_spec(project_id, compute_region, dataset_id, table_spec_id):
    """
    Get the table spec.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    # table_spec_id: a long format numeric id, can retrieve by executing list_table_specs
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the table spec.
    table_spec_full_id = client.table_spec_path(
        project_id, compute_region, dataset_id, table_spec_id
    )

    # Get complete detail of the table spec.
    table_spec = client.get_table_spec(table_spec_full_id)

    # Display the table spec information.
    print("Table spec name: {}".format(table_spec.name))
    print("Table spec id: {}".format(table_spec.name.split("/")[-1]))
    print("Table spec time column spec id: {}".format(
        table_spec.time_column_spec_id))
    print("Table spec row count: {}".format(table_spec.row_count))
    print("Table spec column count: {}".format(table_spec.column_count))
    
    
    
def get_column_spec(project_id, compute_region, dataset_id, table_spec_id, column_spec_id):
    """
    Get the column spec.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    # table_spec_id: a long format numeric id, can retrieve by executing list_table_specs
    # column_spec_id: a long format numeric id, can retrieve by executing get_table_specs
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the column spec.
    column_spec_full_id = client.column_spec_path(
        project_id, compute_region, dataset_id, table_spec_id, column_spec_id
    )

    # Get complete detail of the column spec.
    column_spec = client.get_column_spec(column_spec_full_id)

    # Display the column spec information.
    print("Column spec name: {}".format(column_spec.name))
    print("Column spec id: {}".format(column_spec.name.split("/")[-1]))
    print("Column spec display name: {}".format(column_spec.display_name))
    print("Column spec data type: {}".format(column_spec.data_type))
    print("Column spec data stats: {}".format(column_spec.data_stats))
    print("Column spec top correlated columns\n")
    for column_correlation in column_spec.top_correlated_columns:
        print(column_correlation)
                
        
def import_data(project_id, compute_region, dataset_id, path):
    """
    Import structured data.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    # path: directory to Google Cloud Storage or BigQuery
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the dataset.
    dataset_full_id = client.dataset_path(
        project_id, compute_region, dataset_id
    )

    if path.startswith('bq'):
        input_config = {"bigquery_source": {"input_uri": path}}
    else:    
        # Get the multiple Google Cloud Storage URIs.
        input_uris = path.split(",")
        input_config = {"gcs_source": {"input_uris": input_uris}}

    # Import data from the input URI.
    response = client.import_data(dataset_full_id, input_config)

    print("Processing import...")
    # synchronous check of operation status.
    print("Data imported. {}".format(response.result()))
    
    
    
def schema_review(dataset_name):
    """
    review the schema.
    # dataset_name: giving the dataset a name
    """

    import google.cloud.automl_v1beta1.proto.data_types_pb2 as data_types
    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # List table specs
    list_table_specs_response = client.list_table_specs(dataset_name)
    table_specs = [s for s in list_table_specs_response]

    # List column specs
    table_spec_name = table_specs[0].name
    list_column_specs_response = client.list_column_specs(table_spec_name)
    column_specs = {s.display_name: s for s in list_column_specs_response}
    for x in column_specs.keys():
        print("Feature name:{}".format(x))
        print("Feature name:{}".format(data_types.TypeCode.Name(column_specs[x].data_type.type_code))) 
        print("")
        
        
        
def update_dataset(project_id, compute_region, dataset_id, target_column_spec_id):
    """
    Update dataset.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the dataset.
    dataset_full_id = client.dataset_path(
        project_id, compute_region, dataset_id
    )

    # Set the target, weight, and ml use columns in the tables dataset metadata.
    tables_dataset_metadata = {}
    if target_column_spec_id:
        tables_dataset_metadata['target_column_spec_id'] = target_column_spec_id

    # Set the updated tables dataset metadata in the dataset.
    my_dataset = {
        'name': dataset_full_id,
        'tables_dataset_metadata': tables_dataset_metadata,
    }

    # Update the dataset.
    response = client.update_dataset(my_dataset)

    # synchronous check of operation status.
    print("Dataset updated. {}".format(response))
    
    
    
def update_column_spec(project_id, compute_region, dataset_id, table_spec_id, column_spec_id, type_code, nullable=None):
    """
    Update column spec.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    # table_spec_id: a long format numeric id, can retrieve by executing list_table_specs
    # column_spec_id: a long format numeric id, can retrieve by executing get_table_specs
    # type_code: Numeric or Category
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the column spec.
    column_spec_full_id = client.column_spec_path(
        project_id, compute_region, dataset_id, table_spec_id, column_spec_id
    )

    # Set type code and nullable in data_type.
    data_type = {'type_code': type_code}
    if nullable is not None:
        data_type['nullable'] = nullable

    # Set the updated data_type in the column_spec.
    my_column_spec = {
        'name': column_spec_full_id,
        'data_type': data_type,
    }

    # Update the column spec.
    response = client.update_column_spec(my_column_spec)

    # synchronous check of operation status.
    print("Table spec updated. {}".format(response))
    
    
    
def delete_dataset(project_id, compute_region, dataset_id):
    """
    Delete a dataset.
    # project_id: the 'Project ID showed in GCP Console
    # compute_region: only 'us-central1' works now
    # dataset_id: start with 'TBL', can retrieve the info by execute list_datasets
    """

    from google.cloud import automl_v1beta1 as automl

    client = automl.AutoMlClient()

    # Get the full path of the dataset.
    dataset_full_id = client.dataset_path(
        project_id, compute_region, dataset_id
    )

    # Delete a dataset.
    response = client.delete_dataset(dataset_full_id)

    # synchronous check of operation status.
    print("Dataset deleted. {}".format(response.result()))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    # create dataset
    create_dataset_parser = subparsers.add_parser("create_dataset", help='create dataset')
    create_dataset_parser.add_argument("--dataset_name")

    # list dataset
    list_datasets_parser = subparsers.add_parser("list_datasets", help='list dataset')
    list_datasets_parser.add_argument("--filter_")

    # list table specs
    list_table_specs_parser = subparsers.add_parser("list_table_specs", help='list table specs')
    list_table_specs_parser.add_argument("--dataset_id")
    list_table_specs_parser.add_argument("--filter_")

    # list column specs
    list_column_specs_parser = subparsers.add_parser("list_column_specs", help='list column specs')
    list_column_specs_parser.add_argument("--dataset_id")
    list_column_specs_parser.add_argument("--table_spec_id")
    list_column_specs_parser.add_argument("--filter_")

    # get dataset
    get_dataset_parser = subparsers.add_parser("get_dataset", help='get dataset')
    get_dataset_parser.add_argument("--dataset_id")

    get_table_spec_parser = subparsers.add_parser(
        "get_table_spec", help=get_table_spec.__doc__
    )
    get_table_spec_parser.add_argument("--dataset_id")
    get_table_spec_parser.add_argument("--table_spec_id")

    # get column spec
    get_column_spec_parser = subparsers.add_parser("get_column_spec", help='get column specs')
    get_column_spec_parser.add_argument("--dataset_id")
    get_column_spec_parser.add_argument("--table_spec_id")
    get_column_spec_parser.add_argument("--column_spec_id")

    # import data
    import_data_parser = subparsers.add_parser("import_data", help='import data')
    import_data_parser.add_argument("--dataset_id")
    import_data_parser.add_argument("--path")
    
    # schema review
    schema_review_parser = subparsers.add_parser("schema_review", help='schema review')
    schema_review_parser.add_argument("--dataset_name")

    # update dataset
    update_dataset_parser = subparsers.add_parser("update_dataset", help='update dataset')
    update_dataset_parser.add_argument("--dataset_id")
    update_dataset_parser.add_argument("--target_column_spec_id")

    # update column specs
    update_column_spec_parser = subparsers.add_parser("update_column_spec", help='update column specs')
    update_column_spec_parser.add_argument("--dataset_id")
    update_column_spec_parser.add_argument("--column_spec_id")
    update_column_spec_parser.add_argument("--table_spec_id")
    update_column_spec_parser.add_argument("--type_code")
    update_column_spec_parser.add_argument("--nullable", type=bool)

    # delete dataset
    delete_dataset_parser = subparsers.add_parser("delete_dataset", help='delete dataset')
    delete_dataset_parser.add_argument("--dataset_id")

    project_id = "hackathon1-183523"
    compute_region = "us-central1"

    args = parser.parse_args()
    if args.command == "create_dataset":
        create_dataset(project_id, compute_region, args.dataset_name)
        
    if args.command == "list_datasets":
        list_datasets(project_id, compute_region, args.filter_)
        
    if args.command == "list_table_specs":
        list_table_specs(project_id,
                         compute_region,
                         args.dataset_id,
                         args.filter_)
        
    if args.command == "list_column_specs":
        list_column_specs(project_id,
                         compute_region,
                         args.dataset_id,
                         args.table_spec_id,
                         args.filter_)
        
    if args.command == "get_dataset":
        get_dataset(project_id, compute_region, args.dataset_id)
        
    if args.command == "get_table_spec":
        get_table_spec(project_id,
                       compute_region,
                       args.dataset_id,
                       args.table_spec_id)
        
    if args.command == "get_column_spec":
        get_column_spec(project_id,
                        compute_region,
                        args.dataset_id,
                        args.table_spec_id,
                        args.column_spec_id)
        
    if args.command == "import_data":
        import_data(project_id, compute_region, args.dataset_id, args.path)
        
    if args.command == "schema_review":
        schema_review(args.dataset_name)

    if args.command == "update_dataset":
        update_dataset(project_id,
                       compute_region,
                       args.dataset_id,
                       args.target_column_spec_id)
        
    if args.command == "update_column_spec":
        update_column_spec(project_id,
                           compute_region,
                           args.dataset_id,
                           args.table_spec_id,
                           args.column_spec_id,
                           args.type_code, 
                           args.nullable)
        
    if args.command == "delete_dataset":
        delete_dataset(project_id, compute_region, args.dataset_id)
