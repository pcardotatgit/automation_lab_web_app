#  def_create_rte_for_db_read_function***
def create_rte_for_db_read_function(name):
    '''
    MODIFIED : 2025-09-30

    description : Read SQLITE DB Content and display result into a select box
    
    how to call it : create_rte_for_db_read_function(db_name)
    '''
    route="/create_rte_for_db_read_function"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_db_read_function() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_db_read_function() in app.py : >')
    # ===================================================================    
    db=name
    db_name=name.replace('./zbases/','')
    db_name=db_name.replace('.db','')
    name=name+'_db_read'
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'
    description='Flask Route for the '+name+' Database Read DB content function'
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
        route="/"+db+"_db_read"
        title="FLASK APP GENERATOR"
        with open('./sqlite_databases_code/'+db+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))       
        
        menu='''
                    <li><a href="/">Back to main page</a></li>
                    <li><a href="/'''+db+'''_dashboard">Back to Database Page</a></li>
                    <li><a href="/logout">log Out</a></li>
                    <li><a href="javascript:popup_window('/page_info?page=route_def_'''+db+'''_db_read.py&route='''+route+'''','page_info',700,600);">:</a></li>
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
                            	<input type="hidden" name="database" value="'''+db+'''">
                            	<input type="hidden" name="table" value="'''+db_details_dict['table_name']+'''"> 
                                <input type="hidden" name="columns" value="\'\'\'+columns+\'\'\'">                                
								<div class="row">
									<div class="col-12">
										<select id="row" name="row">
                                            \'\'\'+select_options+\'\'\'           
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
                        <form method="get" action="/'''+db+'''_db_read">
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
        text_content='''#  def_'''+db+'''_db_read***
@app.route('/'''+db+'''_db_read', methods=['GET'])
def '''+db+'''_db_read():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_db_read"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_db_read() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_db_read() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        keyword=\'\'
        keyword=request.args.get("keyword")
        print("\\nkeyword : ",keyword)      
        with open(\'./sqlite_databases_code/'''+db+'''/db_details.txt\') as file:
            db_details_dict=json.loads(file.read())
        print(\'db_details_dict : \\n\',yellow(db_details_dict,bold=True))
        database = os.getcwd()+\'/z_bases/'''+db+'''.db\'
        database=database.replace("\\\\","/")
        print(\'database is :\',database)
        # sqlite:///:memory: (or, sqlite://)
        # sqlite:///relative/path/to/file.db
        # sqlite:////absolute/path/to/file.db
        db_name = "'''+db+'''.db"
        table_name = db_details_dict["table_name"]
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[[\'index',\''''        
        len_columns=len(db_details_dict['columns'])-1
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+"','"
            else:
                text_content=text_content+col+"']]"
            i+=1
        text_content=text_content+'''
        #save result to csv file
        out_df.to_csv(r\'./result/'''+db+'''.csv\')
        df = DataFrame(out_df)
        #print (df)
        select_options=\'\'
        res = df.values.tolist()
        for item in res:
            if keyword:
                if keyword in item:
                    select_options=select_options+\'<option value="\'+str(item[0])+\'">\'+item[1]+\'</option>\'
            else:
                select_options=select_options+\'<option value="\'+str(item[0])+\'">\'+item[1]+\'</option>\'     
        print(\'=========================================\')
        columns="'''        
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+","
            else:
                text_content=text_content+col
            i+=1
        text_content=text_content+'''"                
        print(\'DONE\')        
        html_output=\'\'\''''+output+'''\'\'\'
        loguer(env.level+\' route END OF '''+db+'''_db_read() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]    
        return html_output
'''        
        filename='./code_app_routes/route_def_'+db+'_db_read.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        result=1
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_db_read_function() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
