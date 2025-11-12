# def_goto_script***
@app.route('/goto_script', methods=['GET'])
def goto_script():
    env.level+='-'
    # print()
    # print(env.level,white('route goto_script() : >',bold=True))
    #loguer(env.level+' route goto_script() : >')
    # print()
    scriptdir = request.args.get('script')
    scriptdir=scriptdir.replace('.py','')
    # print()
    # print(' scriptdir :\n',yellow(scriptdir,bold=True))
    # print()    
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br><b><a href="/new_script_function_create?scriptdir='+scriptdir+'">Create a new function for [ '+scriptdir+'.py ]</a></b><h3>Edit a score chunks</h3><ul>';
    files =[file for file in os.listdir('./code_app_scripts_to_import/'+scriptdir)]
    ii=0
    function_list=[]
    for file in files:
        if 'route_' not in file and 'a_core_' not in file and file !='back':
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<li><b><a href="/code_edit?code=.../code_app_scripts_to_import/'+scriptdir+'/'+file+'&type=function">'+file+'</a>.---.<a href="/edit_html?filename=../code_app_scripts_to_import/'+scriptdir+'/'+file+'">( open in notepad++ )</b></li>'
    html_output=html_output+'<h3>Edit a route</h3>';
    html_output=html_output+'<h3>Edit a function</h3>';
    env.level=env.level[:-1]
    return html_output
        

