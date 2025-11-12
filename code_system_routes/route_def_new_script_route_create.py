#  def_new__script_route_create***
@app.route('/new_script_route_create', methods=['GET','POST'])
def new__script_route_create():
    '''
    Modified : 20250324
    
    create a new route for the selected imported script
    '''
    env.level+='-'
    print()
    print(env.level,white('route new__script_route_create() : >',bold=True))
    loguer(env.level+' route new__script_route_create() : >')
    print()
    scriptdir= request.args.get('scriptdir')    
    name = request.args.get('name')
    name=name.replace('-','_')
    name=name.replace(' ','_')    
    description = request.args.get('description')

    filename='./code_app_scripts_to_import/'+scriptdir+'/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'

    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print()
    print(' filename2 :\n',yellow(filename2,bold=True))
    print()
    print(' description :\n',yellow(description,bold=True))
    print()
    print()
    print(' scriptdir :\n',yellow(scriptdir,bold=True))
    print()    
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    # check if file already exits 
    fichier_route = Path(filename)    
    if fichier_route.is_file():    
        print(filename+' already exists ! Choose another name')
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><center><h3>new function for [ '''+scriptdir+'''.py ]</h3></center>
    <form action="/new_script_route_create" method="GET">
    <b>function name : </b><input type="text"  id="function_name" name="name" /><br><br>
    <b>Function description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <input type="hidden"  id="scriptdir" name="scriptdir" value="'''+scriptdir+'''"/>
    <center><input type="submit" value="create"/></center>
    </form>
    </body></html>
    ''';         
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        with open('./code_templates/route_template.py') as file:
            text_content=file.read()
        text_content=text_content.replace('example_name',name)
        version='MODIFIED : '+current_date_and_time_for_json_data()+'\n\n    description : '
        description=version+description
        text_content=text_content.replace('***description***',description) 
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open(f'./code_app_scripts_to_import/{scriptdir}/script_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>function created</h3></center>
        <center><h3><a href="/code_edit_B?code='''+filename2+'''&subdir='''+scriptdir+'''">EDIT in inline editor :'''+filename2+'''</a>. OR .<a href="/edit_html?filename=.'''+filename+'''">( Edit in notepad++ )</a></center><hr><br><b><a href="/new_script_function?scriptdir='''+scriptdir+'''">Create a new function for [ '''+scriptdir+'''.py ]</a></b><br><b><a href="/new_script_route?scriptdir='''+scriptdir+'''">Create a new route for [ '''+scriptdir+'''.py ]</a></b>
        </body></html>
        ''';           
    with open('./result/current_edited_script.txt',"w") as file:
        file.write(filename2)          
    env.level=env.level[:-1]
    return html_output   
    
    
