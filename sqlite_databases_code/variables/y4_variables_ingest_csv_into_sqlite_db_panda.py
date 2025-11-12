import pandas as pd
from sqlalchemy import create_engine
# the csv file is : variables.csv
# database will be : variables.db
# the table name is  : variables
df = pd.read_csv('variabless.csv', sep=',')
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
engine = create_engine('sqlite:///variables.db')
df.to_sql('variables', engine) #With this one the table and database must not already exists
#df.to_sql('variables', con=engine, if_exists='append')   #with this one you can append data to an existing database
#df.to_sql('variables', con=engine, if_exists='replace')   #with this one you can truncat an existing database
