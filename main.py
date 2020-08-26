from get_data_names import gdn
from process_data import pro_da
from draw_pretty_table import dpt
from write_to_excel_nation import wten

# 读取数据
areaType = 'Nation'
areaName = gdn(areaType)
[nations_data,date_list] = pro_da(areaType,areaName)
area_list = list(nations_data.keys())

# # Draw a pretty table
# dpt(areaType,date_list,nations_data,area_list)

# # 模拟数据
# areaType = 'Nation'
# areaName = ['England']
# nations_data = {'England': {'08-25': 1065, '08-24': 758, '08-23': 938, '08-22': 1060, '08-21': 908, '08-20': 1035, '08-19': 707, '08-18': 975, '08-17': 634, '08-16': 952, '08-15': 934, '08-14': 1284, '08-13': 1059}}
# date_list = ['08-25', '08-24', '08-23', '08-22', '08-21', '08-20', '08-19', '08-18', '08-17', '08-16', '08-15','08-14','08-13']
# area_list = ['England']

wten(nations_data,date_list,area_list)