import requests
from requests import get
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_data(url):
    # response = get(url, timeout=10)
    
    # if response.status_code >= 400:
    #     raise RuntimeError(f'Request failed: { response.text }')
        
    retry_strategy = Retry(
        total=10,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    response = http.get(url)

    return response.json()


def gdc(areaType,areaName):
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
            +'&structure={"date":"date","newCasesByPublishDate":"newCasesByPublishDate"}'
        )
        
    data = get_data(endpoint)

    return data



