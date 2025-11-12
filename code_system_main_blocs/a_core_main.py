app.config['UPLOAD_FOLDER'] = './temp'

# a_core_main.py***
if __name__ == "__main__":    
    print()
    print(env.level,white('MAIN FUNCTION ( the application starts here ): >',bold=True))
    '''
    with open('./debug/log.txt','w') as file:
        pass
    '''
    loguer(env.level)
    loguer(env.level+' APPLICATION STARTS')
    loguer(env.level)
    print()
    host="127.0.0.1"
    with open('./port.txt') as file:    
        port=file.read()
    with open('./templates/isolation_status.txt','w') as file2:
        file2.write('0')         
    open_browser_tab(host,port)
    app.secret_key = os.urandom(12)
    #app.run(debug=False,host='0.0.0.0', port=port,ssl_context='adhoc')
    app.run(debug=False,host='0.0.0.0', port=port)