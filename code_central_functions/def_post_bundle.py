#  def_post_bundle***
def post_bundle(json_payload,access_token,host):
    '''
    MODIFIED : 2025-07-20

    description : post the bundle to XDR
    '''
    route="/post_bundle"
    env.level+='-'
    # #########################################################################################################################
    #
    # API documentation : https://developer.cisco.com/docs/cisco-xdr/private-intelligence-api-bundle-post-many-new-entities-using-a-single-http-call/
    #
    # #########################################################################################################################     
    print('\n'+env.level,white('def post_bundle() in app.py : >\n',bold=True))
    url=f"{host}/ctia/bundle/import"
    headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
    response = requests.post(url, headers=headers,data=json_payload)
    rep = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
    print(rep)
    if response.status_code==200 or response.status_code==201:
        env.level=env.level[:-1]
        return 1
    else:
        env.level=env.level[:-1]
        return 0
      