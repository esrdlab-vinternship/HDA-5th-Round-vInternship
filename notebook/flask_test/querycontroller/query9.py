from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query9:
    def _init_(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query9 = """SELECT store_dim.division,item_dim.item_name,SUM(fact_table.total_price)  
FROM ecomdb_schema.fact_table 
JOIN ecomdb_schema.store_dim ON
store_dim.store_key = fact_table.store_key
JOIN ecomdb_schema.item_dim ON
item_dim.item_key = fact_table.item_key
GROUP BY CUBE (store_dim.division,item_dim.item_name)
ORDER BY SUM(fact_table.total_price) DESC"""
        cur.execute(query9)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item Name','Division','Total Sales'])
        pd_data['Total Sales'] = pd_data['Total Sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q9 = Query9()
    data = q9.execute()
    print(data)