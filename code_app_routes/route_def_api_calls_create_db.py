#  def_api_calls_create_db***
@app.route('/api_calls_create_db', methods=['GET'])
def api_calls_create_db():
    '''
    Flask Route for the api_calls_create_db Database Create DB action
    '''
    route="/api_calls_create_db"
    env.level+='-'
    print('\n'+env.level,white('route api_calls_create_db() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route api_calls_create_db() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./sqlite_databases_code/api_calls/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        file=open('./sqlite_databases_code/api_calls/init/api_calls.csv','w')
        ligne_out=''
        len_columns=len(db_details_dict['columns'])-1
        i=0        
        for col in db_details_dict['columns']:
            if i<len_columns:
                ligne_out=ligne_out+col+','
            else:
                ligne_out=ligne_out+col
            i+=1
        file.write(ligne_out+'\n')
        for i in range (0,10):
            ligne_out='name'+str(i)+','+'fqdn'+str(i)+','+'relative_url'+str(i)+','+'documentation'+str(i)+','+'method'+str(i)+','+'description'+str(i)+','+'payload'+str(i)+','+'header'+str(i)+','+'body'+str(i)+','+'query_params'+str(i)+','+'custom_variables'+str(i)+','+'authentication_profile'+str(i)+','+'inputs_variables'+str(i)+','+'output_variables'+str(i)           
            file.write(ligne_out+'\n')
        file.close()  
        create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
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
                    <li><a href="javascript:popup_window('/page_info?page=route_def_bases.py&route=/api_calls_create_db','page_info',700,600);">:</a></li>
        
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
								<h1><strong> Database :api_calls, was created</strong></h1>
							</header>
							<p>The SQLITE had been created in ./z_bases</p>
                            <a href="/api_calls_dashboard" class="button small scrolly">Go to Dashboard for api_calls DB </a>
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
        loguer(env.level+' route END OF api_calls_create_db() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
