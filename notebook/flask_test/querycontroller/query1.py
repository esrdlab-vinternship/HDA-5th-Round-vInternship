from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = """SELECT store_dim.district as "District", SUM(fact_table.total_price) "Generated_revenue" 
FROM ecomdb_schema.fact_table 
JOIN ecomdb_schema.store_dim ON
store_dim.store_key = fact_table.store_key 
GROUP BY CUBE(store_dim.district) 
ORDER BY store_dim.district"""
        cur.execute(select_stmt)
        records = cur.fetchall()
        df = pd.DataFrame(list(records), columns=['division', 'sales'])
        df = df.dropna()
        return df.to_dict(orient='records')

if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)
