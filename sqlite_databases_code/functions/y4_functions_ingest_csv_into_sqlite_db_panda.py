import pandas as pd
from sqlalchemy import create_engine
# the csv file is : functions.csv
# database will be : functions.db
# the table name is  : functions
df = pd.read_csv('functionss.csv', sep=',')
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
engine = create_engine('sqlite:///functions.db')
df.to_sql('functions', engine) #With this one the table and database must not already exists
#df.to_sql('functions', con=engine, if_exists='append')   #with this one you can append data to an existing database
#df.to_sql('functions', con=engine, if_exists='replace')   #with this one you can truncat an existing database
