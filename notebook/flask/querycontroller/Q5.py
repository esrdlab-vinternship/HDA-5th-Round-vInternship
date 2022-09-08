from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query5():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):


# Total sales of Barisal in 2015
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT SUM(fact_table.total_price) as "total_sales"
        FROM star_schema.fact_table
        JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key 
        JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key
        WHERE time_data.year = '2015'
        AND store_dim.district = 'BARISAL'"""
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        total_sales_in_2015_and_barisal = pd.read_sql_query(insert_stmt, con)
        return total_sales_in_2015_and_barisal.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    result = query5.execute()
    print(result)