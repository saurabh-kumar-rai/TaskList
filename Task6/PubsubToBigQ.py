from google.cloud import bigquery
import base64

def pubsub_to_bigq1(data, msgID) :
   # Construct a BigQuery client object.
   bigquery_client = bigquery.Client.from_service_account_json('key.json')
   table_name="crested-aquifer-352613.mydataset01.finaldata"
   print(table_name)
   table_field="msgId,message"
   table_field_value="\""+msgID+"\",\""+data+"\""
   query = 'INSERT INTO `{}` ({}) values ({});'.format(table_name, table_field, table_field_value)
   print(query)
   query_job = bigquery_client.query(query)  # Make an API request.
   print("The query data:")
   return 'ok'

def pubsub_to_bigq(event, context):
   pubsub_message = base64.b64decode(event['data']).decode('utf-8')
   print(pubsub_message)
   msgID=context.event_id
   print(pubsub_to_bigq1(pubsub_message,  msgID))
