from querycontroller.Q7 import Query7 
from flask import jsonify, request
from flask.views import MethodView

class Query7API(MethodView):
    def post(self):
        d = request.json['days']
        # print(d)
        self.q7 = Query7(days= d)
        result = self.q7.execute()
        return result