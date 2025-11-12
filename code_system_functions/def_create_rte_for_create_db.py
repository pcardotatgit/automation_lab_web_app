#  def_create_rte_for_create_db***
def create_rte_for_create_db(name):
    '''
    MODIFIED : 2025-10-29

    description : create a new files structure for management of a new database
    
    how to call it : result=create_rte_for_create_db(name)
    '''
    route="/create_rte_for_create_db"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_create_db() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_create_db() in app.py : >')
    # ===================================================================    
    db=name
    db_name=name.replace('./zbases/','')
    db_name=db_name.replace('.db','')
    name=name+'_create_db'
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'
    description='Flask Route for the '+name+' Database Create DB action'
    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print()
    print(' filename2 :\n',yellow(filename2,bold=True))
    print()
    print(' description :\n',yellow(description,bold=True))
    print()
    print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
    # check if file already exits
    with open('./code_architecture/app_functions.txt') as file:
        text_content2=file.read()    
    fichier_route = Path('./code_app_routes/route_def_'+name+'.py')    
    if fichier_route.is_file() or filename in text_content2:
        print(filename+' already exists ! Choose another name')
        message1="ALREADY EXIST"
        image="../static/images/nok.png" 
        message2="Choose another name"
        message3="/home"
        message4="Back Home"          
        PAGE_DESTINATION="operation_done"
        page_name="z_operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return 0
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        route='/'+db+"_create_db"
        title="FLASK APP GENERATOR"
        with open('./sqlite_databases_code/'+db+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))        
        len_columns=len(db_details_dict['columns'])-1
        menu='''
                    <li><a href="/">Back to main page</a></li>
                    <li><a href="/logout">log Out</a></li>
                    <li><a href="javascript:popup_window('/page_info?page=route_def_bases.py&route='''+route+'''','page_info',700,600);">:</a></li>
        '''       
        output='''<!DOCTYPE HTML>
<!-- description-->
<html>
    <head>
        <title>'''+title+'''</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="../static/assets/css/main.css" />
    <script>
        function popup_window( url, id, width, height )
        {
            //extract the url parameters if any, and pass them to the called html
            var tempvar=document.location.toString(); // fetch the URL string
            var passedparams = tempvar.lastIndexOf("?");
            if(passedparams > -1)
                url += tempvar.substring(passedparams);
            popup = window.open( url, id, 'toolbar=no,scrollbars=yes,location=yes,statusbar=yes,menubar=no,resizable=yes,width=' + width + ',height=' + height + '' );
            popup.focus();
        }
    </script>
    </head>
    <body class="is-preload">
        <!-- Nav -->
            <nav id="nav">
                <ul>
                '''+menu+'''
                </ul>
            </nav>
        <!-- Portfolio -->
			<article id="top" class="wrapper style1">
				<div class="container">
					<div class="row">
						<div class="col-4 col-5-large col-12-medium">
							<span class="image fit"><img src="../static/images/ok.png" alt="" /></span>
						</div>
						<div class="col-8 col-7-large col-12-medium">
							<header>
								<h1><strong> Database :'''+db+''', was created</strong></h1>
							</header>
							<p>The SQLITE had been created in ./z_bases</p>
                            <a href="/'''+db+'''_dashboard" class="button small scrolly">Go to Dashboard for '''+db+''' DB </a>
						</div>						
					</div>				
				</div>
			</article>
        <!-- Scripts -->
            <script src="../static/assets/js/jquery.min.js"></script>
            <script src="../static/assets/js/jquery.scrolly.min.js"></script>
            <script src="../static/assets/js/init.js"></script>
            <script src="../static/assets/js/browser.min.js"></script>
            <script src="../static/assets/js/breakpoints.min.js"></script>
            <script src="../static/assets/js/util.js"></script>
            <script src="../static/assets/js/main.js"></script>
    </body>
</html>
'''
        text_content='''#  def_'''+db+'''_create_db***
@app.route('/'''+db+'''_create_db', methods=['GET'])
def '''+db+'''_create_db():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_create_db"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_create_db() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_create_db() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        with open(\'./sqlite_databases_code/'''+db+'''/db_details.txt\') as file:
            db_details_dict=json.loads(file.read())
        print(\'db_details_dict : \\n\',yellow(db_details_dict,bold=True))
        file=open('./sqlite_databases_code/'''+db+'''/init/'''+db+'''.csv','w')
        ligne_out=\'\'
        len_columns=len(db_details_dict[\'columns\'])-1
        i=0        
        for col in db_details_dict[\'columns\']:
            if i<len_columns:
                ligne_out=ligne_out+col+\','
            else:
                ligne_out=ligne_out+col
            i+=1
        file.write(ligne_out+\'\\n\')
        for i in range (0,10):
            ligne_out=\'''' 
        i=0
        for col in db_details_dict['columns']:
            if i<len_columns:
                text_content=text_content+col+"'+str(i)+','+'"
            else:
                text_content=text_content=text_content+col+"'+str(i)"
            i+=1        
        text_content=text_content+'''           
            file.write(ligne_out+\'\\n\')
        file.close()  
        create_db_and_table(db_details_dict[\'db_name\'],db_details_dict[\'table_name\'])
        html_output=\'\'\''''+output+'''\'\'\'
        loguer(env.level+\' route END OF '''+db+'''_create_db() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
'''        
        filename='./code_app_routes/route_def_'+db+'_create_db.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        result=1
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_create_db() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
