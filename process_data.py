from get_data_cases import gdc

def pro_da(areaType,areaName):
    nation_data = {}
    date_list = []
    for index_1 in range(len(areaName)):
        nation_data[areaName[index_1]] = {}
        data_raw = gdc(areaType,areaName[index_1])
        data = data_raw['data']
        for index_2 in list(range(8)):
            date= data[index_2]['date'][5:]
            nation_data[areaName[index_1]][date] = newCasesByPublishDate
            if not date in date_list:
                date_list.append(date)
    return [nation_data,date_list]