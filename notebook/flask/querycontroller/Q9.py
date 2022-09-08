from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query9():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):


# Total Price By Transaction(Cash/ Card/ Mobile)
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT item_name,division,  SUM(quantity)
        FROM star_schema.fact_table
        JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key
        JOIN star_schema.item_dim ON item_dim.item_key = fact_table.item_key
        GROUP BY CUBE(division, item_dim.item_name)
        ORDER BY item_name DESC"""
        total_sales_geographically = pd.read_sql_query(insert_stmt, con)
        total_sales_geographicallys = total_sales_geographically.dropna()
        return total_sales_geographicallys.to_dict(orient='records')


if __name__ == '__main__':
    query9 = Query9()
    result = query9.execute()
    print(result)