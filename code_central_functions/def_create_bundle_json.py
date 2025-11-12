#  def_create_bundle_json***
def create_bundle_json(source,incidents,sightings,indicators,judgments_new, relationships_new):
    '''
    MODIFIED : 2025-07-20

    description : Create the Bundle JSDON payload to be posted to XDR
    '''
    route="/create_bundle_json"
    env.level+='-'
    print('\n'+env.level,white('def create_bundle_json() in app.py : >\n',bold=True))
    # ===================================================================    
    bundle_object={}
    bundle_object["type"] = "bundle"
    bundle_object["source"] = source
    if incidents!=[]:
        bundle_object["incidents"] = incidents
    if sightings!=[]:
        bundle_object["sightings"] = sightings
    if indicators!=[]:
        bundle_object["indicators"] = indicators
    if judgments_new!=[]:
        bundle_object["judgements"] = judgments_new
    if relationships_new!=[]:
        bundle_object["relationships"] = relationships_new
    env.level=env.level[:-1]
    return(bundle_object)