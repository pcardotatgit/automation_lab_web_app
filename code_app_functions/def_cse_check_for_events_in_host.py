#  def_cse_check_for_events_in_host***
def cse_check_for_events_in_host(events,guid,event_id_list):
    '''
    MODIFIED : 2025-11-04T16:11:33.000Z

    description : check if events name are in the last CSE event for the selected host
    
    how to call it :
    '''
    route="/cse_check_for_events_in_host"
    env.level+='-'
    print('\n'+env.level,white('def cse_check_for_events_in_host() in app.py : >\n',bold=True))
    loguer(env.level+' def cse_check_for_events_in_host() in app.py : >')
    # ===================================================================    
    print('event_id_list : ',cyan(event_id_list,bold=True))
    print('guid : ',cyan(guid,bold=True))
    print()
    events_in_json=json.loads(events)
    #print('events_in_json : \n',yellow(events_in_json,bold=True))
    data=events_in_json['data']
    #print('data : \n',cyan(data,bold=True))
    host_events={}
    index=0
    for event in data:
        print('\nevent_type_id : \n',yellow(event["event_type_id"],bold=True))
        print('\nconnector_guid : \n',yellow(event["connector_guid"],bold=True))
        if event["connector_guid"]==guid and str(event["event_type_id"]) in event_id_list:
            print(red('OK'))
            host_events[index]=event
            index+=1
    step_output="nb_of_events_on_victim_machine"
    variables_sqlite_update_value(step_output,str(index))
    #print(cyan(host_events,bold=True))
    # ===================================================================
    loguer(env.level+' def END OF cse_check_for_events_in_host() in app.py : >')    
    env.level=env.level[:-1]
    return host_events
    
