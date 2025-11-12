#  def_product_api_call***
@app.route('/product_api_call', methods=['GET','POST'])
def product_api_call():
    '''
    Created : 2025-10-26T10:01:07.000Z

    description : run the CSE get computer API formular
    '''
    route="/product_api_call"
    env.level+='-'
    print('\n'+env.level,white('route product_api_call() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route product_api_call() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:  
        name = request.form.get("name")
        print("\nname : ",name)
        base_url = request.form.get("base_url")
        print("\nbase_url : ",base_url)
        relative_url = request.form.get("relative_url")
        print("\nrelative_url : ",relative_url)
        api_docummentation = request.form.get("api_docummentation")
        print("\napi_docummentation : ",api_docummentation)  
        short_description = request.form.get("short_description")
        print("\nshort_description : ",short_description)  
        payload = request.form.get("payload")
        print("\npayload : ",payload) 
        method = request.form.get("method")
        print("\nmethod : ",method)  
        header = request.form.get("header")
        print("\nheader : ",header)  
        body = request.form.get("body")
        print("\nbody : ",body)  
        params = request.form.get("params")
        print("\nparams : ",params)  
        parameters = request.form.get("parameters")
        print("\nparameters : ",parameters)  
        authentication_profile = request.form.get("authentication_profile")
        print("\nauthentication_profile : ",authentication_profile)  
        inputs = request.form.get("inputs")
        print("\ninputs : ",inputs)  
        outputs = request.form.get("outputs")
        print("\noutputs : ",outputs)          
        PAGE_DESTINATION="z_product_api_call"
        page_name="z_product_api_call.html"
        loguer(env.level+' route END OF product_api_call() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,name=name,base_url=base_url,relative_url=relative_url,api_docummentation=api_docummentation,short_description=short_description,payload=payload,method=method,header=header,body=body,params=params,parameters=parameters,authentication_profile=authentication_profile,inputs=inputs,outputs=outputs)
        
