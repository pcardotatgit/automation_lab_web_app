#  def_account_keys_db_read***
@app.route('/account_keys_db_read', methods=['GET'])
def account_keys_db_read():
    '''
    Flask Route for the account_keys_db_read Database Read DB content function
    '''
    route="/account_keys_db_read"
    env.level+='-'
    print('\n'+env.level,white('route account_keys_db_read() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route account_keys_db_read() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        keyword=''
        keyword=request.args.get("keyword")
        print("\nkeyword : ",keyword)      
        with open('./sqlite_databases_code/account_keys/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/account_keys.db'
        database=database.replace("\\","/")
        print('database is :',database)
        # sqlite:///:memory: (or, sqlite://)
        # sqlite:///relative/path/to/file.db
        # sqlite:////absolute/path/to/file.db
        db_name = "account_keys.db"
        table_name = db_details_dict["table_name"]
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','name','type','username','password','key','comment']]
        #save result to csv file
        out_df.to_csv(r'./result/account_keys.csv')
        df = DataFrame(out_df)
        #print (df)
        select_options=''
        res = df.values.tolist()
        for item in res:
            if keyword:
                if keyword in item:
                    select_options=select_options+'<option value="'+str(item[0])+'">'+item[1]+'</option>'
            else:
                select_options=select_options+'<option value="'+str(item[0])+'">'+item[1]+'</option>'     
        print('=========================================')
        columns="name,type,username,password,key,comment"                
        print('DONE')        
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
                    <li><a href="/account_keys_dashboard">Back to Database Page</a></li>
                    <li><a href="/logout">log Out</a></li>
                    <li><a href="javascript:popup_window('/page_info?page=route_def_account_keys_db_read.py&route=/account_keys_db_read','page_info',700,600);">:</a></li>
        
                </ul>
            </nav>
			<article id="indic_list" class="wrapper style4">
				<div class="container medium">
					<header>
						<h2>Database Content</h2>
                        <p>Select a Row</p>
						<p>Or refine Search by keyword (in any columns)</p>
					</header>
					<div class="row">
						<div class="col-12">
							<form method="get" action="/db_row_details">
                            	<input type="hidden" name="database" value="account_keys">
                            	<input type="hidden" name="table" value="account_keys"> 
                                <input type="hidden" name="columns" value="'''+columns+'''">                                
								<div class="row">
									<div class="col-12">
										<select id="row" name="row">
                                            '''+select_options+'''           
                                        </select>
									</div>      
									<div class="col-12">
										<ul class="actions">
                                            <li><input type="submit" value="Select this row" class="button small scrolly" /></li>
										</ul>
									</div>                                    
								</div>
							</form>
						</div>    
                        <form method="get" action="/account_keys_db_read">
                            <div class="row">                        
                                <div class="col-6 col-12-small">
                                    <h3>Search Keyword :</h3>
                                </div>                                
                                <div class="col-6 col-12-small">
                                    <input type="text"  id="keyword" name="keyword" placeholder="keyword" />
                               </div>  
                                <div class="col-12">      
                                    <ul class="actions">
                                        <input type="submit" value="Search" class="button small scrolly" />
                                    </ul>
                                </div> 
                        </form>
					</div>
					<footer>
						<ul id="copyright">
							
						</ul>
					</footer>
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
        loguer(env.level+' route END OF account_keys_db_read() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
