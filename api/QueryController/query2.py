from DBconnection.dbconfig import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        insert_stmts = "SELECT trans_dim.trans_type, SUM(fact_table.total_price) " \
                       "FROM ecomdb_star_schema.fact_table " \
                       "JOIN ecomdb_star_schema.customer_dim on customer_dim.customer_key=fact_table.customer_key " \
                       "JOIN ecomdb_star_schema.trans_dim on trans_dim.payment_key=fact_table.payment_key " \
                       "GROUP BY CUBE (trans_dim.trans_type) " \
                       "ORDER BY trans_dim.trans_type"
        cur.execute(insert_stmts)
        records_type = cur.fetchall()
        type_df = pd.DataFrame(list(records_type), columns=['Type', 'Sales'])
        type_df = type_df.dropna()
        # print(pd_data)
        return type_df.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    print(data)