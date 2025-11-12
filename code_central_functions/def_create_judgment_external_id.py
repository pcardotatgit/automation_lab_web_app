#  def_create_judgment_external_id***
def create_judgment_external_id(judgment_input):
    '''
    MODIFIED : 2025-07-20

    description : Create an external ID for judgement which is required within the Bundle
    '''
    route="/create_judgment_external_id"
    env.level+='-'
    print('\n'+env.level,white('def create_judgment_external_id() in app.py : >\n',bold=True))
    # hash judgment without transient ID
    hash_input = json.dumps(judgment_input)
    hash_value = hashlib.sha256(hash_input.encode('utf-8')).hexdigest()
    judgment_external_id = "xdr-automation-judgment-" + hash_value
    env.level=env.level[:-1]
    return judgment_external_id
    