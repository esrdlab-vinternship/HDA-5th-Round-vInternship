from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query4:
    def _init_(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query4 = """SELECT time_dim.year,SUM(fact_table.total_price) 
FROM ecomdb_schema.fact_table 
JOIN ecomdb_schema.time_dim ON
time_dim.time_key = fact_table.time_key 
WHERE time_dim.year=2015
GROUP BY CUBE(time_dim.year) """
        cur.execute(query4)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['year', 'total_sale_price'])
        pd_data['total_sale_price'] = pd_data['total_sale_price'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q4 = Query4()
    data = q4.execute()
    print(data)