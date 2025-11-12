#  def_run_workflow***
@app.route('/run_workflow', methods=['GET'])
def run_workflow():
    '''
    Created : 2025-10-31T13:52:25.000Z
    description : Go to run workflow
    '''
    route="/run_workflow"
    env.level+='-'
    print('\n'+env.level,white('route run_workflow() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route run_workflow() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/step.txt','w') as file:
            file.write('Step 01')
        message1="Ready to run the workflow"
        image="../static/images/automation.png"
        message2="Run the workflow step by step"
        message3="/go_run_workflow"
        message4="GO Run Workflow"
        PAGE_DESTINATION="z_run_workflow"
        page_name="z_run_workflow.html"
        loguer(env.level+' route END OF run_workflow() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
