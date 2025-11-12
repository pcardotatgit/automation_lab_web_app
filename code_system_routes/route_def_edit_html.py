# def_edit_html***
@app.route('/edit_html', methods=['GET'])
def edit_html():
    env.level+='-'
    route="/edit_html"
    print()
    print(env.level,white('route edit_html() : >',bold=True))
    #loguer(env.level+' route edit_html() : >')
    filename=request.args.get('filename')
    print()
    print(yellow(f"- filename : {filename}",bold=True))
    command="start notepad++.exe ./code_app_html_templates/"+filename
    result = os.system(command)
    print()    
    with open('./result/home_url.txt') as file:
        home_url=file.read()   
    env.level=env.level[:-1]
    return render_template('OK.html',home_url=home_url)
   


