#  def_search_app_function***
@app.route('/search_app_function', methods=['GET'])
def search_app_function():
    '''
    Created : 2025-08-01T06:20:17.000Z

    description : list app functions that have keyword in their names
    '''
    route="/search_app_function"
    env.level+='-'
    print('\n'+env.level,white('route search_app_function() in ***app.py*** : >\n',bold=True))
    #loguer(env.level+' route search_app_function() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        keyword=request.args.get('keyword')
        print('\nkeyword : ',keyword)     
        with open('./result/home_url.txt') as file:
            home_url=file.read()  
        with open('./result/keyword.txt','w') as file:
            file.write(keyword)              
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br><form action="/search_app_function" method="get"><input type="text" name="keyword" value="'+keyword+'" ><input type="submit" value="Search"></form><br><br>';
                
        with open('./result/current_edited_function.txt') as file:
            last_function=file.read()
        html_output=html_output+'<b><a href="/code_edit?code='+last_function+'&type=function">Last Edited : '+last_function+'</a><br><a href="/new_function">Create a new function</a><br><h4>FUNCTIONS :</h4><table border="1"><tbody>';   
        
        files =[file for file in os.listdir('./code_app_functions')]
        ii=0
        scriptdir='code_app_functions'
        function_list=[]
        for file in files:
            if 'a_core_' not in file and file !='back' and keyword in file: 
                # print(' file : ',yellow(file,bold=True)) 
                html_output=html_output+'<tr><td><b><a href="/code_edit?code='+file+'&type=function">'+file+'</a></td><td><a href="/edit_html?filename=../code_app_functions/'+file+'">( open in notepad++ )</b></td><td><a href="/delete_file?filename=../code_app_functions/'+file+'&scriptdir='+scriptdir+'">(DEL)</a></b></td><td><a href="/rename_file?filename=../code_app_functions/'+file+'&scriptdir='+scriptdir+'">(REN)</a></b></td><td><a href="/move_function_to_system?filename=../code_app_functions/'+file+'&scriptdir=code_system_functions">( mv 2 sys )</a></b></td><td><a href="/copy_function_to_central?filename=./code_app_functions/'+file+'&scriptdir=code_central_functions">( cp 2 central )</a></b></td><td><a href="/duplicate_function?filename='+file+'">(duplic)</a></b></td></tr>'
        env.level=env.level[:-1]
        html_output=html_output+'\n</tbody></table><br><a href="/list_routes">List Routes</a><br><br><a href="/stop">Click here to stop the App  </a></body><html>'
        return html_output
    

            