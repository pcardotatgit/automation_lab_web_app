#  def_replace_variable***
def replace_variable(objet):
    '''
    MODIFIED : 2025-11-03T22:47:34.000Z

    description : replace every variables in the object by their values
    
    how to call it :
    '''
    route="/replace_variable"
    env.level+='-'
    print('\n'+env.level,white('def replace_variable() in app.py : >\n',bold=True))
    loguer(env.level+' def replace_variable() in app.py : >')
    # ===================================================================    
    # Variables
    db_name = "variables.db"
    table_name = "variables"
    engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
    df = pd.read_sql_table(table_name, engine)
    out_df = df[['index','name','environment_name','value','description','comment','used_by']]
    df = DataFrame(out_df)
    #print (df)
    res = df.values.tolist()
    variables_dict={}
    for item in res:
        #print(item)
        objet=objet.replace('$'+item[1],item[3])
    # ===================================================================
    loguer(env.level+' def END OF replace_variable() in app.py : >')    
    env.level=env.level[:-1]
    return objet
    
