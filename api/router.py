<<<<<<< HEAD
from QueryServices.query7service import Query7API
from QueryServices.query8service import Query8API
from QueryServices.query10service import Query10API
from QueryServices.query1service import Query1API
from QueryServices.query2service import Query2API
from QueryServices.query3service import Query3API
from flask import Blueprint

from QueryServices.query4service import Query4API
from QueryServices.query5service import Query5API
from QueryServices.query6service import Query6API
from QueryServices.query9service import Query9API

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/query1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/query2', view_func=Query2API.as_view("Transaction wise sales "))
query_api.add_url_rule('/query3', view_func=Query3API.as_view("Total sales in Barisal"))
query_api.add_url_rule('/query4', view_func=Query4API.as_view("Total sales in 2015"))
query_api.add_url_rule('/query5', view_func=Query5API.as_view("Total sales of Barisal in 2015"))
query_api.add_url_rule('/query6', view_func=Query6API.as_view("Top three products purchased each store"))
query_api.add_url_rule('/query7', view_func=Query7API.as_view("Sales in X days"))
query_api.add_url_rule('/query8', view_func=Query8API.as_view("Worst quarter for each product item"))
query_api.add_url_rule('/query9', view_func=Query9API.as_view("Total sales of items geographically"))
=======
from QueryServices.query7service import Query7API
from QueryServices.query8service import Query8API
from QueryServices.query10service import Query10API
from QueryServices.query1service import Query1API
from QueryServices.query2service import Query2API
from QueryServices.query3service import Query3API
from flask import Blueprint

from QueryServices.query4service import Query4API
from QueryServices.query5service import Query5API
from QueryServices.query6service import Query6API
from QueryServices.query9service import Query9API

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/query1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/query2', view_func=Query2API.as_view("Transaction wise sales "))
query_api.add_url_rule('/query3', view_func=Query3API.as_view("Total sales in Barisal"))
query_api.add_url_rule('/query4', view_func=Query4API.as_view("Total sales in 2015"))
query_api.add_url_rule('/query5', view_func=Query5API.as_view("Total sales of Barisal in 2015"))
query_api.add_url_rule('/query6', view_func=Query6API.as_view("Top three products purchased each store"))
query_api.add_url_rule('/query7', view_func=Query7API.as_view("Sales in X days"))
query_api.add_url_rule('/query8', view_func=Query8API.as_view("Worst quarter for each product item"))
query_api.add_url_rule('/query9', view_func=Query9API.as_view("Total sales of items geographically"))
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
query_api.add_url_rule('/query10', view_func=Query10API.as_view("Average sales of products per store monthly"))