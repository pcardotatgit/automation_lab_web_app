#  def_icon***
def icon(line):
    '''
    MODIFIED : 2025-07-19T14:16:41.000Z

    description : select the icon at the begining of the line
    
    how to call it :
    '''
    route="/icon"
    env.level+='-'
    print('\n'+env.level,white('def icon() in analyse_application_logs.py : >\n',bold=True))
    loguer(env.level+' def icon() in analyse_application_logs.py : >')
    # ===================================================================    
    if ';!;' in line:
        icone='img/warning2.gif'  
    elif ';q;' in line:
        icone='img/icon_question.gif'  
    elif ';t;' in line:
        icone='img/icon_todo.gif'  
    elif ';error;' in line:
        icone='img/icon_not_active.png'   
    elif ';checknok;' in line:
        icone='img/check_no.gif' 
    elif ';cnk;' in line:
        icone='img/checkbox_no_full.gif'         
    elif ';checkok;' in line:
        icone='img/checkbox_ok.gif' 
    elif ';checkokfull;' in line:
        icone='img/checkbox_ok_full.gif'       
    elif ';checknokfull;' in line:
        icone='img/checkbox_no_full.gif' 
    elif ';cok;' in line:
        icone='img/checkbox_ok_full.gif'         
    elif ';infected;' in line:
        icone='img/trojan.gif'     
    elif ';block;' in line:
        icone='img/red_cross.gif'     
    elif ';allow;' in line:
        icone='img/check_ok_green.gif'  
    elif ';alert;' in line:
        icone='img/alarm.gif'  
    elif ';task;' in line:
        icone='img/task.gif' 
    elif ';connected;' in line:
        icone='img/icon_connected.png'    
    elif ';disconnected;' in line:
        icone='img/icon_disconnected.png'  
    elif ';off;' in line:
        icone='img/icon_unavailable.png'  
    elif ';eth;' in line:
        icone='img/icon_wired.png'   
    elif ';wifi;' in line:
        icone='img/icon_wireless.png'  
    elif ';book;' in line:
        icone='img/book.png' 
    elif ';cmd;' in line:
        icone='img/cmd.png' 
    elif ';python;' in line:
        icone='img/python.gif'   
    elif ';py;' in line:
        icone='img/python.gif' 
    elif ';firefox;' in line:
        icone='img/firefox.gif'   
    elif ';protect;' in line:
        icone='img/protect.gif'
    elif ';if;' in line:
        icone='img/if_block.gif'   
    elif ';loop;' in line:
        icone='img/loop.gif'  
    elif ';http_target;' in line:
        icone='img/http_target.gif'  
    elif ';http;' in line:
        icone='img/http_target.gif'      
    elif ';stop;' in line:
        icone='img/stop.gif' 
    elif ';info;' in line:
        icone='img/info.gif' 
    elif ';del;' in line:
        icone='img/trash.gif'   
    elif ';read;' in line:
        icone='img/topic.png'    
    elif ';start;' in line:
        icone='img/start.gif'     
    elif ';root;' in line:
        icone='img/base.gif'   
    elif ';folder;' in line:
        icone='img/folder.gif'   
    elif ';folderopen;' in line:
        icone='img/folderopen.gif'   
    elif ';node;' in line:
        icone='img/node.gif'    
    elif ';endpoint;' in line:
        icone='img/base.gif'       
    elif ';video;' in line:
        icone='img/youtube.jpg'     
    elif ';globe;' in line:
        icone='img/globe.gif'  
    elif ';vpn;' in line:
        icone='img/anyconnect.jpg'   
    elif ';anyconnect;' in line:
        icone='img/anyconnect.jpg'         
    else:
        icone=''
    # ===================================================================
    env.level=env.level[:-1]
    return(icone)
    
