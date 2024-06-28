from flask import Flask,request


app = Flask(__name__)

stores = [          #data stored in list instead of DB
    {
        "name": "my store",
        "items": [
            {
                "name": "chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")  # create endpoints
def get_stores():
    return {"stores":stores} #return all datas and it will in JSON format (which is long string)

@app.post("/store")
def create_stores():
    req_data = request.get_json()
    new_store = {"name": req_data["name"] , "items":[]}
    stores.append(new_store)
    return new_store, 201 # as we created a store we need to give the status code as well default will 200(ok) but we need to give 201 (created)

@app.post("/store/<string:name>/item") # add items to particular store
def create_item(name):  
    req_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": req_data["name"], "price":req_data["price"]}
            store["items"].append(new_item)
            return new_item , 201
    return {"message": "Item not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/items")
def get_storesp(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

