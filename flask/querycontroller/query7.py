
from dbconnection.dbcon import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        self.con = PostgresConnection().getConnection()
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        s1 = '''SELECT i.item_name 
                            FROM ecomdb_star_schema.fact_table f
                            JOIN ecomdb_star_schema.item_dim AS i ON i.item_key=f.item_key 
                            JOIN ecomdb_star_schema.time_dim t ON t.time_key=f.time_key
                            WHERE t.date>(CURRENT_DATE - integer '{}')'''.format(self.days)

        cur.execute(s1)
        result = cur.fetchall()
        card = pd.DataFrame(list(result), columns=['item_name'])
        # card['sales']=card['sales'].astype('float64')
        card = card.dropna()
        return card.to_dict(orient='records')


if __name__ == '__main__':
    q7 = Query7(days=400)
    data = q7.execute()
    print(data)
