# def_code_edit_B***
@app.route('/code_edit_B', methods=['GET','POST'])
def code_edit_B():
    env.level+='-'
    # print()
    # print(env.level,white('route code_edit_B() : >',bold=True))
    #loguer(env.level+' route code_edit_B() : >')
    # print()
    python_code = request.args.get('code')
    subdir = request.args.get('subdir')    
    if python_code=='route_def_.py':
        python_code='route_def_home.py'
    # print()
    # print(' python_code:\n',yellow(python_code,bold=True))
    # print()  
    # print()
    # print(' subdir :\n',yellow(subdir,bold=True))
    # print() 
    filename=f'./code_app_scripts_to_import/{subdir}/{python_code}'  
    filename=filename.replace('/.','/')
    if os.path.exists(filename):    
        with open(filename) as file:
            code=file.read()
        env.level=env.level[:-1]
        return render_template("./code_editor_B.html",code=code,fichier=filename,subdir=subdir,python_code=python_code)
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()    
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>This file does not exist anymore</h3></center>
        </body></html>
        ''';                
        env.level=env.level[:-1]
        return html_output 
    
    
