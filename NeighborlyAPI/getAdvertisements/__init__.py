import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://azurecosmosdbneighborly:SDnHk2IYrtaCuYzcp75TIZYqbqvu6C4tVPVRMWNXWLmtMyJHTXsnpLUaOJHFgDIQTl1rQ4LTId7lACDbowSl7w==@azurecosmosdbneighborly.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@azurecosmosdbneighborly@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['azurecosmosdbneighborly']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

