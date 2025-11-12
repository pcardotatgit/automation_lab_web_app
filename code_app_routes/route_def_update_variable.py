#  def_update_variable***
@app.route('/update_variable', methods=['GET'])
def update_variable():
    '''
    Created : 2025-11-04T17:31:37.000Z

    description : display selected variable details formular for update
    '''
    route="/update_variable"
    env.level+='-'
    print('\n'+env.level,white('route update_variable() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route update_variable() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # GET variable from calling web page
        name=request.args.get("name")
        print("\nname : ",name)
        database="variables"
        print("\ndatabase : ",database)
        table="variables"
        print("\ntable : ",table)
        where_clause=f'where name = "{name}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)
        row=entry_list[0][0]
        print("\nrow : ",row)        
        name=entry_list[0][1]
        print("\nname : ",name)         
        environment_name=entry_list[0][2]
        print("\nenvironment_name : ",environment_name)
        value=entry_list[0][3]
        print("\nvalue : ",value)
        description=entry_list[0][4]
        print("\ndescription : ",description)
        comment=entry_list[0][5]
        print("\ncomment : ",comment)
        comment=entry_list[0][6]
        PAGE_DESTINATION="z_update_variable"
        page_name="z_update_variable.html"    
        loguer(env.level+' route END OF update_variable() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,
        page_name=page_name,row=row,name=name,environment_name=environment_name,value=value,description=description,comment=comment)
        
