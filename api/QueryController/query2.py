from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = """SELECT customer_dim.name as "name", SUM(fact_table.total_price) "sales"
FROM star.fact_table
JOIN star.customer_dim ON
customer_dim.customer_key = fact_table.customer_key
GROUP BY CUBE(customer_dim.name)
ORDER BY customer_dim.name"""
        cur.execute(query)
        result = cur.fetchall()[10]
        pd_data = pd.DataFrame(list(result), columns=['customer', 'sales'])
        pd_data['sales'][10]= pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    print(data)
