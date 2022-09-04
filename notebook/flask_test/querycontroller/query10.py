from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query10:
    def _init_(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query10 = """SELECT store_dim.store_key,time_dim.month,AVG(fact_table.total_price)  
FROM ecomdb_schema.fact_table 
JOIN ecomdb_schema.store_dim ON
store_dim.store_key = fact_table.store_key
JOIN ecomdb_schema.time_dim ON
time_dim.time_key = fact_table.time_key
GROUP BY CUBE (store_dim.store_key,time_dim.month)
ORDER BY AVG(fact_table.total_price) DESC"""
        cur.execute(query10)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Store Key','Month','Total Avg Sales'])
        pd_data['Total Avg Sales'] = pd_data['Total Avg Sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q10 = Query10()
    data = q10.execute()
    print(data)