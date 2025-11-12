# def_code_edit***
@app.route('/code_edit', methods=['GET','POST'])
def code_edit():
    env.level+='-'
    # print()
    # print(env.level,white('route code_edit() : >',bold=True))
    #loguer(env.level+' route code_edit() : >')
    # print()
    python_code = request.args.get('code')
    the_type = request.args.get('type')    
    if python_code=='route_def_.py':
        python_code='route_def_index.py'
    # print()
    # print(' python_code:\n',yellow(python_code,bold=True))
    # print()  
    # print()
    # print(' the_type :\n',yellow(the_type,bold=True))
    # print() 
    if the_type=='function':
        filename=f'./code_app_functions/{python_code}'  
    elif the_type=='route':
        filename=f'./code_app_routes/{python_code}' 
    else:
        filename=f'./code_app_html_templates/{python_code}'
    filename=filename.replace('/.','/')
    # print()
    # print(' filename :',yellow(filename,bold=True))
    # print()      
    with open(filename) as file:
        code=file.read()
    env.level=env.level[:-1]
    return render_template("./code_editor.html",code=code,fichier=filename,the_type=the_type)

