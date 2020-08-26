from requests import get

def get_data(url):
    response = get(url, timeout=20)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()


def gdn_API():
    
    endpoint = ('https://opendata.arcgis.com/datasets/85e5bca2a6d549fd80cf3b8fb777a0cd_0.geojson')
        
    data = get_data(endpoint)
    return data


def gdn(indictor):
    return_data = []
    if indictor == 'Nation':
        return(['England','Northern Ireland','Scotland','Wales'])
        # return(['England'])
    elif indictor == 'Region':
        return(['East Midlands','East of England','London','North East','North West','South East','South West','West Midlands','Yorkshire and The Humber'])
    elif indictor == 'LTLA':
        data = gdn_API()
        data_featues = data['features']
        for index in range(len(data_featues)):
            if not data_featues[index]['properties']['LTLA19NM'] in return_data:
                return_data.append(data_featues[index]['properties']['LTLA19NM'])
        return return_data
    elif indictor == 'UTLA': 
        data = gdn_API()
        data_featues = data['features']
        for index in range(len(data_featues)):
            if not data_featues[index]['properties']['UTLA19NM'] in return_data:
                return_data.append(data_featues[index]['properties']['UTLA19NM'])
        return return_data