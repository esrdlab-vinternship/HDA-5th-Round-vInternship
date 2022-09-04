from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query11:
    def _init_(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query11 ="""SELECT item_dim.item_name,trans_dim.trans_type, SUM(fact_table.quantity)  
FROM ecomdb_schema.fact_table 
JOIN ecomdb_schema.item_dim ON
item_dim.item_key = fact_table.item_key 
JOIN ecomdb_schema.trans_dim ON
trans_dim.payment_key = fact_table.payment_key
WHERE trans_dim.trans_type='mobile'and trans_dim.trans_type='card' 
GROUP BY CUBE (item_dim.item_name,trans_dim.trans_type)
ORDER BY time_dim.t_date DESC"""
        cur.execute(query11)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item Name','trans_type','Quantity'])
        pd_data['Quantity'] = pd_data['Quantity'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q11 = Query11()
    data = q11.execute()
    print(data)