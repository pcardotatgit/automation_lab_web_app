#  def_change_listening_port_confirmed***
@app.route('/change_listening_port_confirmed', methods=['GET'])
def change_listening_port_confirmed():
    '''
    Created : 2025-07-20

    description : Ok change listening port confirmed, lets do it
    '''
    route="/change_listening_port_confirmed"
    env.level+='-'
    print()
    print(env.level,white('route change_listening_port_confirmed() in ***app.py*** : >',bold=True))
    loguer(env.level+' route change_listening_port_confirmed() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        new_port=request.args.get('new_port')
        print()
        print('new_port : ',new_port)
        loguer(env.level+'- var Inputs : ???')
        loguer(env.level+'-- var new_port : '+new_port+' ???')
        new_ip_address=request.args.get('new_ip_addr')
        loguer(env.level+'-- var new_ip_address : '+new_ip_address+' ???')
        print()
        print('new_ip_address : ',new_ip_address)        
        with open('./code_system_main_blocs/a_core_main.py') as file:
            text_content=file.read()    
        text_content=text_content.replace('port=5000','port='+new_port)
        with open('./code_system_main_blocs/a_core_main.py','w') as file:
            file.write(text_content) 
        with open('./code_system_html_templates/code_editor.html') as file:
            text_content=file.read()    
        text_content=text_content.replace('5000/save_code',new_port+'/save_code')
        with open('./code_system_html_templates/code_editor.html','w') as file:
            file.write(text_content)
        with open('./code_system_html_templates/code_editor_B.html') as file:
            text_content=file.read()    
        text_content=text_content.replace('5000/save_code',new_port+'/save_code')
        with open('./code_system_html_templates/code_editor_B.html','w') as file:
            file.write(text_content)                             
        with open('./result/home_url.txt') as file:
            home_url=file.read()   
        with open('./port.txt','w') as file:
            file.write(new_port)         
        with open('./server_ip_address.txt','w') as file:
            file.write(new_ip_address)              
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>Ok Done New port is : '''+new_port+'''</h3></center>
        <b>Listening port had been changed into :<ul>
        <li>./code_system_main_blocs/a_core_main.py</li>
        <li>./code_system_html_templates/code_editor.html</li>
        <li>./code_system_html_templates/code_editor_B.html</li>        
        </ul>
        </b>
        <br><br><a href="/stop">Click here to stop the App  </a>
        </body></html>
        ''';        
    env.level=env.level[:-1]
    return html_output        

