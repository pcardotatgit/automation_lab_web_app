#  def_new_script_to_import***
@app.route('/new_script_to_import', methods=['GET','POST'])
def route_def_new_script_to_import():
    '''
    MODIFIED : 20250507
    display formular for create a new script to import  
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_script_to_import() : >',bold=True))
    loguer(env.level+' route new_script_to_import() : >')
    print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
    <form action="/new_script_to_import_create" method="GET">
    <b>script name : </b><input type="text"  id="script_name" name="name" /><br><br>
    <b>script description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output 
