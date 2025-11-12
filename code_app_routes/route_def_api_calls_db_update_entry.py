#  def_api_calls_db_update_entry***
@app.route('/api_calls_db_update_entry', methods=['GET'])
def api_calls_db_update_entry():
    '''
    Flask Route for the api_calls_db_update_entry Database Update an entry
    '''
    route="/api_calls_db_update_entry"
    env.level+='-'
    print('\n'+env.level,white('route api_calls_db_update_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route api_calls_db_update_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        name=request.args.get('name')
        print('\nname : ',name)
        fqdn=request.args.get('fqdn')
        print('\nfqdn : ',fqdn)
        relative_url=request.args.get('relative_url')
        print('\nrelative_url : ',relative_url)
        documentation=request.args.get('documentation')
        print('\ndocumentation : ',documentation)
        method=request.args.get('method')
        print('\nmethod : ',method)
        description=request.args.get('description')
        print('\ndescription : ',description)
        payload=request.args.get('payload')
        print('\npayload : ',payload)
        header=request.args.get('header')
        print('\nheader : ',header)
        body=request.args.get('body')
        print('\nbody : ',body)
        query_params=request.args.get('query_params')
        print('\nquery_params : ',query_params)
        custom_variables=request.args.get('custom_variables')
        print('\ncustom_variables : ',custom_variables)
        authentication_profile=request.args.get('authentication_profile')
        print('\nauthentication_profile : ',authentication_profile)
        inputs_variables=request.args.get('inputs_variables')
        print('\ninputs_variables : ',inputs_variables)
        output_variables=request.args.get('output_variables')
        print('\noutput_variables : ',output_variables)
        with open('./sqlite_databases_code/api_calls/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))        
        db_name = "api_calls.db"
        table_name = db_details_dict["table_name"]
        where_clause='`index` = '+row
        sql_fields=['index','name','fqdn','relative_url','documentation','method','description','payload','header','body','query_params','custom_variables','authentication_profile','inputs_variables','output_variables']
        sql_data_list=[int(row),name,fqdn,relative_url,documentation,method,description,payload,header,body,query_params,custom_variables,authentication_profile,inputs_variables,output_variables]
        result=sqlite_db_update_entry(db_name,table_name,where_clause,sql_fields,sql_data_list)        
        message1="OK done"
        image="../static/images/ok.png" 
        message2="entry had been updated"
        message3="/api_calls_dashboard"
        message4="api_calls Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
