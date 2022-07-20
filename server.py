from unittest import result
from flask import Flask, request
from about import me
from data import mock_data
import json
import random

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


@app.get('/api/products')
def get_products():
    return json.dumps(mock_data)

# POST
# communicate front with back end


@app.post('/api/products')
def save_product():
    prod = request.get_json()

    # add product to the mock_data with append
    # assign ID to prod and generate random #
    # return the product as json

    mock_data.append(prod)
    prod['id'] = random.randint(1, 888888888)
    return json.dumps(prod)

################
#get /api/products
# return mock_data a json string containing
# GET


@app.get('/api/products/<id>')
def get_id_by_product(id):
    for prod in mock_data:
        if str(prod['id']) == id:
            return json.dumps(prod)

    return 'NOT FOUND'


#get  /api/categories/category
# #return the list of categorizes
# 1 - return OK
# 2 - travel mock_data, and print the category of every product
# 3 - pyt the category in a list and at the end of the for loop, return the list as jsonify


@app.get('/api/categories')
def get_categories():
    categories = []
    for product in mock_data:
        cat = product['category']
        if not cat in categories:   # this helps filter out dupplicates
            categories.append(cat)

    return json.dumps(categories)

#########
# create a results list
# travel the list, get every prod
# if prod -> category is equal to the category variable
# add prod to the results list
# outside the for loop, return the results list as json


@app.get('/api/products_category/<category>')
def get_prod_cat(category):
    print('your category: ', category)
    results = []
    category = category.lower()
    for prod in mock_data:
        if prod['category'].lower() == category:
            results.append(prod)

    return json.dumps(results)
################
#get /api/product_cheapest


@app.get('/api/product_cheapest')
def get_cheapest():
    cheapest = mock_data[0]
    for prod in mock_data:
        if prod['price'] < cheapest['price']:
            cheapest = prod

    return json.dumps(cheapest)


# get return the number of prod in the catalog
#  api/count_products

@app.get('/api/count_products')
def get_prod_count():
    count = len(mock_data)

    return json.dumps({"count": count})


# searches for products that contains the text you need EX: api/search/insert_text_to_find
# get /api/search/<text>
#  return all prods whose title contains text


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
