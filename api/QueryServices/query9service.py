<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query9 import Query9


class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        result = self.q9.execute() ## Dataframe
        # print(jsonify(result))
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query9 import Query9


class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        result = self.q9.execute() ## Dataframe
        # print(jsonify(result))
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)