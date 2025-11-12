#  def_cse_id_of_event_type_name***
def cse_id_of_event_type_name(event_name):
    '''
    MODIFIED : 2025-11-03T09:54:03.000Z

    description : Send CSE Get event type id API call and parse ID of the event type name give as input
    
    how to call it :
    '''
    route="/cse_id_of_event_type_name"
    env.level+='-'
    print('\n'+env.level,white('def cse_id_of_event_type_name() in app.py : >\n',bold=True))
    loguer(env.level+' def cse_id_of_event_type_name() in app.py : >')
    # ===================================================================    
    api_call_name="Secure Endpoint Get Event Types"
    # GET variable from calling web page
    row=request.args.get("row")
    print("\nrow : ",row)
    database="api_calls"
    print("\ndatabase : ",database)
    table="api_calls"
    print("\ntable : ",table)
    where_clause=f' where name = "{api_call_name}"'
    entry_list=sqlite_db_select_entry(database,table,where_clause)
    print("\nentry_list : \n",entry_list)
    result,json_txt_result=select_api_call_and_send_it(api_call_name)
    result_dict=json.loads(json_txt_result)
    #print(cyan(result_dict,bold=True))
    all_events=result_dict['data']
    event_id="xxxxxx"
    for item in all_events:
        print('\n',yellow(item,bold=True))
        if item['name']==event_name:
            event_id=str(item['id'])
    print('event_id : ',green(event_id,bold=True))
    # ===================================================================
    loguer(env.level+' def END OF cse_id_of_event_type_name() in app.py : >')    
    env.level=env.level[:-1]
    return event_id
    
