#  def_parse_txt***
def parse_txt(filename,debug):
    '''
    MODIFIED : 2025-07-19T14:08:15.000Z

    description : parse the input file and create the dtree html file
    
    how to call it :
    '''
    route="/parse_txt"
    env.level+='-'
    print('\n'+env.level,white('def parse_txt() in analyse_application_logs.py : >\n',bold=True))
    #loguer(env.level+' def parse_txt() in analyse_application_logs.py : >')
    # ===================================================================    
    lnumber=1
    level=0
    last_level=0
    tree=''
    back=0
    levels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    level_index=0
    notes_index=0 
    fichier=open('result.txt','w')
    fichier2=open('tree.txt','w')    
    with open(filename) as file:
        all_text_content=file.read()
    lines=all_text_content.split('\n')
    parent_base=0
    str_parent=1
    for line in lines:
        nb_comma=line.count(';')
        nb_comma_to_add=4-nb_comma
        for i in range (0,nb_comma_to_add):
            line+=';'
        color=''         
        if ';cnk;' in line:
            color='red'     
        line_list=line.split(';')
        level=line_list[0].count('-')     
        description=line_list[1].replace("'","&lsquo;")
        liste_de_mots=description.split('<<:')
        if '<<col:' in liste_de_mots[0] and color=='':
            col_list=liste_de_mots[0].split('>>')
            color=col_list[0].replace('<<col:','')
            part1='<span style="color:'+color+';font-weight:bolder">'+col_list[1]+' </span>'          
        else:
            if color=='red':
                part1='<span style="color:red;font-weight:bolder"> '+liste_de_mots[0]+' </span>' 
            else:
                part1='<span style="color:blue;font-weight:bolder"> '+liste_de_mots[0]+' </span>'
        if len(liste_de_mots)>1:
            if '<<col:' in liste_de_mots[1]  and color=='':
                col_list=liste_de_mots[1].split('>>')
                color=col_list[0].replace('<<col:','')  
                part2='<span style="color:'+color+';font-weight:bolder">'+col_list[1]+'</span>' 
            else:
                part2='<span style="color:green;font-weight:bolder">'+liste_de_mots[1]+'</span>'
            description='('+str(lnumber)+')'+part1+part2
        else:
            description='('+str(lnumber)+')'+part1
        description='<b>'+description+'<b>'
        #icone=icon(line)
        icone=''
        if '<<url:' in line:
            lien_url=line_list[2].replace("<<url:","")
        elif '<<local_url:' in line:
            lien_url='notes/'+line_list[2].replace("<<local_url:","")            
        elif '<<note:' in line:
            lien_url='notes/'+line_list[2].replace("<<note:","")
        else:
            lien_url=''            
        # print(white(f"Parent -> last level:{last_level}",bold=True))          
        # print(white(f"Current-> level:{level}",bold=True))        
              
        if level==last_level+1:            #NEXT LEVEL
            str_parent=parent_base-1
            if debug:                        
                print(red(f"current level index ={level_index}",bold=True))                    
                print(red(f"parent level line number ={str_parent}",bold=True)) 
                print(red(f"levels before saving line",bold=True))
                print(yellow(levels,bold=True))              
            line_out2=f"        d.add({parent_base},{str_parent},'{description}','{lien_url}','','','{icone}','{icone}');" 
            # print()
            # print(cyan(line_out2,bold=True))  
            # print()
            if levels[level_index]==0:
                levels[level_index]=parent_base-1
            # print(green(f"set levels[{level_index}]to {parent_base}-1 and increment level_index",bold=True))                                  
            if parent_base!=0:
                tree=tree+line_out2+'\n'
                fichier2.write(line_out2)
                fichier2.write("\r")
                #levels[level_index]+=1
                if debug:
                    print(green('saved to file',bold=True)) 
            else:
                if debug:
                    print(red('dont save'))          
                else:
                    pass
            level_index+=1
            back=2 # next level
            if debug:
                print(red(f"after saving line",bold=True))       
                print(green(levels,bold=True))                 
                print(red(f"new level index ={level_index}",bold=True)) 
                print()
                gio=input(' -> NEW LEVEL and new key added:') 
                print('---------------------------------------------------next block >')                
        elif level<last_level:              # BACK TO PARENT LEVEL
            level_index=level-1
            str_parent=levels[level_index]
            for ii in range (level,26):
                levels[ii]=0
            if debug:                        
                print(yellow(f"BACK level index ={level_index}",bold=True))                    
                print(yellow(f"BACK parent level line number ={str_parent}",bold=True)) 
                print(yellow(levels,bold=True))              
            line_out2=f"        d.add({parent_base},{str_parent},'{description}','{lien_url}','','','{icone}','{icone}');"  
            # print()
            # print(cyan(line_out2,bold=True))  
            # print()         
            #levels[level_index]=parent_base            
            if parent_base!=0:
                tree=tree+line_out2+'\n'
                fichier2.write(line_out2)
                fichier2.write("\r")
                #levels[level_index]+=1
                if debug:
                    print(green('saved to file',bold=True)) 
            else:
                if debug:
                    print(red('dont save'))          
                else:
                    pass
            level_index+=1
            levels[level_index]=parent_base
            if debug:
                print(yellow(f"Newlevel index ={level_index}",bold=True))                    
                print(yellow(f"New parent level line number ={str_parent}",bold=True)) 
                print(yellow(levels,bold=True))              
                gio=input(' <- GET BACK AND NEW KEY ADDED:') 
                print('---------------------------------------------------next block >')  
            back=1
        elif level==last_level:       # SAME LEVEL - ADD NEW KEY
            # print('SAME LEVEL')
            if back==2:
                #str_parent=parent_base-1
                levels[level_index-1]=str_parent
                # print('back=2 =>  from new level')
            else:
                str_parent=levels[level_index-1]
                # print(f'back={back}')
            #str_parent=levels[level_index-1] 
            back=0
            if debug:                        
                print(red(f"level index ={level_index}",bold=True))                    
                print(red(f"parent level line number ={str_parent}",bold=True)) 
                print(yellow(levels,bold=True))              
            line_out2=f"        d.add({parent_base},{str_parent},'{description}','{lien_url}','','','{icone}','{icone}');" 
            # print()
            # print(cyan(line_out2,bold=True))     
            # print()           
            #levels[level_index]=parent_base   
            level_index=level
            if parent_base!=0:
                tree=tree+line_out2+'\n'
                fichier2.write(line_out2)
                fichier2.write("\r")
                #levels[level_index]+=1
                if debug:
                    print(green('saved to file',bold=True)) 
            else:
                if debug:
                    print(red('dont save'))          
                else:
                    pass
            if debug:
                print(red(f"level index ={level_index}",bold=True))                    
                print(red(f"parent level line number ={str_parent}",bold=True)) 
                print(red(f"after saving line",bold=True))
                print(yellow(levels,bold=True))             
                gio=input(' <-> SAME LEVEL NEW KEY ADDED:')   
                print('---------------------------------------------------next block >') 
        parent_base+=1                 
        last_level=level
        lnumber+=1
    fichier.close()
    fichier2.close()
    # ===================================================================
    env.level=env.level[:-1]
    return(tree)
    
