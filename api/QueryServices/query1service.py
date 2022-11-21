<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView
from QueryController.query1 import Query1


class Query1API(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute() ## Dataframe
        # print(jsonify(result))
=======
from flask import jsonify
from flask.views import MethodView
from QueryController.query1 import Query1


class Query1API(MethodView):
    def __init__(self):
        self.q1 = Query1()

    def get(self):
        result = self.q1.execute() ## Dataframe
        # print(jsonify(result))
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)