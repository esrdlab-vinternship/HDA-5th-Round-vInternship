from flask import jsonify, request
from flask.views import MethodView
import querycontroller.query1
from querycontroller.query2 import Query2
from querycontroller.quer3 import Query3
from querycontroller.query4 import Query4
from querycontroller.query5 import Query5


class Query1API(MethodView):
    def __int__(self):
        self.q1 = querycontroller.query1.Query1()

    def get(self):
        result = self.q1.execute()
        # print(jsonify(result))
        return jsonify(result)


class Query1API(MethodView):
    def __int__(self):
        self.q2 = querycontroller.query2.Query2()

    def get(self):
        result = self.q2.execute()
        # print(jsonify(result))
        return jsonify(result)



class Query3API(MethodView):
    def __init__(self):
        self.q3 = Query3()

    def get(self):
        result = self.q3.execute()
        # print(jsonify(result))
        return jsonify(result)


class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute()
        # print(jsonify(result))
        return jsonify(result)


class Query5API(MethodView):
    def __init__(self):
        self.q5 = Query5()

    def get(self):
        result = self.q5.execute()
        # print(jsonify(result))
        return jsonify(result)

class Query6API(MethodView):
    def __int__(self):
        self.q6 = querycontroller.query6.Query6()

    def get(self):
        result = self.q6.execute()
        # print(jsonify(result))
        return jsonify(result)

class Query6API(MethodView):
    def __int__(self):
        self.q8 = querycontroller.query8.Query8()

    def get(self):
        result = self.q8.execute()
        # print(jsonify(result))
        return jsonify(result)


class Query6API(MethodView):
    def __int__(self):
        self.q9 = querycontroller.query9.Query9()

    def get(self):
        result = self.q9.execute()
        # print(jsonify(result))
        return jsonify(result)


class Query6API(MethodView):
    def __int__(self):
        self.q10 = querycontroller.query10.Query10()

    def get(self):
        result = self.q10.execute()
        # print(jsonify(result))
        return jsonify(result)


class Query6API(MethodView):
    def __int__(self):
        self.q11 = querycontroller.query11.Query11()

    def get(self):
        result = self.q11.execute()
        # print(jsonify(result))
        return jsonify(result)