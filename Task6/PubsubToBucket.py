from google.cloud import storage
def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
     storage_client = storage.Client.from_service_account_json('private_key.json')
     bucket = storage_client.bucket(bucket_name)
     blob = bucket.blob(destination_blob_name)
     blob.upload_from_string(contents)
def hello_pubsub(event, context):
    
    import base64

    print("""This Function was triggered by messageId {} published at {} to {}
    """.format(context.event_id, context.timestamp, context.resource["name"]))

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'There is no data'
    print(name)
    bucket_name="crested-aquifer-my-bucket-1"
    print(bucket_name)
    destination_blob_name= "MessageID:"+str(context.event_id)
    upload_blob_from_memory(bucket_name, name, destination_blob_name)
    print("successfully uploaded")
    
    #add service_acc_credentials
    #requirnments : google-cloud-storage==2.4.0
