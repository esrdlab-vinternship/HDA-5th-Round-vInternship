from services.allquery import Query1API

from flask import Blueprint

query_api = Blueprint('queryapi', __name__)
query_api.add_url_rule("/q1", view_func=Query1API.as_view("Get division wise total sales"))
