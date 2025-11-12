#  def_list_snippets***
@app.route('/list_snippets', methods=['GET'])
def list_snippets():
    '''
    Created : 2025-03-31T17:42:51.000Z

    list code snippets
    '''
    route="/list_snippets"
    env.level+='-'
    # print()
    # print(env.level,white('route list_snippets() : >',bold=True))
    #loguer(env.level+' route list_snippets() : >')
    # print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><ul>';
    files =[file for file in os.listdir('./code_snippets')]
    ii=0
    function_list=[]
    for file in files:
        # print(' file : ',yellow(file,bold=True)) 
        html_output=html_output+'<li><b><a href="/read_code_snippet?snippet='+file+'">'+file+'</a></b></li>'
    env.level=env.level[:-1]
    html_output=html_output+'\n</ul><br><a href="/stop">Click here to stop the App  </a></body><html>'
    return html_output
        

