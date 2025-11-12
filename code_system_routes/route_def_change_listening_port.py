#  def_change_listening_port***
@app.route('/change_listening_port', methods=['GET'])
def change_listening_port():
    '''
    Created : 2025-07-20

    description : change the listening port of the application
    '''
    route="/change_listening_port"
    env.level+='-'
    print()
    print(env.level,white('route change_listening_port() in ***app.py*** : >',bold=True))
    loguer(env.level+' route change_listening_port() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        with open('./port.txt') as file:
            port=file.read()
        with open('./server_ip_address.txt') as file:
            ip_address=file.read()              
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <form action="/change_listening_port_confirmed" method="GET">
        <b>New Listening port number  : </b><input type="text"  id="new_port" name="new_port" value="'''+port+'''"/><br>
        <b>New Server IP address  : </b><input type="text"  id="new_ip_addr" name="new_ip_addr" value="'''+ip_address+'''"/><br>
        <center><input type="submit" value="valid"/></center>
        </form>
        </body></html>
        ''';   
        env.level=env.level[:-1]
        return html_output
