#  def_expand***
@app.route('/expand', methods=['GET'])
def expand():
    '''
    Created : 2025-09-03T07:31:45.000Z
    description : open selected script and list sub functions
    '''
    route="/expand"
    env.level+='-'
    print('\n'+env.level,white('route expand() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route expand() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        script=request.args.get('code')
        print('\nscript : ',script+'\n')
        type=request.args.get('type')
        print('\ntype : ',type+'\n')      
        parent=request.args.get('parent')
        print('\nparent : ',parent+'\n')        
        if type=="route":
            fichier='./code_app_routes/'+script
            type="function"
        elif type=="function":            
            fichier='./code_app_functions/'+script
        elif type=="main":            
            fichier='./code_system_main_blocs/'+script            
        else:
            subdir=parent.replace('.py','')
            fichier='./code_app_scripts_to_import/'+subdir+'/'+script
        with open(fichier) as file:
            python_code=file.read()
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='<html><body><a href="/application_tree"><b><= back to home</b></a><br><h2>'+script+'</h2><h2>Functions called in this function</h2>';                   
        functions_dict={}
        with open('./result/function_list.txt') as file:
            txt_content=file.read()
        items=txt_content.split('\n')
        for item in items:
            print('item',item)
            if item!='':
                function=item.split(";")[0]
                parent_script=item.split(";")[1]
                functions_dict[function]={'function':function,'parent_script':parent_script}
                function2=function.replace('(','')
                function3='def_'+function2+'.py'
                if functions_dict[function]['parent_script']!="app.py":
                    type="script"
                    parent2=functions_dict[function]['parent_script']
                if function in python_code and function2 not in script:
                    #code_edit_B?code=def_loguer.py&subdir=analyse_application_logs
                    print('\nparent : ',parent+'\n') 
                    print('\nparent_script : ',functions_dict[function]['parent_script']+'\n')
                    if functions_dict[function]['parent_script']=="app.py":
                        parent2="app.py"
                        html_output=html_output+'<li><b><a href="/code_edit?code='+function3+'&type=function">'+function2+'</a> --- [ in '+functions_dict[function]['parent_script']+'  ] --- <a href="/expand?code='+function3+'&type='+type+'&parent='+parent2+'">( Expand )</a></b></li>'
                    else:
                        subdir=functions_dict[function]['parent_script'].replace('.py','')
                        html_output=html_output+'<li><b><a href="/code_edit_B?code='+function3+'&subdir='+subdir+'">'+function2+'</a> --- [ in '+functions_dict[function]['parent_script']+'  ] --- <a href="/expand?code='+function3+'&type='+type+'&parent='+parent2+'">( Expand )</a></b></li>'                         
        html_output=html_output+'</body></html>';
        print('functions_dict : \n',cyan(functions_dict,bold=True))
        env.level=env.level[:-1]
        return (html_output)
        
