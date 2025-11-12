import pandas as pd
from sqlalchemy import create_engine
# the csv file is : api_calls.csv
# database will be : api_calls.db
# the table name is  : api_calls
df = pd.read_csv('api_callss.csv', sep=',')
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
engine = create_engine('sqlite:///api_calls.db')
df.to_sql('api_calls', engine) #With this one the table and database must not already exists
#df.to_sql('api_calls', con=engine, if_exists='append')   #with this one you can append data to an existing database
#df.to_sql('api_calls', con=engine, if_exists='replace')   #with this one you can truncat an existing database
