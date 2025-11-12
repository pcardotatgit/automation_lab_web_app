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
        filename=request.args.get('filename')
        filename=filename.replace('../','./')
        print('\nfilename : ',filename+'\n')    
        scriptdir='code_app_html_templates'
        html_output=f'<h3>Do you really want to delete : <br><br>{filename}</h3><br>in directory <b>./code_app_html_templates</b><br><hr>';
        html_output=html_output+f'<form action="/ok_delete_file" method="GET"><input type="hidden" name="filename" value="{filename}"><input type="hidden" name="scriptdir" value="{scriptdir}"><input type="submit" value="YES I DO"></form>'
        env.level=env.level[:-1]
        return html_output  
