import psycopg2
import configparser
import os
import pandas as pd
import glob


config = configparser.ConfigParser()
config.read("module-8-project/config.ini")

csv_path_pattern = config["Files"]["csv_path"]

csv_files = glob.glob(csv_path_pattern)

sales_df_list = []
for file in csv_files:
    df = pd.read_csv(file)
    sales_df_list.append(df)
    os.remove(file)

if sales_df_list:
    sales_df = pd.concat(sales_df_list, ignore_index=True)
else:
    sales_df = pd.DataFrame()  # Empty DataFrame if no CSV files found

print(sales_df)


class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.conn = psycopg2.connect(
            host=host, database=database, user=user, password=password
        )

        self.cur = self.conn.cursor()

        self.conn.autocommit = True

    def post(self, query, args=()):
        try:
            self.cur.execute(query, args)
        except Exception as er:
            print(repr(er))


database_creds = config["Database"]

database = Database(
    host=database_creds["HOST"],
    database=database_creds["DATABASE"],
    user=database_creds["USER"],
    password=database_creds["PASSWORD"],
)

for i, row in sales_df.iterrows():
    query = f"insert into sales values ('{row['doc_id']}', '{row['item']}', '{row['category']}', {row['amount']}, {row['price']}, {row['discount']})"
    database.post(query)
