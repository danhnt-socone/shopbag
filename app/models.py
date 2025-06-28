from . import mongo

def get_all_products():
    return mongo.db.products.find()

def add_product(data):
    return mongo.db.products.insert_one(data)
