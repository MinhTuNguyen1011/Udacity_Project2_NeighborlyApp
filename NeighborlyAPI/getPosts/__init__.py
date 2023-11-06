import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://azurecosmosdbneighborly:SDnHk2IYrtaCuYzcp75TIZYqbqvu6C4tVPVRMWNXWLmtMyJHTXsnpLUaOJHFgDIQTl1rQ4LTId7lACDbowSl7w==@azurecosmosdbneighborly.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurecosmosdbneighborly@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['azurecosmosdbneighborly']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)