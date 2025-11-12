#  def_compile_script***
@app.route('/compile_script', methods=['GET'])
def compile_script():
    '''
    Created : 2025-06-05T21:36:10.000Z

    description : create the selected external script
    '''
    route="/compile_script"
    env.level+='-'
    print()
    print(env.level,white('route compile_script() in ***app.py*** : >',bold=True))
    loguer(env.level+' route compile_script() in ***app.py*** : >')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        scriptdir = request.args.get('subdir')
        print()
        print(' scriptdir :\n',yellow(scriptdir,bold=True))
        print()    
        code = request.args.get('code')
        print()
        print(' code :\n',yellow(code,bold=True))
        print()    
        os.system("python compile_script.py 1")
        with open('./result/home_url.txt') as file:
            home_url=file.read()    
        with open('./result/current_edited_imported_script.txt') as file:
            last_edited_script=file.read()             
        html_output='''<html><body><br><a href="'''+home_url+'''"><b><= back to home</b></a><br><br><a href="/goto_script_B?script='''+last_edited_script+'''&type=route">Go To Last edited</a><br>
        <center><h3>Script builted</h3></center>
        </body></html>
        ''';             
    env.level=env.level[:-1]
    return html_output 

