from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query4():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

# Get Total sales in 2015
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT SUM(fact_table.total_price) "total_sales"
        FROM star_schema.fact_table
        JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key
        WHERE time_data.year = '2015'
        """
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        total_sales_in_2015 = pd.read_sql_query(insert_stmt, con)
        total_sales_in_2015s = total_sales_in_2015.dropna()
        return total_sales_in_2015s.to_dict(orient='records')


if __name__ == '__main__':
    query4 = Query4()
    result = query4.execute()
    print(result)