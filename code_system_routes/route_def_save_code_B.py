# def_save_code_B***
@app.route('/save_code_B', methods=['POST'])
def save_code_B():
    '''
        version : 20250825
        save code for script to import
    '''
    env.level+='-'
    # print()
    # print(env.level,white('route save_code_B() : >',bold=True))
    #loguer(env.level+' route save_code_B() : >')
    # print()
    params = request.form['code']
    python_code=params.split(',***subdir=***')[0]
    # print()
    # print(' python_code:\n',yellow(python_code,bold=True))
    # print()
    # print()
    fichier = params.split(',***subdir=***')[1]
    # print()
    # print(' fichier:\n',yellow(fichier,bold=True))
    # print()
    # print()
    python_code=python_code.replace('\t','    ')
    lines=python_code.split('\n')
    output_lines=''
    for line in lines:
        line2=line.replace(' ','*')
        print(line2)
        if line.startswith('                                              '):
            print(red('found 46',bold=True))
            line=line.strip()
            line='                                            '+line          
        elif line.startswith('                                          '):
            print(red('found 42',bold=True))
            line=line.strip()
            line='                                        '+line        
        elif line.startswith('                                      '):
            print(red('found 38',bold=True))
            line=line.strip()
            line='                                    '+line         
        elif line.startswith('                                  '):
            print(red('found 34',bold=True))
            line=line.strip()
            line='                                '+line         
        elif line.startswith('                              '):
            print(red('found 30',bold=True))
            line=line.strip()
            line='                                '+line        
        elif line.startswith('                          '):
            print(red('found 26',bold=True))
            line=line.strip()
            line='                            '+line        
        elif line.startswith('                      '):
            print(red('found 22',bold=True))
            line=line.strip()
            line='                        '+line        
        elif line.startswith('                  '):
            print(red('found 18',bold=True))
            line=line.strip()
            line='                    '+line
        elif line.startswith('              '):
            print(red('found 14',bold=True))
            line=line.strip()
            line='                '+line            
        elif line.startswith('          '):
            print(red('found 10',bold=True))
            line=line.strip()
            line='            '+line             
        elif line.startswith('      '):
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
    with open(fichier,'w') as file:
        file.write(output_lines)
    liste=fichier.split('/')
    current_script=liste[-1]
    with open('./result/current_edited_script.txt',"w") as file:
        file.write(current_script)
    route="/save_code_B"
    PAGE_DESTINATION="code_saved.html"
    page_name="code_saved.html"
    env.level=env.level[:-1]
    return render_template('code_saved.html')
    
    
