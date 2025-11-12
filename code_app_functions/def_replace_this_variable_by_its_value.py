#  def_replace_this_variable_by_its_value***
def replace_this_variable_by_its_value(objet):
    '''
    MODIFIED : 2025-11-03T22:47:34.000Z

    description : replace every variables in the object by their values
    
    how to call it :
    '''
    route="/replace_this_variable_by_its_value"
    env.level+='-'
    print('\n'+env.level,white('def replace_this_variable_by_its_value() in app.py : >\n',bold=True))
    loguer(env.level+' def replace_this_variable_by_its_value() in app.py : >')
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
        print(cyan(item[1],bold=True))
        if objet==item[1]:
            print(green('OK Match => '+item[3],bold=True))
            objet=item[3]
            break
    # ===================================================================
    loguer(env.level+' def END OF replace_this_variable_by_its_value() in app.py : >')    
    env.level=env.level[:-1]
    return objet
    
