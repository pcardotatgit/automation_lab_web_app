#  def_bases***
@app.route('/bases', methods=['GET'])
def bases():
    '''
    Created : 2025-09-23T05:51:19.000Z
    description : display Databases Access Web Page
    '''
    route="/bases"
    env.level+='-'
    print('\n'+env.level,white('route bases() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route bases() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        route="/bases"
        title="FLASK APP GENERATOR"
        portfolio=''        
        if os.path.exists('./sqlite_databases_code/databases.txt'):     
            with open('./sqlite_databases_code/databases.txt') as file:
                text_content=file.read()
            databases=text_content.split('\n')
            for db in databases:
                if db!='':
                    with open('./sqlite_databases_code/'+db+'/db_description.txt') as file:   
                        description=file.read()
                    portfolio=portfolio+'''
                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/'''+db+'''_dashboard" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/'''+db+'''_dashboard">'''+db+'''</a></h3>
                                <p>'''+description+'''</p>
                            </article>
                        </div>            
'''            
        portfolio=portfolio+'''                        <div class="col-4 col-6-medium col-12-small">
                            <article class="box style2">
                                <a href="/reset_databases" class="image featured"><img src="../static/images/database0.png" alt="" /></a>
                                <h3><a href="/reset_databases">Reset Databases</a></h3>
                                <p>Reset All Databases</p>
                            </article>
                        </div>
'''
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
            <article id="portfolio" class="wrapper style3">
                <div class="container">
                    <header>
                        <h2>Databases</h2>
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
        loguer(env.level+' route END OF bases() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return output
