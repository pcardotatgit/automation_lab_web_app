import pandas as pd
from sqlalchemy import create_engine
# the csv file is : account_keys.csv
# database will be : account_keys.db
# the table name is  : account_keys
df = pd.read_csv('account_keyss.csv', sep=',')
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
engine = create_engine('sqlite:///account_keys.db')
df.to_sql('account_keys', engine) #With this one the table and database must not already exists
#df.to_sql('account_keys', con=engine, if_exists='append')   #with this one you can append data to an existing database
#df.to_sql('account_keys', con=engine, if_exists='replace')   #with this one you can truncat an existing database
