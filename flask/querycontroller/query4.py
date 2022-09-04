from dbconnection.dbcon import PostgresConnection
import pandas as pd
class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query4 = "SELECT tim.year, SUM(t.total_price) " \
              "FROM ecomdb_star_schema.fact_table t " \
              "JOIN ecomdb_star_schema.store_dim s on s.store_key=t.store_key " \
                "JOIN ecomdb_star_schema.time_dim tim on tim.time_key=t.time_key " \
                "WHERE tim.year='2015' " \
                "GROUP BY CUBE(tim.year) " \
                "ORDER BY tim.year"
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