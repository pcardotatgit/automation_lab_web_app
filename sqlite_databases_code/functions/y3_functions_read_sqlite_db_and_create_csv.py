import pandas as pd
import sqlalchemy
from pandas import DataFrame
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
db_name = "functions.db"
table_name = "functions"
engine = sqlalchemy.create_engine("sqlite:///%s" % db_name, execution_options={"sqlite_raw_colnames": True})
df = pd.read_sql_table(table_name, engine)
out_df = df[['name','environment_name','description','called_function','input_variables','output_variables','comment']]
#save result to csv file
out_df.to_csv(r'functions.csv')
df = DataFrame(out_df)
print (df)
print('=========================================')
print('DONE')
            