#  def_del_html_file***
@app.route('/del_html_file', methods=['GET'])
def del_html_file():
    '''
    Created : 2025-07-25T06:45:11.000Z

    description : delete an html file from local library
    '''
    route="/del_html_file"
    env.level+='-'
    print('\n'+env.level,white('route del_html_file() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route del_html_file() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename='./profiles/'+request.args.get('filename')
        print('\nfilename : ',filename+'\n')      
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br>';
        html_output=html_output+'< li>< b>< a href="/code_edit?code=.../code_app_scripts_to_import/'+scriptdir+'/'+file+'&type=function">'+file+'< /a>.---.< a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'">( open in notepad++ )< /b>< /li>'
        html_output=html_output+'< h3>Edit a route< /h3>';
        html_output=html_output+'< h3>Edit a function< /h3>';
        env.level=env.level[:-1]
        return html_output
