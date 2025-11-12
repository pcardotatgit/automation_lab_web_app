#  new_route***
@app.route('/new_route', methods=['GET','POST'])
def new_route():
    '''
    MODIFIED : 20250507
    display formular for create a new route  
    '''
    env.level+='-'
    print()
    print(env.level,white('route new_route() : >',bold=True))
    loguer(env.level+' route new_route() : >')
    print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
    <form action="/new_route_create" method="GET">
    <b>route name : </b><input type="text"  id="route_name" name="name" /><br><br>
    <b>route description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output 
