from get_data_names import gdn
from process_data import pro_da
from draw_pretty_table import dpt
from write_to_excel_nation import wten

areaType = 'Nation'
areaName = gdn(areaType)
[nation_data,date_list] = pro_da(areaType,areaName)
area_list = list(nation_data.keys())

# Draw a pretty table
# dpt(areaType,date_list,nation_data,area_list)

wten(nation_data,date_list,area_list)