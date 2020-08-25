from requests import get

def get_data(url):
    response = get(url, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()


def gdc(areaType,areaName):
<<<<<<< HEAD
    if areaType == 'Nation':
        endpoint = (
            'https://api.coronavirus.data.gov.uk/v1/data?'
            'filters=areaType=' +
            areaType
            +';areaName='+
            areaName
            +'&structure={"date":"date","newCasesByPublishDate":"newCasesByPublishDate"}'
        )
    else:
        endpoint = (
            'https://api.coronavirus.data.gov.uk/v1/data?'
            'filters=areaType=' +
            areaType
            +';areaName='+
            areaName
            +'&structure={"date":"date","newCasesByPublishDate":"newCasesBySpecimenDate"}'
        )
=======
    
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=' +
        areaType
        +';areaName='+
        areaName
        +'&structure={"date":"date","newCasesBySpecimenDate":"newCasesBySpecimenDate"}'
    )
>>>>>>> parent of 20ddcfe... Updated
        
    data = get_data(endpoint)
    return data



