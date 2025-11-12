#  def_new_html_page_create***
@app.route('/new_html_page_create', methods=['GET'])
def new_html_page_create():
    '''
    MODIFIED : 2025-09-25

    description : Create a new html page into the ./tempates subfolder
    '''
    route="/new_html_page_create"
    env.level+='-'
    print()
    print(env.level,white('route new_html_page_create() : >',bold=True))
    loguer(env.level+' route new_html_page_create() : >')
    print()
    name = request.args.get('name')
    name=name.split('.')[0]
    description = request.args.get('description')
    template = request.args.get('template')
    filename='z_'+name+'.html'
    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print()
    print(' template :\n',yellow(template,bold=True))
    print()
    print(' description :\n',yellow(description,bold=True))
    print()
    print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
    # check if file already exits
    fichier_function = Path('z_'+name+'.html')    
    if fichier_function.is_file():
        print(filename+' already exists ! Choose another name')
        html_output='''<html><body>
        <center><h3>This html page already exists ! choose another name</h3></center>
    <form action="/new_html_page_create" method="GET">
    <b>Page name : </b><input type="text"  id="function_name" name="name" /><br><br>
    <b>Page description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>        
        </body></html>
        ''';        
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        if template=='page1':
            with open('./code_templates/html_page.html') as file:
                text_content=file.read()
        elif template=='page2':
            with open('./code_templates/html_page2.html') as file:
                text_content=file.read()   
        elif template=='page3':
            with open('./code_templates/html_page3.html') as file:
                text_content=file.read()     
        elif template=='page4':
            with open('./code_templates/html_page4.html') as file:
                text_content=file.read() 
        elif template=='page5':
            with open('./code_templates/html_page5.html') as file:
                text_content=file.read()       
        elif template=='page6':
            with open('./code_templates/html_page6.html') as file:
                text_content=file.read()     
        elif template=='page7':
            with open('./code_templates/html_page7.html') as file:
                text_content=file.read()     
        elif template=='page8':
            with open('./code_templates/html_page8.html') as file:
                text_content=file.read()       
        elif template=='page9':
            with open('./code_templates/html_page9.html') as file:
                text_content=file.read()   
        elif template=='page10':
            with open('./code_templates/html_page10.html') as file:
                text_content=file.read()              
        elif template=='page11':
            with open('./code_templates/html_page11.html') as file:
                text_content=file.read()   
        elif template=='page12':
            with open('./code_templates/html_page12.html') as file:
                text_content=file.read()               
        elif template=='page13':
            with open('./code_templates/html_page13.html') as file:
                text_content=file.read()         
        elif template=='page14':
            with open('./code_templates/html_page14.html') as file:
                text_content=file.read()         
        elif template=='page15':
            with open('./code_templates/html_page15.html') as file:
                text_content=file.read()          
        elif template=='page16':
            with open('./code_templates/html_page1.html') as file:
                text_content=file.read()                    
        text_content=text_content.replace('example_name',name)
        text_content="* "+filename+"***"+text_content
        version='Created : '+current_date_and_time_for_json_data()+'\n\n    description : '
        description=version+description
        text_content=text_content.replace('***description***',description) 
        filename2=filename.replace("./templates/","")
        filename2=filename2.replace(".html","")
        main_index_chunk='''&nbsp;&nbsp;&nbsp;&nbsp;{% if PAGE_DESTINATION == &quot;'''+filename2+'''&quot;%}<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{% extends &quot;'''+filename2+'''.html&quot; %}<br>
&nbsp;&nbsp;&nbsp;&nbsp;{% endif %} '''
        with open("./code_app_html_templates/"+filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>function created</h3></center>
        <center><h3><a href="/code_edit?code='''+filename+'''&type=html">EDIT in inline editor :'''+filename+'''</a>. OR .<a href="/edit_html?filename='''+filename+'''">( Edit in notepad++ )</a></center><br><br>'''+main_index_chunk+'''
        </body></html>
        ''';      
        with open('./code_architecture/main_html.txt',"a+") as fichier:
            fichier.write(filename+'\n')        
    env.level=env.level[:-1]
    return html_output  
