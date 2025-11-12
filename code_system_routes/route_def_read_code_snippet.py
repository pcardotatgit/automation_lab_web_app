#  def_read_code_snippet***
@app.route('/read_code_snippet', methods=['GET'])
def read_code_snippet():
    '''
    Created : 2025-03-31T19:45:47.000Z

read and display the content of the code snippet
    '''
    route="/read_code_snippet"
    env.level+='-'
    print()
    print(env.level,white('route read_code_snippet() : >',bold=True))
    loguer(env.level+' route read_code_snippet() : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:     
        snippet=request.args.get('snippet')
        print()
        print('snippet : ',snippet)
        print()
        with open('./code_snippets/'+snippet) as file:
            txt_content=file.read()    
        lines=txt_content.split('\n')
        html_out=''
        for line in lines:
            line=line.replace(' ','&nbsp;')
            html_out=html_out+line+'<br>'
    return html_out
        

