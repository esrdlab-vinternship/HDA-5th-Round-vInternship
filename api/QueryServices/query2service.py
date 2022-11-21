<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query2 import Query2


class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()

    def get(self):
        result = self.q2.execute()
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query2 import Query2


class Query2API(MethodView):
    def __init__(self):
        self.q2 = Query2()

    def get(self):
        result = self.q2.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)