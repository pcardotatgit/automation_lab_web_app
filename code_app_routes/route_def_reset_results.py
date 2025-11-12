#  def_reset_results***
@app.route('/reset_results', methods=['GET'])
def reset_results():
    '''
    Created : 2025-11-09

    description : reset every challenge results
    '''
    route="/reset_results"
    env.level+='-'
    print('\n'+env.level,white('route reset_results() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route reset_results() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        hostname=''
        variables_sqlite_update_value('victim_hostname',hostname)
        guid=''
        variables_sqlite_update_value('GUID',guid)
        host_ip=''
        variables_sqlite_update_value('infected_machine_internal_ip_address',host_ip)
        internal_ip_1=''
        variables_sqlite_update_value('internal_infected_ip_address_1',internal_ip_1)        
        internal_ip_2=''
        variables_sqlite_update_value('internal_infected_ip_address_2',internal_ip_2)
        internal_ip_3=''
        variables_sqlite_update_value('internal_infected_ip_address_3',internal_ip_3)
        sha256=''
        variables_sqlite_update_value('CSE_malicious_file_sha256',sha256)
        domain=''
        variables_sqlite_update_value('domain',domain)
        executed_malware_id=''
        variables_sqlite_update_value('CSE_Executed_Malware_event_type_ID',executed_malware_id)
        threat_detected_id=''
        variables_sqlite_update_value('CSE_Threat_Detected_event_type_ID',threat_detected_id)
        sha256_submission=''
        variables_sqlite_update_value('sha256_submission',sha256_submission)
        nb_events=''
        variables_sqlite_update_value('nb_of_events_on_victim_machine',nb_events)
        filename=''
        variables_sqlite_update_value('CSE_malicious_file_name',filename)
        CSE_Events=''
        variables_sqlite_update_value('CSE_Events',CSE_Events)        
        CSE_host_events=''
        variables_sqlite_update_value('CSE_host_events',CSE_host_events)         
        CSE_result_of_get_computers=''
        variables_sqlite_update_value('CSE_result_of_get_computers',CSE_result_of_get_computers)         
        Malware_Analytics_result_of_search_submission=''
        variables_sqlite_update_value('Malware_Analytics_result_of_search_submission',Malware_Analytics_result_of_search_submission)    
        umbrella_json_result_of_api_token_request=''
        variables_sqlite_update_value('umbrella_json_result_of_api_token_request',umbrella_json_result_of_api_token_request)
        umbrella_v2_api_token=''
        variables_sqlite_update_value('umbrella_v2_api_token',umbrella_v2_api_token)
        umbrella_result_of_get_dns_activity=''
        variables_sqlite_update_value('umbrella_result_of_get_dns_activity',umbrella_result_of_get_dns_activity)
        malicious_domain_ip=''
        variables_sqlite_update_value('malicious_domain_ip',malicious_domain_ip)
        XDR_Token=''        
        variables_sqlite_update_value('XDR_Token',XDR_Token)
        observable_payload_for_xdr_response_actions=''
        variables_sqlite_update_value('observable_payload_for_xdr_response_actions',observable_payload_for_xdr_response_actions)
        observable_value='192.168.128.156'
        variables_sqlite_update_value('observable_value',observable_value)
        observable_type='ip'
        variables_sqlite_update_value('observable_type',observable_type)       
        module_instance_id=''
        variables_sqlite_update_value('module_instance_id',module_instance_id)        
        action_id=''
        variables_sqlite_update_value('action_id',action_id)     

        internal_ip_1_isolation_status="NO"
        variables_sqlite_update_value('internal_ip_1_isolation_status',internal_ip_1_isolation_status)
        internal_ip_2_isolation_status="NO"
        variables_sqlite_update_value('internal_ip_2_isolation_status',internal_ip_2_isolation_status)
        internal_ip_3_isolation_status="NO"
        variables_sqlite_update_value('internal_ip_3_isolation_status',internal_ip_3_isolation_status)
        host_ip_isolation_status="NO"
        variables_sqlite_update_value('host_ip_isolation_status',host_ip_isolation_status)
        guid_isolation_status="NO"
        variables_sqlite_update_value('guid_isolation_status',guid_isolation_status)
        hostname_ip_isolation_status="NO"
        variables_sqlite_update_value('hostname_ip_isolation_status',hostname_ip_isolation_status)
        sha256_isolation_status="NO"
        variables_sqlite_update_value('sha256_isolation_status',sha256_isolation_status)
        filename_isolation_status="NO"
        variables_sqlite_update_value('filename_isolation_status',filename_isolation_status)
        malicious_domain_ip_isolation_status="NO"
        variables_sqlite_update_value('malicious_domain_ip_isolation_status',malicious_domain_ip_isolation_status)
        domain_isolation_status="NO"
        variables_sqlite_update_value('domain_isolation_status',domain_isolation_status)
        victim_hostname_isolation_status="NO"
        variables_sqlite_update_value('victim_hostname_isolation_status',victim_hostname_isolation_status)       
        variables_sqlite_update_value('domain','')  
        variables_sqlite_update_value('Malware_Analytics_sample_ID','')    
        variables_sqlite_update_value('Threat_Detected_Event_Type_ID','')     
        variables_sqlite_update_value('umbrella_investigate_api_key','')        
        variables_sqlite_update_value('malware_analytics_api_key','')
        variables_sqlite_update_value('Umbrella_client_id','')
        variables_sqlite_update_value('Umbrella_client_secret','')
        variables_sqlite_update_value('MA_result_of_get_domain','')
        variables_sqlite_update_value('temp','')
        variables_sqlite_update_value('XDR_client_id','')
        variables_sqlite_update_value('XDR_client_password','')
        variables_sqlite_update_value('observable_value','192.168.128.156')
        variables_sqlite_update_value('observable_type','ip')
        variables_sqlite_update_value('Threat_Detected_Event_Type_ID','')
        variables_sqlite_update_value('API_Call_Result','')          
        variables_sqlite_update_value('JSON_FOR_VARIABLE_RESPONSE_ACTION_FOR_CSE','{"module_instance_id":"","action_id":""}')
        variables_sqlite_update_value('JSON_FOR_VARIABLE_RESPONSE_ACTION_FOR_FIREWALLs','{"module_instance_id":"","action_id":""}')
        variables_sqlite_update_value('JSON_FOR_VARIABLE_RESPONSE_ACTION_FOR_HOSTNAME','{"module_instance_id":"","action_id":""}')
        variables_sqlite_update_value('JSON_FOR_VARIABLE_RESPONSE_ACTION_FOR_ISE','{"module_instance_id":"","action_id":""}')
        variables_sqlite_update_value('JSON_FOR_VARIABLE_RESPONSE_ACTION_FOR_UMBRELLA','{"module_instance_id":"","action_id":""}')
        
        with open('./templates/isolation_status.txt','w') as file2:
            file2.write('0')         
        PAGE_DESTINATION="z_challenge_result"
        page_name="z_challenge_result.html"
        loguer(env.level+' route END OF reset_results() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,hostname=hostname,
            host_ip=host_ip,internal_ip_2=internal_ip_2,internal_ip_3=internal_ip_3,sha256=sha256,domain=domain,executed_malware_id=executed_malware_id,
            threat_detected_id=threat_detected_id,sha256_submission=sha256_submission,guid=guid,nb_events=nb_events,internal_ip_1_isolation_status=internal_ip_1_isolation_status,
            internal_ip_2_isolation_status=internal_ip_2_isolation_status,internal_ip_3_isolation_status=internal_ip_3_isolation_status,host_ip_isolation_status=host_ip_isolation_status,
            sha256_isolation_status=sha256_isolation_status,malicious_domain_ip_isolation_status=malicious_domain_ip_isolation_status,domain_isolation_status=domain_isolation_status,
            filename_isolation_status=filename_isolation_status,victim_hostname_isolation_status=victim_hostname_isolation_status,guid_isolation_status=guid_isolation_status,
            malicious_domain_ip=malicious_domain_ip)
        