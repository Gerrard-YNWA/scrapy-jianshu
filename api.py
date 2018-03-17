from flask import Flask, request, jsonify
import pymongo
import json

mongo_settings = {
    "MONGO_HOST": "127.0.0.1",
    "MONGO_PORT": 27017,
    "MONGO_DB": "jianshu",
    "MONGO_COLL": "homepage",
    "MONGO_USER": "test",
    "MONGO_PSW": "xxxxxx"
}

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

client = pymongo.MongoClient(host=mongo_settings['MONGO_HOST'], port=mongo_settings['MONGO_PORT'])
db = client[mongo_settings['MONGO_DB']]
db.authenticate(mongo_settings['MONGO_USER'], mongo_settings['MONGO_PSW'])
coll = db[mongo_settings['MONGO_COLL']]


@app.route('/hot', methods=['GET'])
def index():
    page = int(request.args.get("page")) if request.args.get("page") is not None else 1
    size = int(request.args.get("size")) if request.args.get("size") is not None else 10
    size = 50 if size > 50 else size
    limit = size
    skip = (page-1)*limit
    records = coll.find({},{"_id":0}).skip(skip).limit(limit)
    items = []
    for item in records:
        items.append(item)
    return jsonify({"code":0, "msg":"success", "data":items})


if __name__ == '__main__':
    app.run("127.0.0.1", 6666)
