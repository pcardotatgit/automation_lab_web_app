# def_new_script_route***
@app.route('/new_script_route', methods=['GET','POST'])
def new_script_route():
    '''
    MODIFIED 20250324
    
    display formular for create a new_script_route of an external script
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_script_route() : >',bold=True))
    loguer(env.level+' route new_script_route() : >')
    print()
    scriptdir = request.args.get('scriptdir')
    print()
    print(' scriptdir:\n',yellow(scriptdir,bold=True))
    print()      
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><center><h3>new route for [ '''+scriptdir+'''.py ]</h3></center>
    <form action="/new_script_route_create" method="GET">
    <b>route name : </b><input type="text"  id="function_name" name="name" /><br><br>
    <b>route description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <input type="hidden"  id="scriptdir" name="scriptdir" value="'''+scriptdir+'''"/>
    <center><input type="submit" value="create"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output
    
    
