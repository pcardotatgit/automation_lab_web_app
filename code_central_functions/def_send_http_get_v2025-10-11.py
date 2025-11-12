#  def_send_http_get***
def send_http_get(host,relative_url):
    '''
    MODIFIED : 2025-08-03T16:50:04.000Z

    description : send a message to raspi relai. in order to switch on or switch off relais
    
    how to call it : result = send_http_get(relative_url)
        relative_url : path and variable to the resource we invoke
    '''
    route="/send_http_get"
    env.level+='-'
    print('\n'+env.level,white('def send_http_get() in app.py  : >\n',bold=True))
    loguer(env.level+' def send_http_get() in app.py  : > ')
    # ===================================================================    
    lines=[]   
    print('relative URL : 'relative_url)
    URL = 'https://'+host'+/'+relative_url
    response = requests.get(URL)
    if response.status_code == 200:
        print(green("New message succesfully sent",bold=True))
        env.level=env.level[:-1]
        return 1
    else:
        print(red(response.status_code, response.text,bold=True))
        #loguer(env.level+' def END ERROR OF send_http_get() in app.py  : > ')
        env.level=env.level[:-1]
        return 1
    
