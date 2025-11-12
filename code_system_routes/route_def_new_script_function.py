# def_new_script_function***
@app.route('/new_script_function', methods=['GET','POST'])
def new_script_function():
    '''
    MODIFIED 20250605
    
    display formular for create a new_script_function of an external script
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_script_function() : >',bold=True))
    loguer(env.level+' route new_script_function() : >')
    print()
    scriptdir = request.args.get('scriptdir')
    print()
    print(' scriptdir:\n',yellow(scriptdir,bold=True))
    print()      
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><center><h3>new function for [ '''+scriptdir+'''.py ]</h3></center>
    <form action="/new_script_function_create" method="GET">
    <b>function name : </b><input type="text"  id="function_name" name="name" />-- Args :<input type="text"  id="args" name="args" value="()"/><br><br>
    <b>Function description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <input type="hidden"  id="scriptdir" name="scriptdir" value="'''+scriptdir+'''"/>
    <center><input type="submit" value="create"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output
    
    
