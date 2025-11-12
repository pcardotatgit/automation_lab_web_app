#  def_format_log***
def format_log():
    '''
    MODIFIED : 2025-08-01

    description : read log file and create a formated file
    
    how to call it :
    '''
    route="/format_log"
    env.level+='-'
    print('\n'+env.level,white('def format_log() in analyse_application_logs.py : >\n',bold=True))
    #loguer(env.level+' def format_log() in analyse_application_logs.py : >')
    # ===================================================================    
    with open('./port.txt') as file:
        port=file.read()    
    with open('./debug/log.txt') as file:
        text_content=file.read()
    lines=text_content.split('\n')
    with open('./debug/parsed.txt','w') as file:
        for line in lines:
            if line != '' and '[-' in line:
                # print('\n line :\n',cyan(line+'\n',bold=True))               
                if "app.py" in line or "() : >" in line:
                    script=line.split('()')[0]
                    # print('\n script :',yellow(script+'\n',bold=True))
                    script=script.split(' ')[2]
                    # print('\n script :',yellow(script+'\n',bold=True))
                    line=line.replace('[','')
                    line=line.replace('- r','-; r')
                    line=line.replace('- d','-; d')            
                    line=line.replace(': >:','<<:')  
                    line=line.replace(': > at','<<: at')
                    if 'route' in line:
                        url=f";<<url:http://localhost:{port}/code_edit?code=route_def_{script}.py&type=route"
                    else:
                        url=f";<<url:http://localhost:{port}/code_edit?code=def_{script}.py&type=function"
                    # print('\n url :',green(url+'\n',bold=True))
                elif '???' in line:
                    line=line.replace('- var','-;')
                    line=line.split(' ???')[0]
                    line.replace(' : ','<<:')
                    line.replace(' = ','<<:')
                    url=';'
                else:
                    script=line.split('()')[0]
                    # print('\n script :',yellow(script+'\n',bold=True))
                    script=script.split(' ')[2]      
                    # print('\n script :',yellow(script+'\n',bold=True))
                    subdir=line.split('.py : >')[0]
                    # print('\n subdir 1 :',yellow(subdir+'\n',bold=True))
                    subdir=subdir.split('in ')[1]
                    # print('\n subdir 2 :',yellow(subdir+'\n',bold=True))
                    line=line.replace('[','')
                    line=line.replace('- r','-; r')
                    line=line.replace('- d','-; d')            
                    line=line.replace(': >','<<:')
                    line=line.replace(': > at','<<: at')
                    if 'route' in line:
                        url=f";<<url:http://localhost:{port}/code_edit_B?code=route_{script}.py&subdir={subdir}"
                    else:
                        url=f";<<url:http://localhost:{port}/code_edit_B?code=def_{script}.py&subdir={subdir}"       
                    # print('\n url :',green(url+'\n',bold=True))
                file.write('-'+line+url+';;;\n')
    # ===================================================================
    env.level=env.level[:-1]
    return 1
    
