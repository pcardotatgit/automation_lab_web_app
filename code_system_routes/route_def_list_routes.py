# def list_routes***
@app.route('/list_routes', methods=['GET','POST'])
def list_routes():
    '''
        modified : 2025-09-25
        
        description : liste application routes
        
        how_to_call : list_routes()
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route list_routes() : >',bold=True))
    #loguer(env.level+' route list_routes() : >')
    # print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    if os.path.exists('./result/keyword.txt'):
        with open('./result/keyword.txt') as file:
            keyword=file.read()  
    else:
        keyword=''
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br><form action="/search_app_route" method="get"><input type="text" name="keyword" value="'+keyword+'"><input type="submit" value="Search"></form><br><br>';
    with open('./result/current_edited_route.txt') as file:
        last_route=file.read()
    html_output=html_output+'<b><a href="/code_edit?code='+last_route+'&type=route">Last Edited : '+last_route+'</a><br><a href="/new_route">Create a new route</a><br><h4>ROUTES :</h4><table border="1"><tbody>';
    files =[file for file in os.listdir('./code_app_routes')]
    ii=0
    function_list=[]
    scriptdir='code_app_routes'
    for file in files:
        if 'route_' in file and 'a_core_' not in file and file !='back':
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<tr><td><b><a href="/code_edit?code='+file+'&type=route">'+file+'</a></td><td><a href="/edit_html?filename=../code_app_routes/'+file+'">( open in notepad++ )</a></td><td><a href="/delete_file?filename=../code_app_routes/'+file+'&scriptdir='+scriptdir+'">(DEL)</a></b></td><td><a href="/rename_file?filename=../code_app_routes/'+file+'&scriptdir='+scriptdir+'">(REN)</a></b></td><td><a href="/move_route_to_system?filename=../code_app_routes/'+file+'&scriptdir=code_system_routes">(mv 2 sys)</a></b></td><td><a href="/copy_route_to_central?filename=./code_app_routes/'+file+'&scriptdir=code_central_routes">(cp 2 central)</a></b></td><td><a href="/duplicate_route?filename='+file+'">(duplic)</a></b></td></tr>'
    env.level=env.level[:-1]
    html_output=html_output+'\n</tbody></table><br><a href="/list_functions">List Functions</a><br><br><a href="/stop">Click here to stop the App  </a></body><html>'
    return html_output
    

