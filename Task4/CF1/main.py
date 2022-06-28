import google
from google.cloud import pubsub_v1
import base64
from config import *
publisher = pubsub_v1.PublisherClient()

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    publish_message_to_topic(f'Passed message: {pubsub_message}')

def publish_message_to_topic(message):
    try:
        topic_name = f'projects/{GOOGLE_CLOUD_PROJECT}/topics/{TOPIC_NAME}'
        future = publisher.publish(topic_name, message.encode("utf-8"))
        future.result()
    except Exception as exc:
        print(exc)
