#  def_create_rte_for_db_dashboard***
def create_rte_for_db_dashboard(name):
    '''
    MODIFIED : 2025-09-29
    description : create a new files structure for management of a new database
    
    how to call it : result=create_rte_for_db_dashboard(name)
    '''
    route="/create_rte_for_db_dashboard"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_db_dashboard() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_db_dashboard() in app.py : >')
    # ===================================================================    
    db=name
    name=name+'_dashboard'
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'
    description='Flask Route for the '+name+' Database dashoard'
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
    with open('./code_architecture/app_routes.txt') as file:
        text_content2=file.read()
    fichier_route = Path('./code_app_routes/route_def_'+name+'.py')    
    if fichier_route.is_file() or filename in text_content2:
        print(filename+' already exists ! Choose another name')
        image="../static/images/nok.png"
        message2="Flask Route for this DB already exist"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="operation_done"
        page_name="z_operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return 0
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        route='/'+db+"_dashboard"
        title="FLASK APP GENERATOR"
        portfolio='''
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_create_db" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_create_db">Create Database</a></h3>
                                <p>Create the '''+db+''' Database</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_ingest_demo_data" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_ingest_demo_data">Ingest Demo Data</a></h3>
                                <p>Ingest Demo Data into DB</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_db_read" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_db_read">Read Database content</a></h3>
                                <p>Read DB an Create a CSV result</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_db_clear" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_db_clear">Clear Database</a></h3>
                                <p>Delete Database content</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_db_ingest_csv" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_db_ingest_csv">Ingest a CSV file</a></h3>
                                <p>Ingest a CSV file</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_db_add_entry" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_db_add_entry">Add Entry</a></h3>
                                <p>Add an Entry to Database</p>
                            </article>
                        </div>
            '''
        menu='''
                    <li><a href="/">Back to main page</a></li>
                    <li><a href="/logout">log Out</a></li>
                    <li><a href="javascript:popup_window('/page_info?page=route_def_'''+db+'''_dashboard.py&route='''+route+'''','page_info',700,600);">:</a></li>
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
            <article id="portfolio" class="wrapper style3">
                <div class="container">
                    <header>
                        <h2>'''+db+''' Database</h2>
                    </header>
                    <div class="row">'''
        output=output+portfolio
        output=output+'''
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
        text_content='''#  def_'''+db+'''_dashboard***
@app.route('/'''+db+'''_dashboard', methods=['GET'])
def '''+db+'''_dashboard():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_dashboard"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_dashboard() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_dashboard() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        html_output=\'\'\''''+output+'''\'\'\'
        loguer(env.level+\' route END OF '''+db+'''_dashboard() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]
        return html_output
        '''
        filename='./code_app_routes/route_def_'+db+'_dashboard.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')
        result=1
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_db_dashboard() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
