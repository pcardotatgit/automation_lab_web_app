#  def_new_function_create***
@app.route('/new_function_create', methods=['GET','POST'])
def new_function_create():
    '''
    Modified : 202501001
    
    create the function .py file into the ./code_chunks subfolder if that one doesn t already exist
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_function_create() : >',bold=True))
    loguer(env.level+' route new_function_create() : >')
    print()
    name = request.args.get('name')
    name=name.replace('-','_')
    name=name.replace(' ','_')    
    description = request.args.get('description')
    args = request.args.get('args')       
    filename='./code_app_functions/def_'+name+'.py'
    filename2='/def_'+name+'.py'

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
    with open('./code_architecture/app_functions.txt') as file:
        text_content=file.read()
    print(' text_content :\n',yellow(text_content,bold=True))
    with open('./code_architecture/app_routes.txt') as file:
        text_content2=file.read()
    print(' text_content :\n',yellow(text_content,bold=True))    
    print()          
    mot=filename2.replace('/','')
    print(' mot :\n',yellow(mot,bold=True))
    print()    
    if mot in text_content or mot in text_content2:
        print(filename+' already exists ! Choose another name')
        with open('./result/home_url.txt') as file:
            home_url=file.read()        
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>This function already exists ! choose another name</h3></center>
    <form action="/new_function_create" method="GET">
    <b>function name : </b><input type="text"  id="function_name" name="name" /><br><br>
    <b>Function description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>        
        </body></html>
        ''';        
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        with open('./code_templates/function_template.py') as file:
            text_content=file.read()
        text_content=text_content.replace('example_name',name)
        version='MODIFIED : '+current_date_and_time_for_json_data()+'\n\n    description : '
        description=version+description
        text_content=text_content.replace('***description***',description) 
        text_content=text_content.replace('***app.py***','app.py')        
        text_content=text_content.replace('(args)',args)         
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_functions.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>function created</h3></center>
        <center><h3><a href="/code_edit?code='''+filename2+'''&type=function">EDIT in inline editor :'''+filename2+'''</a>. OR .<a href="/edit_html?filename=.'''+filename+'''">( Edit in notepad++ )</a></center>
        </body></html>
        ''';             
    with open('./result/current_edited_script.txt',"w") as file:
        file.write(filename2)        
    env.level=env.level[:-1]
    return html_output   
    
    
