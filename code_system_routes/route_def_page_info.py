# def_page_info***
@app.route('/page_info', methods=['GET'])
def page_info():
    '''
        Modified : 20250708
        
        description : display page_info.html
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route page_info() : >',bold=True))
    #loguer(env.level+' route page_info() : >')
    # print()
    route="/page_info"
    page=request.args.get('page')
    route=request.args.get('route').split('?')[0]
    # print()
    # print('page : ',yellow(page,bold=True))
    # print()
    # print('route : ',yellow(route,bold=True))
    url='/page_info?page='+page+'&route='+route
    with open('./result/home_url.txt','w') as file:
        file.write(url)
    chunk=route+'.py'
    chunk=chunk.replace('/','route_def_')
    # print()
    with open('./result/current_edited_imported_script.txt') as file:
        last_edited_script=file.read()          
    # print()
    # print('last_edited_script : ',yellow(last_edited_script,bold=True))
    # print()          
    env.level=env.level[:-1]
    return render_template('page_info.html',page=page,route=route,chunk=chunk,last_edited_script=last_edited_script)
    
