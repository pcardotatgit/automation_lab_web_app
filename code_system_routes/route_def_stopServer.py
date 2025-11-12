# def_stopServer***
@app.route('/stop', methods=['GET'])
def stopServer():
    env.level+='-'
    print()
    print(env.level,white('route stopServer() : >',bold=True))
    loguer(env.level+' route stopServer() : >')
    print()
    route="/stop"
    os.kill(os.getpid(), signal.SIGINT)
    env.level=env.level[:-1]
    return "Flask Server is shutting down..."
    

