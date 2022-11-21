<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query6 import Query6


class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()

    def get(self):
        result = self.q6.execute()
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query6 import Query6


class Query6API(MethodView):
    def __init__(self):
        self.q6 = Query6()

    def get(self):
        result = self.q6.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)