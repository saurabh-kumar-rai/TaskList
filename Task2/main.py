from translate import Translator
from google.cloud import storage

def getdata(bucket_name, blob_name):
     storage_client = storage.Client.from_service_account_json('key.json')
     bucket = storage_client.get_bucket(bucket_name)
     blob = bucket.blob(blob_name)
     read_output = blob.download_as_string()
     print(read_output)
     temp=read_output.decode("utf-8")
     print(temp)
     return temp

def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
     storage_client = storage.Client.from_service_account_json('key.json')
     bucket = storage_client.bucket(bucket_name)
     blob = bucket.blob(destination_blob_name)
     blob.upload_from_string(contents)
     print(f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}.")

def translate_text(event, context):
     print("Processing file:")
     bucket_name=event['bucket']
     print(bucket_name)
     blob_name=event['name']
     print(blob_name)
     content=getdata(bucket_name, blob_name)
     translator= Translator(to_lang="hi")
     translation = translator.translate(content)
     print(translation)
     destination_blob_name=blob_name
     bucket_name1="langtransfinal"
     upload_blob_from_memory(bucket_name1,translation, destination_blob_name)
     print("File uploaded")

#executedfunction =  translate_text
#bucketname = langtranslationdemo
