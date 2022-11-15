from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmts = """SELECT item_dim.item_name,store_dim.division,SUM(fact_table.quantity)  
        FROM ecomdb_star_schema.fact_table 
        JOIN ecomdb_star_schema.store_dim ON
        store_dim.store_key = fact_table.store_key
        JOIN ecomdb_star_schema.item_dim ON
        item_dim.item_key = fact_table.item_key
        GROUP BY CUBE (store_dim.division,item_dim.item_name)
        ORDER BY item_dim.item_name,store_dim.division """
        # BY ()cur = con.cursor()
        cur.execute(select_stmts)
        records = cur.fetchall()
        item_div_df = pd.DataFrame(list(records), columns=['Item', 'Division', 'Sales'])
        item_div_df = item_div_df.dropna()
        return item_div_df.to_dict(orient='records')[:140]

if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    print(data)