#  def_challenge_result***
@app.route('/challenge_result', methods=['GET'])
def challenge_result():
    '''
    Created : 2025-11-05

    description : display the challenge result and discovery tables
    '''
    route="/challenge_result"
    env.level+='-'
    print('\n'+env.level,white('route challenge_result() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route challenge_result() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        hostname=variable_value('victim_hostname')
        guid=variable_value('GUID')
        host_ip=variable_value('infected_machine_internal_ip_address')
        internal_ip_1=variable_value('internal_infected_ip_address_1')  
        internal_ip_2=variable_value('internal_infected_ip_address_2')
        internal_ip_3=variable_value('internal_infected_ip_address_3')
        sha256=variable_value('CSE_malicious_file_sha256')
        domain=variable_value('domain')
        executed_malware_id=variable_value('CSE_Executed_Malware_event_type_ID')
        threat_detected_id=variable_value('CSE_Threat_Detected_event_type_ID')
        sha256_submission=variable_value('Malware_Analytics_sample_ID')
        nb_events=variable_value('nb_of_events_on_victim_machine')
        filename=variable_value('CSE_malicious_file_name')
        malicious_domain_ip=variable_value('malicious_domain_ip')
        # ##
        internal_ip_1_isolation_status=variable_value('internal_ip_1_isolation_status')
        if 'NO' not in internal_ip_1_isolation_status:
            internal_ip_1_isolation_status='YES'        
        internal_ip_2_isolation_status=variable_value('internal_ip_2_isolation_status')
        if 'NO' not in internal_ip_2_isolation_status:
            internal_ip_2_isolation_status='YES'        
        internal_ip_3_isolation_status=variable_value('internal_ip_3_isolation_status')
        if 'NO' not in internal_ip_3_isolation_status:
            internal_ip_3_isolation_status='YES'
        host_ip_isolation_status=variable_value('host_ip_isolation_status')
        if internal_ip_3=="192.168.128.156" and host_ip=="192.168.128.156":  
            host_ip_isolation_status='YES'
        '''
        if 'NO' not in host_ip_isolation_status:
            host_ip_isolation_status='YES'   
        '''
        guid_isolation_status=variable_value('guid_isolation_status')
        if 'NO' not in guid_isolation_status:
            guid_isolation_status='YES'        
        hostname_isolation_status=variable_value('host_ip_isolation_status')
        if 'NO' not in hostname_isolation_status:
            hostname_isolation_status='YES'        
        sha256_isolation_status=variable_value('sha256_isolation_status')
        if 'NO' not in sha256_isolation_status:
            sha256_isolation_status='YES'        
        filename_isolation_status=variable_value('filename_isolation_status')
        if 'NO' not in filename_isolation_status:
            filename_isolation_status='YES'        
        malicious_domain_ip_isolation_status=variable_value('malicious_domain_ip_isolation_status')
        if 'NO' not in malicious_domain_ip_isolation_status:
            malicious_domain_ip_isolation_status='YES'        
        domain_isolation_status=variable_value('domain_isolation_status')
        if 'NO' not in domain_isolation_status:
            domain_isolation_status='YES'        
        victim_hostname_isolation_status=variable_value('victim_hostname_isolation_status')
        if 'NO' not in victim_hostname_isolation_status:
            victim_hostname_isolation_status='YES'        
        PAGE_DESTINATION="z_challenge_result"
        page_name="z_challenge_result.html"
        loguer(env.level+' route END OF challenge_result() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,hostname=hostname,
            host_ip=host_ip,internal_ip_1=internal_ip_1,internal_ip_2=internal_ip_2,internal_ip_3=internal_ip_3,sha256=sha256,domain=domain,executed_malware_id=executed_malware_id,
            threat_detected_id=threat_detected_id,sha256_submission=sha256_submission,guid=guid,nb_events=nb_events,filename=filename,malicious_domain_ip=malicious_domain_ip,
            internal_ip_1_isolation_status=internal_ip_1_isolation_status,internal_ip_2_isolation_status=internal_ip_2_isolation_status,internal_ip_3_isolation_status=internal_ip_3_isolation_status,
            host_ip_isolation_status=host_ip_isolation_status,guid_isolation_status=guid_isolation_status,hostname_isolation_status=hostname_isolation_status,sha256_isolation_status=sha256_isolation_status,
            filename_isolation_status=filename_isolation_status,malicious_domain_ip_isolation_status=malicious_domain_ip_isolation_status,domain_isolation_status=domain_isolation_status,
            victim_hostname_isolation_status=victim_hostname_isolation_status)
        
