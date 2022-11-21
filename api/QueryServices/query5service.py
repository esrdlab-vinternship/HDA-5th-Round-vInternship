<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query5 import Query5


class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        result = self.q5.execute()
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query5 import Query5


class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        result = self.q5.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)