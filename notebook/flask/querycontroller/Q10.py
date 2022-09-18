from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query10():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):


# Total Price By Transaction(Cash/ Card/ Mobile)
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT store_dim.store_key, month, SUM(total_price)/30 as avg_sales
        FROM star_schema.fact_table
        JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key
        JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key
        GROUP BY CUBE(store_dim.store_key, time_data."month")
        ORDER By store_dim.store_key, month"""
        cur = con.cursor()
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        avg_sales_prod = pd.read_sql_query(insert_stmt, con)
        avg_sales_prods = avg_sales_prod.dropna()
        avg_sales_prods = avg_sales_prods[:60]
        return avg_sales_prods.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    result = query10.execute()
    print(result)