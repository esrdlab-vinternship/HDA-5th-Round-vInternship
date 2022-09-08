from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query6():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

# The top three products that are most often purchased each store(or item supplier)
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT store_dim.store_key, item_dim.item_name
        FROM star_schema.fact_table
        JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key
        JOIN star_schema.item_dim ON item_dim.item_key = fact_table.item_key
        GROUP BY store_dim.store_key,item_dim.item_name
        ORDER BY store_key, SUM(quantity) DESC"""
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        top_three_products = pd.read_sql_query(insert_stmt, con)
        top_three_products=top_three_products.groupby('store_key').head(3)
        ptest = pd.DataFrame(top_three_products.values, columns=['store_key', 'item_name']) 
        top_three_products = {k: g["item_name"].tolist() for k,g in ptest.groupby("store_key")}
        return top_three_products

if __name__ == '__main__':
    query6 = Query6()
    result = query6.execute()
    print(result)