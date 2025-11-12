#  def_dtree***
@app.route('/dtree', methods=['GET'])
def dtree():
    '''
    Created : 2025-07-18T14:58:59.000Z

    description : call the dtree function that will create the dtree graph in the template subfolder
    '''
    route="/dtree"
    env.level+='-'
    print()
    print(env.level,white('route dtree() in app.py  : >\n',bold=True))
    loguer(env.level+' route dtree() in app.py  : > ')
    print()
    global api_key
    global orgID
    global host
    global network_id
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename=request.args.get('filename')
        filename=filename.split('***')[0]
        print()
        print('filename : ',filename)  
        html_content=go_analyse_json(filename)
        # ===================================================================
        env.level=env.level[:-1]
        return html_content
        

