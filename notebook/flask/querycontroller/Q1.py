from dbconnection.dbconf import PostgresConnection
import pandas as pd

class Query1():
    def __init__(self):
        self.con = PostgresConnection().getConnection()
    def execute(self):

# Total Price By Division
        con = PostgresConnection().getConnection()
        insert_stmt = """SELECT store_dim.division, SUM(fact_table.total_price)  as sales 
            FROM star_schema.fact_table 
            JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key 
            GROUP BY CUBE(store_dim.division) 
            ORDER BY store_dim.division"""
        cur = con.cursor()
        # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        total_price_by_division = pd.read_sql_query(insert_stmt, con)
        total_price_by_divisions = total_price_by_division.dropna()
        return total_price_by_divisions.to_dict(orient='records')

# Total Price By District
        # con = PostgresConnection().getConnection()
        # insert_stmt = """SELECT store_dim.district as "District", SUM(fact_table.total_price) "Total Sale Price" 
        #     FROM star_schema.fact_table 
        #     JOIN star_schema.store_dim ON store_dim.store_key = fact_table.store_key 
        #     GROUP BY CUBE(store_dim.district) 
        #     ORDER BY store_dim.district"""
        # cur = con.cursor()
        # # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        # total_price_by_district = pd.read_sql_query(insert_stmt, con)
        # total_price_by_districts = total_price_by_district.dropna()
        # return total_price_by_districts.to_dict(orient='records')

# Total Price By Year
        # con = PostgresConnection().getConnection()
        # insert_stmt = """SELECT time_data.year as "Year", SUM(fact_table.total_price) "Total Sale Price"
        # FROM star_schema.fact_table
        # JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key
        # GROUP BY CUBE(time_data.year)
        # ORDER BY time_data.year"""
        # cur = con.cursor()
        # # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        # total_price_by_year = pd.read_sql_query(insert_stmt, con)
        # total_price_by_years = total_price_by_year.dropna()
        # return total_price_by_years.to_dict(orient='records')

# Total Price By Month
        # con = PostgresConnection().getConnection()
        # insert_stmt = """SELECT time_data.month as "Month", SUM(fact_table.total_price) "Total Sale Price"
        # FROM star_schema.fact_table
        # JOIN star_schema.time_data ON time_data.time_key = fact_table.time_key
        # GROUP BY CUBE(time_data.month)
        # ORDER BY time_data.month"""
        # cur = con.cursor()
        # # psycopg2.extras.execute_batch(cur, insert_stmt, fact_data.values)
        # total_price_by_month = pd.read_sql_query(insert_stmt, con)
        # total_price_by_months = total_price_by_month.dropna()
        # return total_price_by_months.to_dict(orient='records')

if __name__ == '__main__':
    query1 = Query1()
    result = query1.execute()
    print(result)