#  def_functions_db_ingest_csv***
@app.route('/functions_db_ingest_csv', methods=['GET'])
def functions_db_ingest_csv():
    '''
    Flask Route for the functions_db_ingest_csv Database Update an entry
    '''
    route="/functions_db_ingest_csv"
    env.level+='-'
    print('\n'+env.level,white('route functions_db_ingest_csv() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route functions_db_ingest_csv() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        db_name="functions"
        message1="Message 1 :"
        image="../static/images/toolbox.png"
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_sqlite_ingest_csv"
        page_name="z_sqlite_ingest_csv.html"
        loguer(env.level+' route END OF functions_db_ingest_csv() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name,db_name=db_name) 
