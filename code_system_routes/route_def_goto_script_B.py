# def_goto_script_B***
@app.route('/goto_script_B', methods=['GET'])
def goto_script_B():
    '''
        modified : 20250709
        menu for imported scripts
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route goto_script_B() : >',bold=True))
    #loguer(env.level+' route goto_script_B() : >')
    # print()
    scriptdir = request.args.get('script')
    with open('./result/selected_script.txt','w') as file:
        file.write(scriptdir)
    fichier=scriptdir
    with open('./result/current_edited_script.txt') as file:
        last_edited_script=file.read()    
    with open('./result/current_edited_imported_script.txt','w') as file:
        file.write(fichier)
    scriptdir=scriptdir.replace('.py','')
    # print()
    # print(' scriptdir :\n',yellow(scriptdir,bold=True))
    # print()      
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    with open('./result/selected_script_working_dir.txt') as file:
        workingdir=file.read()    
    '''
    with open(scriptdir+'/build_location.txt','w') as file:
        workingdir=file.read()     
    '''      
    #html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br><b><a href="/new_script_function?scriptdir='+scriptdir+'">Create a new function for [ '+scriptdir+'.py ]</a></b><br><b><a href="/new_script_route?scriptdir='+scriptdir+'">Create a new route for [ '+scriptdir+'.py ]</a></b><br><br>script working directory is : <br><b>'+workingdir+'</b><a href="/change_script_working_directory"><b>...( modify )</b></a></b><br><br><a href="/compile_script?code='+fichier+'&subdir='+scriptdir+'"><b>Compile Script</b></a></b>';
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><h2>[ '+scriptdir+'.py ]</h2><b><a href="/new_script_function?scriptdir='+scriptdir+'">Create a new function</a>....<a href="/new_function_from_library_B?script='+fichier+'&scriptdir='+scriptdir+'">Add a new function from library</a></b><br><b><a href="/new_script_route?scriptdir='+scriptdir+'">Create a new route</a>....<a href="/new_route_from_library_B?script='+fichier+'&scriptdir='+scriptdir+'">Add a new route from library</a></b><br><br><a href="/compile_script?code='+fichier+'&subdir='+scriptdir+'"><b>Compile Script</b></a> In working directory : <br><b>'+workingdir+'</b><a href="/change_script_working_directory"><b>-( change )</b></a></b><br><br>'
    html_output=html_output+'<b><a href="/code_edit_B?code='+last_edited_script+'&subdir='+scriptdir+'">Last edited : '+last_edited_script+'</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/'+last_edited_script+'">( open in notepad++ )</a></b>'
    html_output=html_output+'<h3>Edit a core chunks</h3><ul>'
    files =[file for file in os.listdir('./code_app_scripts_to_import/'+scriptdir)]
    ii=0
    #function_list=[]
    html_output=html_output+'<li><b><a href="/code_edit_B?code=a_main.txt&subdir='+scriptdir+'">a_main.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/a_main.txt">( open in notepad++ )</a></b></li><li></li><li><b><a href="/code_edit_B?code=a_header.txt&subdir='+scriptdir+'">a_header.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/a_header.txt">( open in notepad++ )</a></b></li><li><b><a href="/code_edit_B?code=a_imports.txt&subdir='+scriptdir+'">a_imports.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/a_imports.txt">( open in notepad++ )</a></b></li><li><b><a href="/code_edit_B?code=a_global_variables.txt&subdir='+scriptdir+'">a_global_variables.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/a_global_variables.txt">( open in notepad++ )</a></b></li><li><b><a href="/code_edit_B?code=script_functions.txt&subdir='+scriptdir+'">script_functions.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/script_functions.txt">( open in notepad++ )</a></b></li><li><b><a href="/code_edit_B?code=script_routes.txt&subdir='+scriptdir+'">script_routes.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/script_routes.txt">( open in notepad++ )</a></b></li><li><b><a href="/code_edit_B?code=./package_dev/z_init_appli.py&subdir='+scriptdir+'">z_init_appli.py</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/package_dev/z_init_appli.py">( open in notepad++ )</a></b></li><li><b><a href="/code_edit_B?code=./package_dev/requirements.txt&subdir='+scriptdir+'">requirements.txt</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/package_dev/requirements.txt">( open in notepad++ )</a></b></li>'
    '''
    for file in files:
        if 'route_' not in file and 'a_core_' not in file and file !='back' and '.txt' in file:
            print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<li><b><a href="/code_edit_B?code='+file+'&subdir='+scriptdir+'">'+file+'</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'">( open in notepad++ )</a></b></li>'
    '''
    html_output=html_output+'</ul><h3>Edit a function</h3><table border="1"><tbody>';
    for file in files:
        if 'route_' not in file and file !='back' and '.py' in file:
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<tr><td><b><a href="/code_edit_B?code='+file+'&subdir='+scriptdir+'">'+file+'</a></td><td><a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'">( open in notepad++ )</a></b></td><td><a href="/delete_file?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'&scriptdir='+scriptdir+'">( DELETE )</a></b></td><td><a href="/rename_file?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'&scriptdir='+scriptdir+'">( RENAME )</a></b></td><td><a href="/copy_function_to_central_B?filename=./code_app_scripts_to_import/'+scriptdir+'/'+file+'&scriptdir='+scriptdir+'">( cp 2 central )</a></b></td></td><td><a href="/duplicate_script?filename='+file+'&scriptdir='+scriptdir+'&type=function">(duplicate)</a></b></td><tr>' 
            
    html_output=html_output+'</tbody></table><h3>Edit a route</h3><table border="1"><tbody>';
    for file in files:
        if 'route_' in file and file !='back' and '.py' in file:
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<tr><td><b><a href="/code_edit_B?code='+file+'&subdir='+scriptdir+'">'+file+'</a></b></td><td><a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'">( open in notepad++ )</a></b></td><td><a href="/delete_file?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'&scriptdir='+scriptdir+'">( DELETE )</a></b></td><td><a href="/rename_file?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'&scriptdir='+scriptdir+'">( RENAME )</a></b></td><td><a href="/copy_route_to_central_B?filename=./code_app_scripts_to_import/'+scriptdir+'/'+file+'&scriptdir='+scriptdir+'">( cp 2 central )</a></b></td><td><a href="/duplicate_script?filename='+file+'&scriptdir='+scriptdir+'&type=route">(duplicate)</a></b></td><tr>'            
    html_output=html_output+'</tbody></table>';            
    env.level=env.level[:-1]
    return html_output
        

