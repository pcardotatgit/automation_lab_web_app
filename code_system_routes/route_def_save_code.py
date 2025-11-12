# def_save_code***
@app.route('/save_code', methods=['POST'])
def save_code():
    '''
        version 20250825
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route save_code() : >',bold=True))
    #loguer(env.level+' route save_code() : >')
    # print()
    python_code = request.form['code']
    # print()
    # print(' code:\n',yellow(python_code,bold=True))
    # print()
    # print()
    if python_code[0]=="#":
        filename=python_code.split("***")[0]
        python_code=python_code.split(",***subdir=***")[0]        
        if "def_"  in filename:
            filename=filename.replace("#  ","")
            filename=filename.replace("# ","")
            if '.py' not in filename:
                filename=filename+'.py'
            if '@app.route' in python_code:
                with open('./result/current_edited_route.txt','w') as file:
                    file.write('route_'+filename)            
                filename='./code_app_routes/route_'+filename  
            else:
                with open('./result/current_edited_function.txt','w') as file:
                    file.write(filename)            
                filename='./code_app_functions/'+filename      
                
            filename=filename.replace(" ","_")        
            filename=filename.replace("__","_")      
            # print()
            # print(' filename: ',yellow(filename,bold=True))
            # print()
            #filepath='./code_chunks/'+filename
            python_code=python_code.replace('\t','    ')
            lines=python_code.split('\n')
            output_lines=''
            for line in lines:
                line2=line.replace(' ','*')
                print(line2)
                if '                                      ' in line:
                    print(red('found 42',bold=True))
                    line=line.strip()
                    line='                                        '+line        
                elif '                                  ' in line:
                    print(red('found 38',bold=True))
                    line=line.strip()
                    line='                                    '+line         
                elif '                              ' in line:
                    print(red('found 34',bold=True))
                    line=line.strip()
                    line='                                '+line         
                elif '                              ' in line:
                    print(red('found 30',bold=True))
                    line=line.strip()
                    line='                                '+line        
                elif '                          ' in line:
                    print(red('found 26',bold=True))
                    line=line.strip()
                    line='                            '+line        
                elif '                      ' in line:
                    print(red('found 22',bold=True))
                    line=line.strip()
                    line='                        '+line                                   
                elif '                  ' in line:
                    print(red('found 18',bold=True))
                    line=line.strip()
                    line='                    '+line
                elif '              ' in line:
                    print(red('found 14',bold=True))
                    line=line.strip()
                    line='                '+line            
                elif '          ' in line:
                    print(red('found 10',bold=True))
                    line=line.strip()
                    line='            '+line             
                elif '      ' in line:
                    print(red('found 6',bold=True))
                    line=line.strip()
                    line='        '+line            
                else:
                    print(green('perfect',bold=True))
                line2=line.replace(' ','*')  
                print('new line :',cyan(line2,bold=True))
                output_lines=output_lines+line+'\n'
                #a=input('NEXT')
            output_lines=output_lines.replace('\n\n\n','\n\n')     
            output_lines=output_lines.replace('\n\n','\n')             
            with open(filename,"w") as file:
                file.write(output_lines)
    else:
        filename=python_code.split(",***subdir=***")[1]    
        python_code=python_code.split(",***subdir=***")[0]
        # print()
        # print(' python_code: ',yellow(python_code,bold=True))
        # print()         
        #filename=filename.replace("./","")
        # print()
        # print(' filename: ',yellow(filename,bold=True))
        # print() 
        python_code=python_code.replace('\n\n\n','\n\n')     
        python_code=python_code.replace('\n\n','\n')           
        with open(filename,"w") as file:
            file.write(python_code)    
    with open('./result/current_edited_script.txt',"w") as file:
        file.write(filename)     
    route="/save_code"
    PAGE_DESTINATION="code_saved.html"
    page_name="code_saved.html"
    env.level=env.level[:-1]
    return render_template('code_saved.html')
    
    
