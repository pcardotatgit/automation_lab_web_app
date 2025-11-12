#  def_account_keys_db_add_entry***
@app.route('/account_keys_db_add_entry', methods=['GET'])
def account_keys_db_add_entry():
    '''
    Flask Route for the account_keys_db_add_entry Database Update an entry
    '''
    route="/account_keys_db_add_entry"
    env.level+='-'
    print('\n'+env.level,white('route account_keys_db_add_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route account_keys_db_add_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        db_name = "account_keys.db"
        column_list=['name','type','username','password','key','comment']
        print('\ncolumn_list :',cyan(column_list,bold=True))
        index=sqlite_db_get_last_index('account_keys')
        index+=1        
        print('index : ',index)
        PAGE_DESTINATION="z_sqlite_db_add_entry"
        page_name="z_sqlite_db_add_entry.html"
        db_name=db_name.split('.')[0]
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,column_list=column_list,index=index,db_name=db_name)
 
