# def_list_external_scripts_B***
@app.route('/list_external_scripts', methods=['GET','POST'])
def list_external_scripts():
    '''
        version : 20250929
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route list_external_scripts() : >',bold=True))
    #loguer(env.level+' route list_external_scripts() : >')
    # print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    with open('./result/current_edited_imported_script.txt') as file:
        last_edited_script=file.read()  
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><br><a href="/goto_script_B?script='+last_edited_script+'&type=route">Last Edited :'+last_edited_script+'</a><br><a href="/new_script_to_import">Create a new script</a><br><a href="edit_html?filename=../code_architecture/imported_scripts.txt">Edit the list ( notepad++ )</a><br><br><b><u>DELETE A SCRIPT :</u> remove the script name from the list ( link above : ./code_architecture/imported_scripts.txt )  and manually delete the directory structure in ./code_app_scripts_to_import.</b><h3>Select a script</h3><ul>';
    with open('./code_architecture/imported_scripts.txt') as file:
        for line in file:
            # print(' file : ',yellow(line,bold=True)) 
            html_output=html_output+'<li><b><a href="/goto_script_B?script='+line+'&type=route">'+line+'</a></b></li>'
    env.level=env.level[:-1]
    html_output=html_output+'\n</ul></body><html>'
    return html_output
    

