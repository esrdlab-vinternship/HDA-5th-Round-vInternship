from DBconnection.dbconfig import PostgresConnection
import pandas as pd

class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    def execute(self):
        con = PostgresConnection().getConnection()
        curr = con.cursor()
        select_stmts = "SELECT s.store_key , i.item_name, sum(f.quantity) as quantity_sales_for_each_item " \
                       "FROM ecomdb_star_schema.fact_table as f " \
                       "JOIN ecomdb_star_schema.store_dim as s ON s.store_key = f.store_key " \
                       "JOIN ecomdb_star_schema.item_dim as i ON i.item_key = f.item_key " \
                       "GROUP BY CUBE(s.store_key, i.item_name)" \
                       "ORDER BY s.store_key, quantity_sales_for_each_item desc"
        curr.execute(select_stmts)
        records = curr.fetchall()
        top_three_products_sold_df = pd.DataFrame(list(records), columns=['Store', 'Item', 'Quantity'])
        top_three_products_sold_df = top_three_products_sold_df.dropna()
        top_three_products_sold_df = top_three_products_sold_df.groupby('Store').head(3)
        return top_three_products_sold_df.to_dict(orient='records')[:150]

if   __name__   ==   '__main__'  :
    query6 = Query6()
    data = query6.execute()
    print(data)