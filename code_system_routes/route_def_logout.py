# def_logout***
@app.route("/logout")
def logout():
    env.level+='-'
    print()
    print(env.level,white('route logout() : >',bold=True))
    loguer(env.level+' route logout() : >')
    print()
    route="/logout"
    session['logged_in'] = False
    env.level=env.level[:-1]
    return index() 
    

