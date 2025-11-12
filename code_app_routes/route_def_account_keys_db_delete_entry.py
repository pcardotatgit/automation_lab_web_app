#  def_account_keys_db_delete_entry***
@app.route('/account_keys_db_delete_entry', methods=['GET'])
def account_keys_db_delete_entry():
    '''
    Flask Route for the account_keys_db_delete_entry Database delete entry
    '''
    route="/account_keys_db_delete_entry"
    env.level+='-'
    print('\n'+env.level,white('route account_keys_db_delete_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route account_keys_db_delete_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        result=sqlite_db_delete_entry('account_keys',row)         
        message1="OK done - Entry DELETED"
        image="../static/images/ok.png" 
        message2="entry had been deleted"
        message3="/account_keys_dashboard"
        message4="account_keys Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
