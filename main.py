from get_data_cases import gdc
from get_data_names import gdn
import time
import pdb

areaType = 'UTLA'
areaName = gdn(areaType)

for index in range(len(areaName)):
    data_raw = gdc(areaType,areaName[index])
    print('Finish reading',areaName[index])
    data = data_raw['data']
    print('Data for ',areaName[index])
    print(data[0:5])

