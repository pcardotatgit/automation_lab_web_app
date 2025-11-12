# def_open_browser_tab***
def open_browser_tab(host, port):
    env.level+='-'
    '''
        open web browser on login page
    '''
    print()
    print(env.level,white('def open_browser_tab() : > in app.py  : >\n',bold=True))
    loguer(env.level+' def open_browser_tab() : > in app.py  : > ')
    print()
    url = 'http://%s:%s/' % (host, port)

    def _open_tab(url):
        time.sleep(1.5)
        webbrowser.open_new_tab(url)

    thread = threading.Thread(target=_open_tab, args=(url,))
    thread.daemon = True
    thread.start() 
    env.level=env.level[:-1]
    return 1   
