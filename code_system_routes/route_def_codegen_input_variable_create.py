#  def_codegen_input_variable_create***
@app.route('/codegen_input_variable_create', methods=['GET'])
def codegen_input_variable_create():
    '''
    Created : 2025-09-22T07:51:41.000Z

    description : create code for input variables
    '''
    route="/codegen_input_variable_create"
    env.level+='-'
    print('\n'+env.level,white('route codegen_input_variable_create() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route codegen_input_variable_create() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # GET variable from calling web page
        variable=request.args.get('variable')
        print('\nvariable : ',variable)          
        output='''        # GET variable from calling web page
        '''+variable+'''=request.args.get("'''+variable+'''")
        print("\\n'''+variable+''' : ",'''+variable+''') 
        
        # POST variable 
        
        <input type="hidden" name="'''+variable+'''" >
         
        '''+variable+''' = request.form["'''+variable+'''"]
        print()
        print("\\n'''+variable+''' : ",'''+variable+''')  
        '''
        print('output :\n',cyan(output,bold=True))             
        message1="Message 1 :"
        image="../static/images/toolbox.png" 
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_codegen_input_variable_create"
        page_name="z_codegen_input_variable_create.html"
        loguer(env.level+' route END OF codegen_input_variable_create() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name,output=output)
        
