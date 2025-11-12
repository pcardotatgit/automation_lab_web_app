#  def_xyz***
def xyz():
    # ===================================================================    
    URL='https://private.intel.amp.cisco.com/ctia/feed/feed-66554139-a250-4f25-81dc-a1e6751fc100/view.txt?s=1e540771-2d94-47c8-910c-97daf55aa97d'
    response = requests.get(URL)
    if response.status_code == 200:
        ok=response.text
        return ok
    else:
        print(red(response.status_code, response.text,bold=True))
        nok='0'
        return nok

