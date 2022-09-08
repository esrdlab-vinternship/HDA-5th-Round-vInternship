from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query8():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

# The top three products that are most often purchased each store(or item supplier)
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT item_dim.item_name as "item", quarter
        FROM star_schema.fact_table
        JOIN star_schema.item_dim ON item_dim.item_key = fact_table.item_key
        JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key
        GROUP BY CUBE(item_name, time_data.quarter)
        ORDER BY item_name, SUM(quantity)"""
        cur = con.cursor()
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        worst_season = pd.read_sql_query(insert_stmt, con)
        worst_season = worst_season.groupby('item').head(1)
        return worst_season.to_dict(orient='records')

if __name__ == '__main__':
    query8 = Query8()
    result = query8.execute()
    print(result)