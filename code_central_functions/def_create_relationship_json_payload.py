#  def_create_relationship_json_payload***
def create_relationship_json_payload(relationship_object,source_xid, target_xid, relationship_xid):
    '''
    MODIFIED : 2025-07-20

    description : create the relationships JSON payload to be added into the bundle
    '''
    route="/create_relationship_json_payload"
    env.level+='-'
    print('\n'+env.level,white('def create_relationship_json_payload() in app.py : >\n',bold=True))
    relationship_object["external_ids"] = [relationship_xid]
    relationship_object["source_ref"] = source_xid
    relationship_object["target_ref"] = target_xid
    relationship_object["source"] = "Cisco XDR Automation"
    relationship_object["relationship_type"] = "element-of"
    relationship_object["type"] = "relationship"
    relationship_object["id"] = "transient:"+relationship_xid
    env.level=env.level[:-1]
    return 1
  