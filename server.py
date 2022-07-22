from unittest import result
from flask import Flask, request
from about import me
from data import mock_data
import json
import random
from config import db  # db = data base
from bson import ObjectId

app = Flask('server')

# root


@app.get('/')
def home():
    return "hello from flask server"

#  end point


@app.get('/test')
def test():
    return 'this is just a test'

#  end point


####################################################################
# API END-POINTS =  PRODUCTS
####################################################################


@app.get('/api/version')
def version():
    return '1.0'


@app.get('/api/about')
def about_json():
    # return me['first'] + ' ' + me['last']
    # return f'{me[first]} {me[last]}'
    return json.dumps(me)  # parse dictionary into a json string


########################
# fix mongol _id

def fix_mongo_id(obj):
    onj['id'] = str(obj['_id'])
    del obj['_id']
    return obj
#######################


@app.get('/api/products')
def get_products():
    cursor = db.prod.find({})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)

# POST
# communicate front with back end


@app.post('/api/products')
def save_product():
    prod = request.get_json()

    # save prod
    db.products.insert_one(prod)

    #  fix the _id
    prod["id"] = str(prod["_id"])
    del prod["_id"]  # deletes under score from 'id

    return json.dumps(prod)

################
# get /api/products
# return mock_data a json string containing
# GET


@app.get('/api/products/<id>')
def get_id_by_product(id):
    prod = db.prod.find_one({"_id": ObjectId(id)})
    if not prod:
        return "NOT FOUND"

    fix_mongo_id(prod)
    return json.dumps(prod)


@app.get('/api/categories')
def get_categories():
    cursor = db.prod.find({})
    categories = []
    for product in cursor:
        cat = product['category']

        if not cat in categories:   # this helps filter out dupplicates
            categories.append(categories)

    return json.dumps(categories)

#########
# create a results list
# travel the list, get every prod
# if prod -> category is equal to the category variable
# add prod to the results list
# outside the for loop, return the results list as json


@app.get('/api/products_category/<category>')
def get_prod_cat(category):
    cursor = db.prod.find({'category': category})
    results = []
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)

    return json.dumps(results)
################
#  cursor = db.prod.find({})
#     results = []
#     for prod in cursor:
#         fix_mongo_id(prod)
#         results.append(prod)


@app.get('/api/product_cheapest')
def get_cheapest():
    cursor = db.prod.find({})
    cheapest = mock_data[0]
    for prod in cursor:
        if prod['price'] < cheapest['price']:
            cheapest = prod
    fix_mongo_id(cheapest)
    return json.dumps(cheapest)


@app.get('/api/count_products')
def get_prod_count():
    cursor = db.prod.find({})
    count = 0
    for prod in cursor:
        count += 1

    return json.dumps({"count": count})


@app.get('/api/search/<text>')
def search_prod(text):
    result = []

    text = text.lower()
    for prod in mock_data:
        if text in prod["title"].lower():
            result.append(prod)

    return json.dumps(result)


###########
app.run(debug=True, port=5001)
