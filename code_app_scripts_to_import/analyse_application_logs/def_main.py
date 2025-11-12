#  def_main***
def main():
    '''
    MODIFIED : 2025-07-19T14:01:36.000Z

    description : main function
    
    how to call it :
    '''
    route="/main"
    env.level+='-'
    print('\n'+env.level,white('def main() in analyse_application_logs.py : >\n',bold=True))
    #loguer(env.level+' def main() in analyse_application_logs.py : >')
    format_log()
    tree=parse_txt('./debug/parsed.txt',debug)
    footer='''
        document.write(d);
        //-->
    </script>
</div>
</body>
</html>
    '''
    global text_out
    text_out=text_out+tree+footer
    with open('./templates/log.html','w') as fich:
        fich.write(text_out)
    env.level=env.level[:-1]
    return 1
    
