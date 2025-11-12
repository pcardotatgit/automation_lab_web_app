# def_edit_todo***
@app.route('/edit_todo', methods=['GET'])
def edit_todo():
    env.level+='-'
    route="/edit_todo"
    print()
    print(env.level,white('route edit_todo() : >',bold=True))
    #loguer(env.level+' route edit_todo() : >')
    command="start notepad++.exe ./templates/todo.txt"
    result = os.system(command)
    print()    
    with open('./result/home_url.txt') as file:
        home_url=file.read()   
    env.level=env.level[:-1]
    return render_template('OK.html',home_url=home_url)

        
