#  def_variables_db_clear***
@app.route('/variables_db_clear', methods=['GET'])
def variables_db_clear():
    '''
    Flask Route for the variables_db_clear Database Clearing / reset function
    '''
    route="/variables_db_clear"
    env.level+='-'
    print('\n'+env.level,white('route variables_db_clear() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route variables_db_clear() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./sqlite_databases_code/variables/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/variables.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :', db_details_dict["table_name"])
        conn=create_connection(database) # open connection to database
        if conn:
            # connection to database is OK
            c=conn.cursor()
            print(f'- Deleting table : {db_details_dict["table_name"]} =>')
            sql_request="drop table "+db_details_dict["table_name"]
            c.execute(sql_request)
            conn.commit()
            print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
            create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
            print(f'-- OK table {db_details_dict["table_name"]} reseted')     

        html_output='''<!DOCTYPE HTML>
<!-- description-->
<html>
    <head>
        <title>FLASK APP GENERATOR</title>
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
                
                    <li><a href="/">Back to main page</a></li>
                    <li><a href="/logout">log Out</a></li>
                    <li><a href="javascript:popup_window('/page_info?page=route_def_variables_db_clear.py&route=/variables_db_clear','page_info',700,600);">:</a></li>
        
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
							<p>Data in Database : variables had been cleaned</p>
                            <a href="/variables_dashboard" class="button small scrolly">Go to Dashboard for variables DB </a>
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
        loguer(env.level+' route END OF variables_db_clear() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
