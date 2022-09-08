from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query3():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):


# Total Price By Transaction(Cash/ Card/ Mobile)
        con = PostgresConnection().getConnection()
        insert_stmt = """Select SUM(fact_table.total_price) "total_sales"
        FROM star_schema.fact_table
        JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key
        WHERE store_dim.district = 'BARISAL'
        """
        cur = con.cursor()
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        total_sales_in_barisal = pd.read_sql_query(insert_stmt, con)
        total_sales_in_barisals = total_sales_in_barisal.dropna()
        return total_sales_in_barisals.to_dict(orient='records')


if __name__ == '__main__':
    query3 = Query3()
    result = query3.execute()
    print(result)