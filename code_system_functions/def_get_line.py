# def_get_line***
def get_line():
    env.level+='-'
    '''
        give the line number in the script wher is called this function
    '''
    print()
    print(env.level,white('def get_line() : >',bold=True))
    loguer(env.level+' def get_line() : >')
    print()     
    currentfram=currentframe()
    result='stop at line # : '+ str(currentfram.f_back.f_lineno)
    env.level=env.level[:-1]
    return result


