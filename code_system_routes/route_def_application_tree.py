#  def_application_tree***
@app.route('/application_tree', methods=['GET'])
def application_tree():
    '''
    Created : 2025-09-03
    description : create and display the application function dependency tree structure
    
    how to call it : application_tree()
    '''
    route="/application_tree"
    env.level+='-'
    print('\n'+env.level,white('route application_tree() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route application_tree() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        functions_list_file=open('./result/function_list.txt','w')
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br>';
        html_output=html_output+'<h1>Application tree</h1>';
        html_output=html_output+'<h2>Main loop in app.py</h2>';
        html_output=html_output+'<li><b>Main function : <a href="/edit_html?filename=../code_system_main_blocs/a_core_main.py">if __name__==\'main\'</a> : <a href="/expand?code=a_core_main.py&type=main&parent=app.py"> ( Expand ) </a></li>'
        html_output=html_output+'<h2>List Routes in app.py</h2>';
        files =[file for file in os.listdir('./code_app_routes')]
        function_list=[]
        scriptdir='code_app_routes'
        for file in files:
            if 'route_' in file and 'a_core_' not in file and file !='back':
                # print(' file : ',yellow(file,bold=True))
                file2=file.replace("route_def_","")
                file2=file2.replace(".py","")
                file2=file2.replace("/","")
                html_output=html_output+'<li><b><a href="/code_edit?code='+file+'&type=route">/'+file2+'</a> : <a href="/expand?code='+file+'&type=route&parent=app.py"> ( Expand ) </a></b></li>'
                functions_list_file.write(file2+"(;app.py\n")
        html_output=html_output+'<h2>List Functions in app.py</h2>';
        files =[file for file in os.listdir('./code_app_functions')]
        ii=0
        scriptdir='code_app_functions'
        function_list=[]
        for file in files:
            if 'route_' not in file and 'a_core_' not in file and file !='back':
                # print(' file : ',yellow(file,bold=True))
                html_output=html_output+'<li><b><a href="/code_edit?code='+file+'&type=function">'+file+'</a> : <a href="/expand?code='+file+'&type=function&parent=app.py"> ( Expand ) </a></b></li>'
                file2=file.replace(".py","")
                file2=file2.replace("def_","")
                functions_list_file.write(file2+"(;app.py\n")
        html_output=html_output+'<h2>List External Imported Scripts</h2>';
        with open('./code_architecture/imported_scripts_to_import.txt') as file:
            text_content=file.read()
        print('imported_scripts_to_import.txt : ',cyan(text_content,bold=True))
        lines=text_content.split('\n')
        for line in lines:
            if line!='':
                html_output=html_output+'<li><b><a href="/goto_script_B?script='+line+'&type=route">'+line+'</a></b><ul>'
                scriptdir2=line.replace(".py","")
                file2s =[file2 for file2 in os.listdir('./code_app_scripts_to_import/'+scriptdir2)]
                for file2 in file2s:
                    if 'route_' not in file2 and file2 !='back' and '.py' in file2:
                        html_output=html_output+'<li><b><a href="/code_edit_B?code='+file2+'&subdir='+scriptdir2+'">'+file2+'</a> : <a href="/expand?code='+file2+'&type=script&parent='+line+'"> ( Expand ) </a></b></li>'
                        file3=file2.replace(".py","")
                        file3=file3.replace("def_","")
                        functions_list_file.write(file3+"(;"+line+"\n")
                html_output=html_output+'</ul></li>'
        html_output=html_output+'</body></html>';
        functions_list_file.close()
        env.level=env.level[:-1]
        return html_output
