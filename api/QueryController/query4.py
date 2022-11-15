from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT tim.year, SUM(t.total_price) " \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.time_dim tim on tim.time_key=t.time_key " \
                      "WHERE tim.year=2015  " \
                      "GROUP BY CUBE(tim.year) " \
                      "ORDER BY tim.year"
        cur.execute(select_stmt)
        records = cur.fetchall()
        y2015_df = pd.DataFrame(list(records), columns=['Year', 'Sales'])
        y2015_df = y2015_df.dropna()
        # print(pd_data)
        return y2015_df.to_dict(orient='records')


if __name__ == '__main__':
    query4 = Query4()
    data = query4.execute()
    print(data)