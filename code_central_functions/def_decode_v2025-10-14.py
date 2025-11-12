#  def_decode***
def decode(mot):
    '''
    MODIFIED : 2025-10-14T07:17:00.000Z
    description : decode loop
    
    how to call it :
    '''
    route="/decode"
    # ===================================================================   
    global original
    ok=""
    ip="192.168.128.191"
    ip=xyz()
    if ip=='0':
        print(red('Error in reading the test_IP_Address From Test feed',bold=True))
        ip=input('Enter the test IP Address : ')
    ip=ip.replace(".","")
    b=[]
    for i in ip:
        b.append(int(i))
    e=['0','1','2','3','4','5','6','7','8','9']
    i=0
    ii=0
    for i in range (0,len(mot)):
        if mot[i] in e:
            v=int(mot[i])-b[ii]
            ii+=1
            if v<0:
                v=10+v
            ok=ok+str(v)
        else:
            ok=ok+str(mot[i])
    print()
    print(original)
    print(ok)
    # ===================================================================
    return ok
    

