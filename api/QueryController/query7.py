<<<<<<< HEAD
from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''SELECT i.item_name
                    FROM ecomdb_star_schema.fact_table AS f 
                    JOIN ecomdb_star_schema.item_dim AS i ON i.item_key=f.item_key 
                    JOIN ecomdb_star_schema.time_dim AS t ON t.time_key = f.time_key 
                    Where t.date > (CURRENT_DATE - integer '{}')'''.format(self.days)
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item Name'])
        pd_data = pd_data.dropna()
        return pd_data['Item Name'].tolist()


if __name__ == '__main__':
    query7 = Query7(days=350)
    data = query7.execute()
    print(data)

=======
from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''SELECT i.item_name
                    FROM ecomdb_star_schema.fact_table AS f 
                    JOIN ecomdb_star_schema.item_dim AS i ON i.item_key=f.item_key 
                    JOIN ecomdb_star_schema.time_dim AS t ON t.time_key = f.time_key 
                    Where t.date > (CURRENT_DATE - integer '{}')'''.format(self.days)
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item Name'])
        pd_data = pd_data.dropna()
        return pd_data['Item Name'].tolist()


if __name__ == '__main__':
    query7 = Query7(days=350)
    data = query7.execute()
    print(data)

>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42