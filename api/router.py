from QueryServices.query10services import Query10API
from QueryServices.query1service import Query1API
from flask import Blueprint

from QueryServices.query2service import Query2API
from QueryServices.query3services import Query3API
from QueryServices.query4services import Query4API
from QueryServices.query5services import Query5API
from QueryServices.query6services import Query6API
from QueryServices.query8services import Query8API
from QueryServices.query9services import Query9API


query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/query1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/query2', view_func=Query2API.as_view("Customer wise total_sale_price"))
query_api.add_url_rule('/query3', view_func=Query3API.as_view("a"))
query_api.add_url_rule('/query4', view_func=Query4API.as_view("Customer wise a"))
query_api.add_url_rule('/query5', view_func=Query5API.as_view("w"))
query_api.add_url_rule('/query6', view_func=Query6API.as_view("e"))
query_api.add_url_rule('/query10', view_func=Query10API.as_view("r"))
query_api.add_url_rule('/query8', view_func=Query8API.as_view("ss"))
query_api.add_url_rule('/query9', view_func=Query9API.as_view("ii"))