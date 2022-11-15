from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.district, SUM(t.total_price) " \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.store_dim s on s.store_key=t.store_key " \
                      "WHERE s.district='BARISAL' " \
                      "GROUP BY CUBE(s.district) " \
                      "ORDER BY s.district"
        cur.execute(select_stmt)
        records_barisal = cur.fetchall()
        barisal_df = pd.DataFrame(list(records_barisal), columns=['District', 'Sales'])
        barisal_df['Sales'] = barisal_df['Sales'].astype('float64')
        barisal_df = barisal_df.dropna()
        # print(pd_data)
        return barisal_df.to_dict(orient='records')


if __name__ == '__main__':
    query3 = Query3()
    data = query3.execute()
    print(data)