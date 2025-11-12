#  def_machin_db_update_entry***
@app.route('/machin_db_update_entry', methods=['GET'])
def machin_db_update_entry():
    '''
    Flask Route for the machin_db_update_entry Database Update an entry
    '''
    route="/machin_db_update_entry"
    env.level+='-'
    print('\n'+env.level,white('route machin_db_update_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route machin_db_update_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        premier=request.args.get('premier')
        print('\npremier : ',premier)
        deuxieme=request.args.get('deuxieme')
        print('\ndeuxieme : ',deuxieme)
        troisieme=request.args.get('troisieme')
        print('\ntroisieme : ',troisieme)
        quatrieme=request.args.get('quatrieme')
        print('\nquatrieme : ',quatrieme)
        with open('./sqlite_databases_code/machin/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        db_name = "machin.db"
        table_name = db_details_dict["table_name"]
        where_clause='`index` = '+row
        sql_fields=['index','premier','deuxieme','troisieme','quatrieme']
        sql_data_list=[int(row),premier,deuxieme,troisieme,quatrieme]
        result=sqlite_db_update_entry(db_name,table_name,where_clause,sql_fields,sql_data_list)
        message1="OK done"
        image="../static/images/ok.png"
        message2="entry had been updated"
        message3="/machin_dashboard"
        message4="machin Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
        