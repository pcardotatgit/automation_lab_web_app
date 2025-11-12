#  def_sxo_path***
def sxo_path():
    '''
    MODIFIED : 2025-07-19T14:20:04.000Z

    description : add JSON path in the resulting line
    
    how to call it :
    '''
    route="/sxo_path"
    env.level+='-'
    print('\n'+env.level,white('def sxo_path() in analyse_application_logs.py : >\n',bold=True))
    loguer(env.level+' def sxo_path() in analyse_application_logs.py : >')
    # ===================================================================    
    word_list=path.split('.')
    ii=0
    result=''    
    #print()
    #print(cyan(list))
    #print()    
    for item in word_list:
        ii+=1
        if item=='item':
            result=result+'['+str(list[ii]-1)+']'
            #result=result+'[xx]'
            #print(yellow(f"ii:{ii} item={item} valeur:{list[ii]-1}",bold=True))                        
            #print(yellow(item,bold=True))  
        else:
            result=result+'["'+item+'"]'
            #print(white(item,bold=True))        
    #print()    
    #print(cyan(result,bold=True))
    #goi=input('OK')
    # ===================================================================
    env.level=env.level[:-1]
    return result
    
