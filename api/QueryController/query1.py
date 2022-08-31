from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.division, SUM(t.total_price) " \
              "FROM star.fact_table t " \
              "JOIN star.store_dim s on s.store_key=t.store_key " \
                "JOIN star.time_dim tim on tim.time_key=t.time_key " \
                "WHERE tim.month=12 " \
                "GROUP BY CUBE (s.division) "\
                "ORDER BY s.division "

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query1 = Query1()
    data = query1.execute()
    print(data)
