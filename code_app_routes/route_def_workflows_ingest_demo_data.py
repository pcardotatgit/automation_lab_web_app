#  def_workflows_ingest_demo_data***
@app.route('/workflows_ingest_demo_data', methods=['GET'])
def workflows_ingest_demo_data():
    '''
    Flask Route for the workflows_ingest_demo_data Database Ingest demo data
    '''
    route="/workflows_ingest_demo_data"
    env.level+='-'
    print('\n'+env.level,white('route workflows_ingest_demo_data() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_ingest_demo_data() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./sqlite_databases_code/workflows/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/workflows.db'
        database=database.replace("\\","/")
        print('database is :',database)
        lines=[]    
        file='./sqlite_databases_code/workflows/init/workflows.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            indexA=0
            print('workflows table =>\n')
            conn=create_connection(database) # open connection to database            
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    sqlite_data=[indexA]
                    sqlite_data=(indexA,row[0] ,row[1] ,row[2] ,row[3] ,row[4] ,row[5])
                    sql_add="INSERT OR IGNORE into workflows (`index`,workflow_name,step,step_name,input,output,comment) VALUES (?,?,?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()        

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
                    <li><a href="javascript:popup_window('/page_info?page=route_def_workflows.py&route=/workflows_ingest_demo_data_ingest_demo_data','page_info',700,600);">:</a></li>
        
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
								<h1><strong>Demo Data ingested</strong></h1>
							</header>
							<p>Demo Data ingested into Database :workflows</p>
                            <a href="/workflows_dashboard" class="button small scrolly">Go to Dashboard for workflows DB </a>
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
        loguer(env.level+' route END OF workflows_ingest_demo_data() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
