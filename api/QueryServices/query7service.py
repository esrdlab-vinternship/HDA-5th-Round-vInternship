<<<<<<< HEAD
from flask import jsonify, request
from flask.views import MethodView
from QueryController.query7 import Query7


class Query7API(MethodView):

    def post(self):
        d = request.json['days']
        self.q7 = Query7(days=d)
        result = self.q7.execute()
=======
from flask import jsonify, request
from flask.views import MethodView
from QueryController.query7 import Query7


class Query7API(MethodView):

    def post(self):
        d = request.json['days']
        self.q7 = Query7(days=d)
        result = self.q7.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)