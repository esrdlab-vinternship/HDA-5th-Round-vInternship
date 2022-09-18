from dbconnection.dbconf import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        # string1 = """SELECT item_dim.item_name
        # FROM star_schema.fact_table
        # JOIN star_schema.item_dim ON item_dim.item_key = fact_table.item_key
        # JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key
        # WHERE time_data.date>(CURRENT_DATE::date - '"""
        # string2=str(self.days)+" days'::interval) AND (trans_dim.trans_type='card' OR trans_dim.trans_type='mobile') GROUP BY item_name"
        insert_stmt = '''SELECT item_dim.item_name
                        FROM star_schema.fact_table
                        JOIN star_schema.item_dim ON item_dim.item_key = fact_table.item_key
                        JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key 
                        WHERE time_data.date > (CURRENT_DATE - integer '{}')'''.format(self.days)
        # insert_stmt = string1+string2
        products_sold = pd.read_sql_query(insert_stmt, con)
        # cur.execute(insert_stmt)
        # result = cur.fetchall()
        # pd_data = pd.DataFrame(list(result), columns=['item_name'])
        products_sold = products_sold.dropna()
        # print(products_sold)
        # products_sold = products_sold.values
        # return pd_data['item_name'].tolist()
        dict = {"items": products_sold['item_name'].tolist()}
        return dict
        # return products_sold.tolist()


if __name__ == '__main__':
    query7 = Query7()
    result = query7.execute()
    print(result)
