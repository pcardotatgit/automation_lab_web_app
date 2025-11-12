#  def_crayons_colors***
def crayons_colors():
    '''
    MODIFIED : 2025-09-17T20:05:26.000Z
    description : list of crayons colors
    
    how to call it :
    '''
    route="/crayons_colors"
    env.level+='-'
    print('\n'+env.level,white('def crayons_colors() in app.py  : >\n',bold=True))
    loguer(env.level+' def crayons_colors() in app.py  : > ')
    # ===================================================================  
    message=" this is a message to display"
    if color=="lblue":
        print('===> ',blue(message))
    elif color=="blue":
        print('===> ',cyan(message,bold=True))
    elif color=="magenta":
        print('===> ',magenta(message,bold=True))
    elif color=="purple":
        print('===> ',magenta(message,bold=True))
    elif color=="lred":
        print('===> ',red(message,bold=True))
    elif color=="pink":
        print('===> ',red(message,bold=True))
    elif color=="red":
        print('===> ',red(message))
    elif color=="yellow":
        print('===> ',yellow(message,bold=True))
    elif color=="orange":
        print('===> ',yellow(message))
    elif color=="green":
        print('===> ',green(message,bold=True))
    elif color=="white":
        print('===> ',white(message,bold=True))
    # ===================================================================
    loguer(env.level+' def END OF crayons_colors() in app.py  : > ')
    env.level=env.level[:-1]
    return result
    

