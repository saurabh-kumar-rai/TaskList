import base64
from google.cloud import storage

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    upload_blob(pubsub_message, "message_from_pubsub")

def upload_blob(contents, destination_blob_name):
    bucket_name = "pubsub-messages"
    storage_client = storage.Client.from_service_account_json('credentials.json')
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    print(f"{destination_blob_name} is uploading to {bucket_name}.")
    blob.upload_from_string(contents)
    print("File uploaded successfully.")
