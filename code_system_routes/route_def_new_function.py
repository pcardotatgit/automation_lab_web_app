# def_new_function***
@app.route('/new_function', methods=['GET','POST'])
def new_function():
    '''
    MODIFIED 20250605
    
    display formular for create a new function
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_function() : >',bold=True))
    loguer(env.level+' route new_function() : >')
    print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
    <form action="/new_function_create" method="GET">
    <b>function name : </b><input type="text"  id="function_name" name="name" width="80"/>-- Args :<input type="text"  id="args" name="args" value="()"/><br><br>
    <b>Function description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output
    
    
