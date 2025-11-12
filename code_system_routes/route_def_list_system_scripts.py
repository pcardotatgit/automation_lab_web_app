#  def_list_system_scripts***
@app.route('/list_system_scripts', methods=['GET'])
def list_system_scripts():
    '''
    Created : 2025-08-01

    description : go to the menu for editing system scripts
    '''
    route="/list_system_scripts"
    env.level+='-'
    # print()
    # print(env.level,white('route list_system_scripts() in ***app.py*** : >',bold=True))
    #loguer(env.level+' route list_system_scripts() in ***app.py*** : >')
    # print()
    last_script=''
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    if os.path.exists('./result/keyword.txt'):
        with open('./result/keyword.txt') as file:
            keyword=file.read()         
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br><form action="/search_system_script" method="get"><input type="text" name="keyword" value="'+keyword+'"><input type="submit" value="Search"></form><br>';        

    html_output=html_output+'<h4>System Route :</h4><table border="1"><tbody>';
    
    
    #html_output=html_output+'<h3>Edit a system route</h3><ul>';
    files =[file for file in os.listdir('./code_system_routes')]    
    for file in files:
        if 'route_' in file and file !='back' and '.py' in file:
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<tr><td><b><a href="/edit_html?filename=../code_system_routes/'+file+'">'+file+' ( open in notepad++ )</a></b></td><td><a href="/duplicate_system_route?filename='+file+'">(duplicate in app routes)</a></b></td></tr>'    
    html_output=html_output+'</tbody></table><h4>System Functions :</h4><table border="1"><tbody>';
    files =[file for file in os.listdir('./code_system_functions')]     
    for file in files:
        if 'route_' not in file and file !='back' and '.py' in file:
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<tr><td><b><a href="/edit_html?filename=../code_system_functions/'+file+'">'+file+' ( open in notepad++ )</a></b></td><td><a href="/duplicate_system_function?filename='+file+'">(duplicate in app functions)</a></b></td></tr>' 
    html_output=html_output+'</tbody></table><br><a href="/stop">Click here to stop the App  </a></body></html>';            
    env.level=env.level[:-1]
    return html_output
