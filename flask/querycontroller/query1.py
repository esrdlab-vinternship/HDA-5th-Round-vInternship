
from dbconnection.dbcon import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.division, SUM(t.total_price) " \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.store_dim s on s.store_key=t.store_key " \
                      "JOIN ecomdb_star_schema.time_dim tim on tim.time_key=t.time_key " \
                      "WHERE tim.month=12 " \
                      "GROUP BY CUBE (s.division) " \
                      "ORDER BY s.division "
        cur.execute(select_stmt)
        records = cur.fetchall()
        df = pd.DataFrame(list(records), columns=['division', 'sales'])
        df = df.dropna()
        df
        return df.to_dict(orient='records')


if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)
