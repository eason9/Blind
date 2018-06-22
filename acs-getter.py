# I've made a little function for grabbing ACS data via the API. 
# The census data is great, but it's not the easiest to figure out.

def get_acs_2010(varlist):
    if len(varlist) > 50: 
        print('No more than 50 vars can be accessed via the API')
        return
    asv = ','.join(varlist)
    base = 'https://api.census.gov/data/'
    year = '2010/'
    data_set = 'acs5'
    var_list = '''?get=''' + asv 
    for_tract = '&for=tract:*'
    in_state = '&in=state:011'
    in_county = '&in=county:*'
    api_key = '&key=8a94013b188270dc1caf589561d93fbed8091e0a'
    url = base+year+data_set+var_list+for_tract+in_state+in_county+api_key
    with urllib.request.urlopen(url) as f:
         data = eval(f.read().decode('utf-8'))
    acs_df = pd.DataFrame(data[1:],columns=data[0])
    acs_df[varlist] = acs_df[varlist].astype(int)
    acs_df['TRACT'] = acs_df['tract'].astype(str)
    return acs_df
