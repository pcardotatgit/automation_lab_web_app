#  def_loguer***
def loguer(log):
    '''
    MODIFIED : 2025-06-19T15:52:21.000Z

    description : log when a function or a route is called with start date
    '''
    time = datetime.now().isoformat()
    #print(time)
    log=log+' at '+ time
    with open(f'./debug/log.txt','a+') as file:
          file.write(log+'\n')
    return 1
    

