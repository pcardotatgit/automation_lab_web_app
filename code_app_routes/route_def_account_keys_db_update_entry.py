#  def_account_keys_db_update_entry***
@app.route('/account_keys_db_update_entry', methods=['GET'])
def account_keys_db_update_entry():
    '''
    Flask Route for the account_keys_db_update_entry Database Update an entry
    '''
    route="/account_keys_db_update_entry"
    env.level+='-'
    print('\n'+env.level,white('route account_keys_db_update_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route account_keys_db_update_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        name=request.args.get('name')
        print('\nname : ',name)
        type=request.args.get('type')
        print('\ntype : ',type)
        username=request.args.get('username')
        print('\nusername : ',username)
        password=request.args.get('password')
        print('\npassword : ',password)
        key=request.args.get('key')
        print('\nkey : ',key)
        comment=request.args.get('comment')
        print('\ncomment : ',comment)
        with open('./sqlite_databases_code/account_keys/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))        
        db_name = "account_keys.db"
        table_name = db_details_dict["table_name"]
        where_clause='`index` = '+row
        sql_fields=['index','name','type','username','password','key','comment']
        sql_data_list=[int(row),name,type,username,password,key,comment]
        result=sqlite_db_update_entry(db_name,table_name,where_clause,sql_fields,sql_data_list)        
        message1="OK done"
        image="../static/images/ok.png" 
        message2="entry had been updated"
        message3="/account_keys_dashboard"
        message4="account_keys Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
