from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query8:
    def _init_(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query8 = """SELECT time_dim.quarter,item_dim.item_name,store_dim.division,MIN(fact_table.total_price)  
FROM ecomdb_schema.fact_table 
JOIN ecomdb_schema.item_dim ON
item_dim.item_key = fact_table.item_key 
JOIN ecomdb_schema.store_dim ON
store_dim.store_key = fact_table.store_key
JOIN ecomdb_schema.time_dim ON
time_dim.time_key = fact_table.time_key
GROUP BY CUBE (time_dim.quarter,item_dim.item_name,store_dim.division)
ORDER BY MIN(fact_table.total_price) DESC"""
        cur.execute(query8)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Season','Item','Division','Total Sales'])
        pd_data['Total Sales'] = pd_data['Total Sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)