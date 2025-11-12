# def_parse_config***
def parse_config(text_content):
    env.level+='-'
    print()
    print(env.level,white('def parse_config() in app.py : >',bold=True))
    loguer(env.level+' def parse_config()  in app.py : >')
    print()
    text_lines=text_content.split('\n')
    conf_result=['','','','','']
    for line in text_lines:
        print(green(line,bold=True))
        if 'api_key' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[0]=line.split('=')[1]
                conf_result[0]=conf_result[0].replace('"','')
                conf_result[0]=conf_result[0].replace("'","")
                conf_result[0]=conf_result[0].strip()
            else:
                conf_result[0]=""
        elif 'network_id' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[1]=line.split('=')[1]
                conf_result[1]=conf_result[1].replace('"','')
                conf_result[1]=conf_result[1].replace("'","")
                conf_result[1]=conf_result[1].strip()
            else:
                conf_result[1]=""
        elif 'host' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[2]=line.split('=')[1]
                conf_result[2]=conf_result[2].replace('"','')
                conf_result[2]=conf_result[2].replace("'","")
                conf_result[2]=conf_result[2].strip()
            else:
                conf_result[2]=""
        elif 'orgID' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[3]=line.split('=')[1]
                conf_result[3]=conf_result[3].replace('"','')
                conf_result[3]=conf_result[3].replace("'","")
                conf_result[3]=conf_result[3].strip()
            else:
                conf_result[3]=""
        elif 'profil_name' in line:
            words=line.split('=')
            if len(words)==2:
                conf_result[4]=line.split('=')[1]
                conf_result[4]=conf_result[4].replace('"','')
                conf_result[4]=conf_result[4].replace("'","")
                conf_result[4]=conf_result[4].strip()
            else:
                conf_result[4]=""
    print(yellow(conf_result))
    env.level=env.level[:-1]
    return conf_result


