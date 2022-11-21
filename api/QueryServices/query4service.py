<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query4 import Query4


class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute()
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query4 import Query4


class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)