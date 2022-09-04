
from dbconnection.dbcon import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        x = input('Enter number of days: ')

        con = PostgresConnection().getConnection()
        cur = con.cursor()
        s1 = '''SELECT i.item_name,tim.date,tt.trans_type 
                            FROM ecomdb_star_schema.fact_table ft 
                            JOIN ecomdb_star_schema.item_dim i ON i.item_key=ft.item_key 
                            JOIN ecomdb_star_schema.trans_dim tt ON tt.payment_key=ft.payment_key 
                            JOIN ecomdb_star_schema.time_dim tim ON tim.time_key=ft.time_key
                            WHERE tim.date>(CURRENT_DATE::date -'
                            '''
        s2 = str(x) + " days'::interval) AND tt.trans_type='card'"

        select_stmt_card = s1 + s2
        cur.execute(select_stmt_card)
        records_card = cur.fetchall()
        card = pd.DataFrame(list(records_card), columns=['item_name', 'date', 'trans_type'])
        card
        return card.to_dict(orient='records')


if __name__ == '__main__':
    q7 = Query7()
    data = q7.execute()
    print(data)
