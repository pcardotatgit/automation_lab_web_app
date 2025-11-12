#  def_delete_file***
@app.route('/delete_file', methods=['GET'])
def delete_file():
    '''
    Created : 2025-06-05T09:07:30.000Z

    description : go to delete file confirmation formular
    '''
    route="/delete_file"
    env.level+='-'
    print()
    print(env.level,white('route delete_file() in ***app.py*** : >',bold=True))
    loguer(env.level+' route delete_file() in ***app.py*** : >')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename=request.args.get('filename')
        filename=filename.replace('../','./')
        print()
        print('filename : ',filename)
        print()
        scriptdir=request.args.get('scriptdir')
        print()
        print('scriptdir : ',scriptdir)
        print()        
        html_output=f'<h3>Do you really want to delete : <br><br>{filename}</h3><br>in directory <b>[ {scriptdir} ]</b><br><hr>';
        html_output=html_output+f'<form action="/ok_delete_file" method="GET"><input type="hidden" name="filename" value="{filename}"><input type="hidden" name="scriptdir" value="{scriptdir}"><input type="submit" value="YES I DO"></form>'
        env.level=env.level[:-1]
        return html_output        

