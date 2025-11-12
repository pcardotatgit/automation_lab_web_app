#  def_send_message***
def send_message(message):
    '''
    MODIFIED : 2025-08-03T16:50:04.000Z

    description : send a message in webex room
    
    how to call it :
    '''
    route="/send_message"
    env.level+='-'
    print('\n'+env.level,white('def send_message() in app.py : >\n',bold=True))
    loguer(env.level+' def send_message() in app.py : >')
    # ===================================================================    
    global BOT_ACCESS_TOKEN
    global DESTINATION_ROOM_ID
    lines=[]   
    print(cyan(f"BOT_ACCESS_TOKEN = {BOT_ACCESS_TOKEN}",bold=True))
    print(cyan(f"DESTINATION_ROOM_ID = {DESTINATION_ROOM_ID}",bold=True))

    URL = 'https://webexapis.com/v1/messages'

    headers = {'Authorization': 'Bearer ' + BOT_ACCESS_TOKEN,'Content-type': 'application/json;charset=utf-8'}
    post_data = {'roomId': DESTINATION_ROOM_ID,'markdown': message}
    response = requests.post(URL, json=post_data, headers=headers)
    if response.status_code == 200:
        # Great your message was posted!
        #message_id = response.json['id']
        #message_text = response.json['text']
        print(green("New message succesfully sent",bold=True))
        #print(message_text)
        print("====================")
        print(response)
    elif response.status_code == 401:
        print()
        print(red("Error bad authentication token",bold=True))    
        loguer(env.level+' def END SUCCESS OF send_message() in app.py : >')    
        env.level=env.level[:-1]
        return result        
    else:
        # Oops something went wrong...  Better do something about it.
        print(red(response.status_code, response.text,bold=True))
        loguer(env.level+' def END ERROR OF send_message() in app.py : >')    
        env.level=env.level[:-1]
        return result
    
