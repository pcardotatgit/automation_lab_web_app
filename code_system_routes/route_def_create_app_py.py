# create_app_py***
@app.route('/create_app_py', methods=['GET'])
def create_app_py():
    env.level+='-'
    route="/create_app_py"
    print()
    print(env.level,white('def create_app_py() : >',bold=True))
    loguer(env.level+' def create_app_py() : >')
    print()
    with open('./app.py') as file:
            text_content=file.read()     
    with open('./code_backup/app_'+current_date_and_time()+'.py','w') as file:
            file.write(text_content)     
    print()
    print(green('   app.py backup = OK',bold=True))
    print()                
    with open('./app_new.py','w') as app:
        print()
        print(green('  Create header',bold=True))
        print()    
        with open('./code_system_main_blocs/a_core_header.py') as file:
            text_content=file.read() 
        app.write(text_content)
        app.write('\n')
        print(green('  - Create header = OK',bold=True))
        print()
        print(green('  Create Import section',bold=True))
        with open('./code_system_main_blocs/a_core_imports.py') as file:
            text_content=file.read() 
        app.write(text_content)
        app.write('\n')   
        print(green('  - Create Import section = OK',bold=True))
        print()
        print(green('  Create Global Variable Definition',bold=True))
        with open('./code_system_main_blocs/a_core_global_definitions.py') as file:
            text_content=file.read() 
        app.write(text_content)
        app.write('\n')
        app.write('\n')     
        print(green('  - Create Global Variable Definition = OK',bold=True))
        print()
        print(green('  Create system functions ',bold=True))      
        line_out='''
# here under FUNCTIONS ===========================   
 
'''
        app.write(line_out)            
        with open('./code_architecture/system_functions.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_system_functions/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')
        print(green('  - Create system functions = OK',bold=True))
        print()  
        print(green('  Create application functions',bold=True))
        app.write(line_out)            
        with open('./code_architecture/app_functions.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_app_functions/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')
        print(green('  - Create application functions = OK',bold=True))
        print()     
        print(green('  Create system routes ',bold=True))        
        line_out='''
# here under the flask routes part ===========================    

app = Flask(__name__)

'''
        app.write(line_out)
        with open('./code_architecture/system_routes.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_system_routes/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')  
                
        print(green('  - Create system routes = OK',bold=True))
        print()     
        print(green('  Create application routes',bold=True))  
        with open('./code_architecture/app_routes.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_app_routes/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')           
        print(green('  - Create system routes = OK',bold=True))
        print()     
        print(green('  Create Main Function',bold=True))        
        with open('./code_system_main_blocs/a_core_main.py') as file:
            text_content=file.read() 
        app.write('\n') 
        app.write(text_content)
        app.write('\n')         
        print(green('  - Create Main Function = OK',bold=True))          
    with open('./result/home_url.txt') as file:
        home_url=file.read()            
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
    <center><h2>app_new.py created in the root directory</h2><b>It is actually named : app_new.py</b></center></body></html>''';          
    env.level=env.level[:-1]
    return html_output
