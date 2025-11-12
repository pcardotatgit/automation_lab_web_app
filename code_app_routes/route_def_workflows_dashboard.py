#  def_workflows_dashboard***
@app.route('/workflows_dashboard', methods=['GET'])
def workflows_dashboard():
    '''
    Flask Route for the workflows_dashboard Database dashoard
    '''
    route="/workflows_dashboard"
    env.level+='-'
    print('\n'+env.level,white('route workflows_dashboard() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_dashboard() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
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
                    <li><a href="javascript:popup_window('/page_info?page=route_def_workflows_dashboard.py&route=/workflows_dashboard','page_info',700,600);">:</a></li>
        
                </ul>
            </nav>
        <!-- Portfolio -->
            <article id="portfolio" class="wrapper style3">
                <div class="container">
                    <header>
                        <h2>workflows Database</h2>
                    </header>
                    <div class="row">
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_create_db" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_create_db">Create Database</a></h3>
                                <p>Create the workflows Database</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_ingest_demo_data" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_ingest_demo_data">Ingest Demo Data</a></h3>
                                <p>Ingest Demo Data into DB</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_db_read_custom" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_db_read_custom">Read Database content</a></h3>
                                <p>Read DB content and get access to entries</p>
                            </article>
                        </div> 
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_db_clear" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_db_clear">Clear Database</a></h3>
                                <p>Delete Database content</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_db_ingest_csv" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_db_ingest_csv">Ingest a CSV file</a></h3>
                                <p>Ingest a CSV file</p>
                            </article>
                        </div>
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_db_add_entry" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_db_add_entry">Add Entry</a></h3>
                                <p>Add an Entry to Database</p>
                            </article>
                        </div>          
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/workflows_solution" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/workflows_solution">Install Solution</a></h3>
                                <p>Install Workflow solution</p>
                            </article>
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
        loguer(env.level+' route END OF workflows_dashboard() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return html_output
        