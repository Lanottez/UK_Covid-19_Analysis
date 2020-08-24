from get_data_names import gdn
from process_data import pro_da
from draw_pretty_table import dpt


areaType = 'Nation'
areaName = gdn(areaType)
# if 'Shropshire' in areaName:
#     areaName.remove('Shropshire')
# if 'Cheshire West and Chester' in areaName:
#     areaName.remove('Cheshire West and Chester')
[nation_data,date_list] = pro_da(areaType,areaName)
area_list = list(nation_data.keys())
dpt(areaType,date_list,nation_data,area_list)