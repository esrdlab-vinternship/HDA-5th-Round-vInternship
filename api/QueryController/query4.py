from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT time_dim.year as "year", SUM(fact_table.total_price) "sales"
FROM star.fact_table
JOIN star.time_dim ON
time_dim.time_key = fact_table.time_key
WHERE time_dim.year='2015'
GROUP BY time_dim.year
"""

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query4 = Query4()
    data = query4.execute()
    print(data)
