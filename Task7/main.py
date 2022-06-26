from google.cloud import storage

def count_blobs(bucket_name):
    #storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json('credentials.json')
    try:
        blobs = storage_client.list_blobs(bucket_name)
        noOfObj=0
        for blob in blobs:
            #print(blob)
            noOfObj += 1
        res = "Bucket name: {}; <br/>No. of objects in bucket: {}".format(bucket_name, noOfObj)
        return res
    except Exception as e:
        #print(e)
        return(e)

def start_here(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name="crested-aquifer-my-bucket-1"
    return count_blobs(name)
