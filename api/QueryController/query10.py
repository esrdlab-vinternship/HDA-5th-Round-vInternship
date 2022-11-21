<<<<<<< HEAD
from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmts = """SELECT store_dim.store_key, time_dim.month, AVG(fact_table.total_price)  
        FROM ecomdb_star_schema.fact_table 
        JOIN ecomdb_star_schema.store_dim ON
        store_dim.store_key = fact_table.store_key
        JOIN ecomdb_star_schema.time_dim ON
        time_dim.time_key = fact_table.time_key
        GROUP BY CUBE (store_dim.store_key,time_dim.month)
        ORDER BY store_dim.store_key,time_dim.month"""
        # BY ()cur = con.cursor()
        cur.execute(select_stmts)
        records = cur.fetchall()
        avg_mon_df = pd.DataFrame(list(records), columns=['Store', 'Month', 'Average_Sales'])
        avg_mon_df = avg_mon_df.dropna()
        return avg_mon_df.to_dict(orient='records')[:144]

if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
=======
from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmts = """SELECT store_dim.store_key, time_dim.month, AVG(fact_table.total_price)  
        FROM ecomdb_star_schema.fact_table 
        JOIN ecomdb_star_schema.store_dim ON
        store_dim.store_key = fact_table.store_key
        JOIN ecomdb_star_schema.time_dim ON
        time_dim.time_key = fact_table.time_key
        GROUP BY CUBE (store_dim.store_key,time_dim.month)
        ORDER BY store_dim.store_key,time_dim.month"""
        # BY ()cur = con.cursor()
        cur.execute(select_stmts)
        records = cur.fetchall()
        avg_mon_df = pd.DataFrame(list(records), columns=['Store', 'Month', 'Average_Sales'])
        avg_mon_df = avg_mon_df.dropna()
        return avg_mon_df.to_dict(orient='records')[:144]

if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
    print(data)