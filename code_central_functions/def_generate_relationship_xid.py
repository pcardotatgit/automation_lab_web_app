#  def_generate_relationship_xid***
def generate_relationship_xid(source_xid, target_xid):
    '''
    MODIFIED : 2025-07-20

    description : Create a relationship transiant ID which is required for the bundle
    '''
    route="/generate_relationship_xid"
    env.level+='-'
    print('\n'+env.level,white('def generate_relationship_xid() in app.py : >\n',bold=True))
    hash_value = hashlib.sha1((source_xid + target_xid).encode('utf-8'))
    hash_value = hash_value.hexdigest()
    relationship_xid = "xdr-automation-relationship-" + hash_value
    env.level=env.level[:-1]
    return relationship_xid
  