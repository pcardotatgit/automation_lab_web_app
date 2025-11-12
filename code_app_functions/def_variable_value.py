#  def_variable_value***
def variable_value(name):
    '''
    MODIFIED : 2025-11-04T17:00:20.000Z

    description : return value of the variable in the Database
    
    how to call it : value=variable_value(variable_name)
    '''
    route="/variable_value"
    env.level+='-'
    print('\n'+env.level,white('def variable_value() in app.py : >\n',bold=True))
    loguer(env.level+' def variable_value() in app.py : >')

    # ===================================================================    
    database="variables"        
    table="variables"              
    where_clause=f'where name = "{name}"'
    entry_list=sqlite_db_select_entry(database,table,where_clause)
    value=entry_list[0][3]
    # ===================================================================
    env.level=env.level[:-1]
    return value
    
