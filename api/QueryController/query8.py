from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmts ="""SELECT item_dim.item_name, time_dim.quarter, sum(fact_table.quantity)  
            FROM ecomdb_star_schema.fact_table 
            JOIN ecomdb_star_schema.item_dim ON
            item_dim.item_key = fact_table.item_key 
            JOIN ecomdb_star_schema.time_dim ON
            time_dim.time_key = fact_table.time_key
            GROUP BY CUBE (item_dim.item_name, time_dim.quarter)
            ORDER BY  item_dim.item_name, sum(fact_table.quantity) desc"""
        cur.execute(select_stmts)
        records = cur.fetchall()
        worst_season_df = pd.DataFrame(list(records), columns=['Item', 'Quarter', 'Quantity_Sold'])
        worst_season_df = worst_season_df.dropna()
        worst_season_df = worst_season_df.groupby('Item').head(1)
        return worst_season_df.to_dict(orient='records')[:100]

if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)