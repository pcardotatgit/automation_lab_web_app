#  def_list_htmlpage***
@app.route('/list_htmlpage', methods=['GET','POST'])
def list_htmlpage():
    '''
    MODIFIED : 20250724

	list every html pages into the ./templates subfolder
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route list_htmlpage() : >',bold=True))
    #loguer(env.level+' route list_htmlpage() : >')
    # print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><h4>HTML PAGES :</h4><table border="1"><tbody>';
    files =[file for file in os.listdir('./code_app_html_templates')]
    ii=0
    function_list=[]
    for file in files:
        if '.html' in file:
            # print(' file : ',yellow(file,bold=True)) 
            html_output=html_output+'<tr><td><b><a href="/code_edit?code='+file+'&type=html">'+file+'</a></td><td><a href="/edit_html?filename=../code_app_html_templates/'+file+'">( open in notepad++)</a></td><td><a href="/del_html_file?filename=./code_app_html_templates/'+file+'">(DEL)</a></b></td><td><a href="/rename_file?filename=../code_app_html_templates/'+file+'&scriptdir=code_app_html_templates">(REN)</a></b></td><td><a href="/duplicate_html?filename='+file+'">(duplic)</a></b></td></tr>'
    env.level=env.level[:-1]
    html_output=html_output+'\n</tbody></table><br><a href="/stop">Click here to stop the App  </a></body><html>'
    return html_output
  
  
