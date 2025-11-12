# def_new_route_create***
@app.route('/new_route_create', methods=['GET','POST'])
def new_route_create():
    env.level+='-'
    print()
    print(env.level,white('route new_route_create() : >',bold=True))
    loguer(env.level+' route new_route_create() : >')
    print()
    '''
    Modified : 20250923
    
    create the route .py file into the ./code_app_routes subfolder if that one doesn t already exist
    '''    
    name = request.args.get('name')
    name=name.replace('-','_')
    name=name.replace(' ','_')    
    if '/' in name:
        name=name.replace('/','')
    description = request.args.get('description')
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'

    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print()
    print(' filename2 :\n',yellow(filename2,bold=True))
    print()
    print(' description :\n',yellow(description,bold=True))
    print()
    print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
    # check if file already exits
    with open('./code_architecture/app_routes.txt') as file:
        text_content2=file.read()    
    fichier_route = Path('./code_app_routes/route_def_'+name+'.py')    
    if fichier_route.is_file() or filename in text_content2:
        print(filename+' already exists ! Choose another name')
        with open('./result/home_url.txt') as file:
            home_url=file.read()        
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>This route already exists ! choose another name</h3></center>
    <form action="/new_route_create" method="GET">
    <b>route name : </b><input type="text"  id="route_name" name="name" /><br><br>
    <b>route description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>        
        </body></html>
        ''';        
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        with open('./code_templates/route_template.py') as file:
            text_content=file.read()
        text_content=text_content.replace('example_name',name)
        version='Created : '+current_date_and_time_for_json_data()+'\n\n    description : '
        description=version+description
        text_content=text_content.replace('***description***',description) 
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>route created</h3></center>
        <center><h3><a href="/code_edit?code='''+filename2+'''&type=route">EDIT in inline editor :'''+filename2+'''</a>. OR .<a href="/edit_html?filename=.'''+filename+'''">( Edit in notepad++ )</a></center>
        </body></html>
        ''';             
    env.level=env.level[:-1]
    return html_output  
