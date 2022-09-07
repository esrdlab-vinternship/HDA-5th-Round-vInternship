from dbconnection.dbcon import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query5 = "SELECT t.year, s.division, SUM(f.total_price) as total_sale_price " \
                 "FROM ecomdb_star_schema.fact_table as f " \
                 "JOIN ecomdb_star_schema.time_dim as t ON t.time_key = f.time_key " \
                 "JOIN ecomdb_star_schema.store_dim as s ON s.store_key = f.store_key " \
                 "WHERE t.year =2015 and s.division = 'BARISAL' " \
                 "GROUP BY CUBE(t.year, s.division)"
        cur.execute(query5)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['year', 'division', 'total_sale_price'])
        pd_data['total_sale_price'] = pd_data['total_sale_price'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q5 = Query5()
    data = q5.execute()
    print(data)
