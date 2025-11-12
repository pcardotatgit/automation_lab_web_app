# def_do_admin_login***
@app.route('/login', methods=['POST'])
def do_admin_login(): 
    env.level+='-'
    print()
    print(env.level,white('route do_admin_login() : >',bold=True))
    loguer(env.level+' route do_admin_login() : >')
    print()
    route="/login"
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
        session['user'] = POST_USERNAME
    else:
        flash('wrong password!')
    env.level=env.level[:-1]
    return index()
  

