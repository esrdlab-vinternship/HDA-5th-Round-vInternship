<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query10 import Query10


class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()

    def get(self):
        result = self.q10.execute() ## Dataframe
        # print(jsonify(result))
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query10 import Query10


class Query10API(MethodView):
    def __init__(self):
        self.q10 = Query10()

    def get(self):
        result = self.q10.execute() ## Dataframe
        # print(jsonify(result))
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)