#  def_new_route_from_library_B***
@app.route('/new_route_from_library_B', methods=['GET'])
def new_route_from_library_B():
    '''
    Created : 2025-06-14T10:21:33.000Z

    description : add a route from central library to imported script routes
    '''
    route="/new_route_from_library_B"
    env.level+='-'
    print()
    print(env.level,white('route new_route_from_library_B() in ***app.py*** : >',bold=True))
    loguer(env.level+' route new_route_from_library_B() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        script=request.args.get('script')
        print()
        print('script : ',script)
        scriptdir=request.args.get('scriptdir')
        print()
        print('scriptdir : ',scriptdir)        
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br><form action="/search_new_route_from_library_B" method="get"><input type="text" name="keyword"><input type="hidden" name="script" value="'+script+'"><input type="hidden" name="scriptdir" value="'+scriptdir+'"><input type="submit" value="Search"></form><ul>';
        files =[file for file in os.listdir('./code_central_routes')]
        function_list=[]
        for file in files:
              if '.txt' not in file:
                print(' file : ',yellow(file,bold=True)) 
                html_output=html_output+'<li><b>'+file+' : <a href="/copy_route_into_project_B?script='+file+'&scriptdir='+scriptdir+'">COPY to project</a>.---.<a href="/link_route_to_project_B?script='+file+'&scriptdir='+scriptdir+'">LINK to project</a></b>'
        env.level=env.level[:-1]
        html_output=html_output+'</ul><br><br><a href="/stop">Click here to stop the App  </a></body><html>'
        return html_output      
      
  
