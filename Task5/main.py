import pandas as pd
from google.cloud import storage
def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    storage_client = storage.Client.from_service_account_json('private_key.json')
    bucket = storage_client.get_bucket(event['bucket'])
    blob = bucket.get_blob(event['name'])
    path1="gs://"+event['bucket']+"/"+event['name']
    print(path1)
    data=pd.read_csv(path1)
    print(data.shape)
    print(data.tail(5))
    file_name=event['name'].replace(".csv","")+"_c.csv"
    path2="gs://crested-aquifer-my-bucket-1/"+file_name
    data.drop_duplicates(keep ='first', inplace = True)
    print(data.shape)
    print(data.tail(5))
    data.to_csv(path2)
