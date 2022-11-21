<<<<<<< HEAD
from flask import jsonify, request, Flask
from flask_cors import CORS

from router import query_api

app = Flask(__name__)
CORS(app)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'msg': 'Welcome Interns'})


@app.route('/hello/input', methods=['POST'])
def hello_input():
    data_dict = {}
    data_dict['name'] = request.json['name']
    data_dict['age'] = request.json['age']

    return jsonify({
        'NAME': data_dict['name'],
        'AGE': data_dict['age']
    })


app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
=======
from flask import jsonify, request, Flask
from flask_cors import CORS

from router import query_api

app = Flask(__name__)
CORS(app)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'msg': 'Welcome Interns'})


@app.route('/hello/input', methods=['POST'])
def hello_input():
    data_dict = {}
    data_dict['name'] = request.json['name']
    data_dict['age'] = request.json['age']

    return jsonify({
        'NAME': data_dict['name'],
        'AGE': data_dict['age']
    })


app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
