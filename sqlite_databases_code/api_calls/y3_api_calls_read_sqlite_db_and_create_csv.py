import pandas as pd
import sqlalchemy
from pandas import DataFrame
# sqlite:///:memory: (or, sqlite://)
# sqlite:///relative/path/to/file.db
# sqlite:////absolute/path/to/file.db
db_name = "api_calls.db"
table_name = "api_calls"
engine = sqlalchemy.create_engine("sqlite:///%s" % db_name, execution_options={"sqlite_raw_colnames": True})
df = pd.read_sql_table(table_name, engine)
out_df = df[['name','fqdn','relative_url','documentation','method','description','payload','header','body','query_params','custom_variables','authentication_profile','inputs_variables','output_variables']]
#save result to csv file
out_df.to_csv(r'api_calls.csv')
df = DataFrame(out_df)
print (df)
print('=========================================')
print('DONE')
            