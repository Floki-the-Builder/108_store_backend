from flask import Flask


app = Flask('server')

# root


@app.get('/')
def home():
    return "hello form flask server"

#  end point


@app.get('/test')
def test():
    return 'this is just a test'

#  end point


@app.get('/About')
def about():
    return 'Ardany'
####################################################################
# API ENDOPOINTS =  PRODUCTS
####################################################################


@app.get('/api/version')
def version():
    return '1.0'


app.run(debug=True, port=5001)
