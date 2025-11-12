#  def_api_calls_db_duplicate_entry***
@app.route('/api_calls_db_duplicate_entry', methods=['GET'])
def api_calls_db_duplicate_entry():
    '''
    Flask Route for the api_calls_db_duplicate_entry Database delete entry
    '''
    route="/api_calls_db_duplicate_entry"
    env.level+='-'
    print('\n'+env.level,white('route api_calls_db_duplicate_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route api_calls_db_duplicate_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        result=sqlite_db_duplicate_entry('api_calls',row)         
        message1="OK done - Entry DUPLICATED"
        image="../static/images/ok.png" 
        message2="entry had been duplicated"
        message3="/api_calls_dashboard"
        message4="api_calls Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
