from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query3:
    def _init_(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query3 = """SELECT store_dim.division as "Division", SUM(fact_table.total_price) "Generated_revenue" 
                     FROM ecomdb_schema.fact_table 
                     JOIN ecomdb_schema.store_dim ON
                     store_dim.store_key = fact_table.store_key 
                     WHERE store_dim.division='BARISAL'
                     GROUP BY CUBE(store_dim.division) """
        cur.execute(query3)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'total_sale_price'])
        pd_data['total_sale_price'] = pd_data['total_sale_price'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)