#  def_compile_script_B***
@app.route('/compile_script_B', methods=['GET'])
def compile_script_B():
    '''
    Created : 2025-06-06T16:11:31.000Z

    description : create the selected application script
    '''
    route="/compile_script_B"
    env.level+='-'
    print()
    print(env.level,white('route compile_script_B() in ***app.py*** : >',bold=True))
    loguer(env.level+' route compile_script_B() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        scriptdir = request.args.get('type')
        print()
        print(' type :\n',yellow(type,bold=True))
        print()    
        code = request.args.get('code')
        print()
        print(' code :\n',yellow(code,bold=True))
        print()    
        os.system("python compile.py 1")
        with open('./result/home_url.txt') as file:
            home_url=file.read()        
        html_output='''<html><body><a href="/code_edit?code='''+code+'''&type='''+type+'''"><b><= back to code</b></a><br><br><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>Script builted</h3></center>
        </body></html>
        ''';             
    env.level=env.level[:-1]
    return html_output 
  
