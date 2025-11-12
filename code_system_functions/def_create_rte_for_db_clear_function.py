#  def_create_rte_for_db_clear_function***
def create_rte_for_db_clear_function(name):
    '''
    MODIFIED : 2025-10-29

    description : Ingest demo data into the database
    
    how to call it : result=create_rte_for_db_clear_function(name)
    '''
    route="/create_rte_for_db_clear_function"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_db_clear_function() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_db_clear_function() in app.py : >')
    # ===================================================================    
    db=name
    db_name=name.replace('./zbases/','')
    db_name=db_name.replace('.db','')
    name=name+'_db_clear'
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'
    description='Flask Route for the '+name+' Database Clearing / reset function'
    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print(' filename2 :\n',yellow(filename2,bold=True))
    print()
    print(' description :\n',yellow(description,bold=True))
    print()
    print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
    # check if file already exits
    with open('./code_architecture/app_routes.txt') as file:
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
        route="/"+db+"_db_clear"
        title="FLASK APP GENERATOR"
        with open('./sqlite_databases_code/'+db+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))       
        
        menu='''
                    <li><a href="/">Back to main page</a></li>
                    <li><a href="/logout">log Out</a></li>
                    <li><a href="javascript:popup_window('/page_info?page=route_def_'''+db+'''_db_clear.py&route='''+route+'''','page_info',700,600);">:</a></li>
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
								<h1><strong>Database Content Deleted</strong></h1>
							</header>
							<p>Data in Database : '''+db+''' had been cleaned</p>
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
        text_content='''#  def_'''+db+'''_db_clear***
@app.route('/'''+db+'''_db_clear', methods=['GET'])
def '''+db+'''_db_clear():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_db_clear"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_db_clear() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_db_clear() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        with open(\'./sqlite_databases_code/'''+db+'''/db_details.txt\') as file:
            db_details_dict=json.loads(file.read())
        print(\'db_details_dict : \\n\',yellow(db_details_dict,bold=True))
        database = os.getcwd()+\'/z_bases/'''+db+'''.db\'
        database=database.replace("\\\\","/")
        print(\'database is :\',database)
        print(\'table is :\', db_details_dict["table_name"])
        conn=create_connection(database) # open connection to database
        if conn:
            # connection to database is OK
            c=conn.cursor()
            print(f\'- Deleting table : {db_details_dict["table_name"]} =>\')
            sql_request="drop table "+db_details_dict["table_name"]
            c.execute(sql_request)
            conn.commit()
            print(\'-- OK DONE : Deleted table : \'+db_details_dict["table_name"])
            create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
            print(f\'-- OK table {db_details_dict["table_name"]} reseted\')     
'''        

        text_content=text_content+'''
        html_output=\'\'\''''+output+'''\'\'\'
        loguer(env.level+\' route END OF '''+db+'''_db_clear() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
'''        
        filename='./code_app_routes/route_def_'+db+'_db_clear.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        result=1
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_db_clear_function() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
