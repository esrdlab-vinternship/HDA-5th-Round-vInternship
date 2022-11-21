<<<<<<< HEAD
from flask import jsonify
from flask.views import MethodView

from QueryController.query3 import Query3


class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        result = self.q3.execute()
=======
from flask import jsonify
from flask.views import MethodView

from QueryController.query3 import Query3


class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        result = self.q3.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return jsonify(result)