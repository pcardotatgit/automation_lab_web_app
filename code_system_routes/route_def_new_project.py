#  new_project***
@app.route('/new_project', methods=['GET','POST'])
def new_project():
    '''
    MODIFIED : 20250507
    display formular for create a new project 
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_project() : >',bold=True))
    loguer(env.level+' route new_project() : >')
    print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
    <form action="/new_project_create" method="GET">
    <b>route name : </b><input type="text"  id="route_name" name="name" /><br><br>
    <b>package directory location : </b><input type="text"  id="working_dir" name="working_dir" size= "80"/><br><br>
    <b>route description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output 
