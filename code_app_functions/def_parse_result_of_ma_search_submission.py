#  def_parse_result_of_ma_search_submission***
def parse_result_of_ma_search_submission(result):
    '''
    MODIFIED : 2025-11-05T13:52:27.000Z

    description : parse the result of malware analytics API call and extract sha256 of malicious file, submision id
    
    how to call it :
    '''
    route="/parse_result_of_ma_search_submission"
    env.level+='-'
    print('\n'+env.level,white('def parse_result_of_ma_search_submission() in app.py : >\n',bold=True))
    loguer(env.level+' def parse_result_of_ma_search_submission() in app.py : >')
    # ===================================================================    
    json_dict=json.loads(result)['data']['items']
    #print("\njson_dict : ",cyan(json_dict,bold=True)) 
    Malware_Analytics_sample_ID='xxxxxxxx'
    for item in json_dict:
        for item2 in item.items():
            if 'item' in item2:
                #print("\nitem2 : ",cyan(item2,bold=True))
                #print("\ntype",cyan(type(item2 ),bold=True))
                Malware_Analytics_sample_ID=str(item2[1]['sample'])
                #print("\nsample : ",red(item2[1]['sample'],bold=True))
                print('==========================================')
    print("\nMalware_Analytics_sample_ID : ",cyan(Malware_Analytics_sample_ID,bold=True)) 
    # ===================================================================
    loguer(env.level+' def END OF parse_result_of_ma_search_submission() in app.py : >')    
    env.level=env.level[:-1]
    return Malware_Analytics_sample_ID
    
