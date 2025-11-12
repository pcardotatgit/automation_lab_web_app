#  def_confirm_workingdir_change***
@app.route('/confirm_workingdir_change', methods=['GET'])
def confirm_workingdir_change():
    '''
    Created : 2025-06-07T14:29:14.000Z

    description : write the new directory in ./result/selected_script_working_dir.txt
    '''
    route="/confirm_workingdir_change"
    env.level+='-'
    print()
    print(env.level,white('route confirm_workingdir_change() in ***app.py*** : >',bold=True))
    loguer(env.level+' route confirm_workingdir_change() in ***app.py*** : >')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        workingdir=request.args.get('directory')
        print()
        print('workingdir : ',workingdir)        
        with open('./result/selected_script_working_dir.txt','w') as file:
            file.write(workingdir)         
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>Script Destination Directory Updated</h3></center>
        </body></html>
        ''';             
    env.level=env.level[:-1]
    return html_output 
