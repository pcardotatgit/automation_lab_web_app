# def_note***
@app.route('/note', methods=['GET'])
def note():
    env.level+='-'
    route="/note"
    print()
    print(env.level,white('route note() : >',bold=True))
    loguer(env.level+' route note() : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        env.level=env.level[:-1]
        return render_template('login.html')
    else:
        # GET variable from calling web page
        note='note_'+request.args.get('note')
        print()
        print('note : ',yellow(note,bold=True))
        print()
        with open('./templates/'+note) as fichier:
            text_content=fichier.read()
        html_content=text_content.replace("\n","<BR>")
        env.level=env.level[:-1]
        return html_content
        
        
