#  def_cse_get_computer***
@app.route('/cse_get_computer', methods=['GET'])
def cse_get_computer():
    '''
    Created : 2025-10-25T14:03:52.000Z
    description : STEP 1 Get computers
    '''
    route="/cse_get_computer"
    env.level+='-'
    print('\n'+env.level,white('route cse_get_computer() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route cse_get_computer() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        database="api_calls"
        print("\ndatabase : ",database)
        table="api_calls"
        print("\ntable : ",table)
        name='Secure Endpoint Get Computers'
        where_clause=f'where `name` = "{name}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)
        name=entry_list[0][1]
        base_url=entry_list[0][2]
        relative_url=entry_list[0][3]
        api_docummentation=entry_list[0][4]
        method=entry_list[0][5]
        short_description=entry_list[0][6]
        payload=entry_list[0][7]
        header=entry_list[0][8]
        body=entry_list[0][9]
        params=entry_list[0][10]
        parameters=entry_list[0][11]
        authentication_profile=entry_list[0][12]
        inputs=entry_list[0][13]
        outputs=entry_list[0][14]
        image="../static/images/toolbox.png"
        PAGE_DESTINATION="z_cse_get_computer"
        page_name="z_cse_get_computer.html"
        loguer(env.level+' route END OF cse_get_computer() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,image=image,page_name=page_name,name=name,base_url=base_url,relative_url=relative_url,api_docummentation=api_docummentation,method=method,short_description=short_description,payload=payload,header=header,body=body,params=params,parameters=parameters,authentication_profile=authentication_profile)
        
