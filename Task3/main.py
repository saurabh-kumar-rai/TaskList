import base64
import json
import requests
from google.cloud import storage
from apiKey import *

def weather_api(name):
    print("Fetching from API...")
    apireq = "{}?key={}&q={}".format(API, API_KEY, name)
    print("Data Fetched.")
    response = requests.get(apireq)
    return response.json()

def upload_blob(contents, destination_blob_name):
    bucket_name = "weather-api-data"
    storage_client = storage.Client.from_service_account_json('credentials.json')
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    print(f"{destination_blob_name} is uploading to {bucket_name}.")
    blob.upload_from_string(data=json.dumps(contents), content_type='application/json')

def hello_pubsub(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print("Message from pubsub:", pubsub_message)
    data = weather_api(pubsub_message)
    res2 = upload_blob(data, pubsub_message+"_weather_report")
    return ("Weather Data successfully uploaded to bucket")
  
