from google.cloud import storage
def countingWordsOfFile(bucket_name, blob_name):
    storage_client = storage.Client.from_service_account_json('private_key.json')
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    read_output = blob.download_as_string()
    print(read_output)
    temp=read_output.decode("utf-8")
    temp_list=temp.split()
    print(temp)
    print(temp_list)
    length=len(temp_list)
    return length
def set_blob_metadata(bucket_name, blob_name,length):
    storage_client = storage.Client.from_service_account_json('private_key.json')
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    metadata = {'noOfWords':length }
    blob.metadata = metadata
    blob.patch()
    print(f"The metadata for the blob {blob.name} is {blob.metadata}")
def hello_gcs(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed,
       and works for all Cloud Storage CRUD operations.
    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Cloud Logging
    """
    bucket_name=event['bucket']
    print(bucket_name)
    blob_name=event['name']
    print(blob_name)
    length=countingWordsOfFile(bucket_name, blob_name)
    print(length)
    set_blob_metadata(bucket_name, blob_name,length)
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))


  #Executed : hello_gcs
