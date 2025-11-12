#  def_new_html_page***
@app.route('/new_html_page', methods=['GET'])
def new_html_page():
    '''
    MODIFIED : 20250923
    
    display formular for creating a new html page in the ./templates folder
    '''
    route="/new_html_page"
    env.level+='-'
    print()
    print(env.level,white('route new_html_page() : >',bold=True))
    loguer(env.level+' route new_html_page() : >')
    print()
    with open('./result/home_url.txt') as file:
        home_url=file.read()
    html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
    <form action="/new_html_page_create" method="GET">
    <b>page name : </b><input type="text"  id="page_name" name="name" /> ( just the name ex ; my_page )<br><br>
    <b>page description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <b>Select a template :</b><br>
    <select name="template">
    <option value="page1">Like Index page</option>
    <option value="page2">Like page for result ( operation done )</option>
    <option value="page3">Like page for item selection</option>
    <option value="page4">Like page complex formular</option>  
    <option value="page5">Like page report in a textarea</option>
    <option value="page6">Like page formular for searching keyword edit box</option>
    <option value="page7">Like page formular for entering paragraph into textarea</option>    
    <option value="page8">Like page result into textarea black</option>  
    <option value="page9">calandar</option>
    <option value="page10">Dark Input field over white background</option>
    <option value="page11">Toggled hints</option>   
    <option value="page12">result page text area on white background & action button</option> 
    <option value="page13">EMPTY PAGE</option> 
    <option value="page14">Result List with Searching field</option> 
    <option value="page15">Search Keyword in wich field</option>     
    </select>
    <center><br><br><input type="submit" value="valid"/></center>
    </form>
    </body></html>
    ''';   
    env.level=env.level[:-1]
    return html_output  
    

