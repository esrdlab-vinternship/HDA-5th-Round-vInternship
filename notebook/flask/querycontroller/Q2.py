from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query2():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):


# Total Price By Transaction(Cash/ Card/ Mobile)
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT trans_dim.trans_type, SUM(fact_table.total_price) "total_sales"
        FROM star_schema.fact_table
        JOIN star_schema.trans_dim ON trans_dim.payment_key = fact_table.payment_key
        GROUP BY CUBE(trans_dim.trans_type)
        ORDER BY trans_dim.trans_type"""
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        total_price_by_trans_type = pd.read_sql_query(insert_stmt, con)
        total_price_by_trans_types = total_price_by_trans_type.dropna()
        return total_price_by_trans_types.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    result = query2.execute()
    print(result)