from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT t.year, s.district, SUM(f.total_price) as total_sale_price " \
                      "FROM ecomdb_star_schema.fact_table as f " \
                      "JOIN ecomdb_star_schema.time_dim as t ON t.time_key = f.time_key " \
                      "JOIN ecomdb_star_schema.store_dim as s ON s.store_key = f.store_key " \
                      "WHERE t.year = 2015 and s.district = 'BARISAL' " \
                      "GROUP BY CUBE(t.year, s.district)"
        cur.execute(select_stmt)
        records = cur.fetchall()
        barisal_2015_df = pd.DataFrame(list(records), columns=['Year', 'District', 'Sales'])
        barisal_2015_df =  barisal_2015_df.dropna()
        return barisal_2015_df.to_dict(orient='records')

if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)