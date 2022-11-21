<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView
from QueryController.query8 import Query8


class Query8API(MethodView):
    def __init__(self):
        self.q8 = Query8()

    def get(self):
        result = self.q8.execute() ## Dataframe
        # print(jsonify(result))
=======
from flask import jsonify
from flask.views import MethodView
from QueryController.query8 import Query8


class Query8API(MethodView):
    def __init__(self):
        self.q8 = Query8()

    def get(self):
        result = self.q8.execute() ## Dataframe
        # print(jsonify(result))
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)