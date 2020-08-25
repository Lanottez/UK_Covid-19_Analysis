import prettytable as pt
from calculate_seven_days_average import cal_se_da_av

def dpt(areaType,date_list,date,area_list):
    #以下为画图代码
    tb = pt.PrettyTable()
    tb.field_names = [areaType] + ['7天平均/10万人次','今日较昨日变化','左日较前日变化','前日较前前日变化','前前日较前前前日变化'] + date_list
    for index in range(len(area_list)):
        output_data = cal_se_da_av(date[area_list[index]],date_list)
        row = [area_list[index]] + output_data
        tb.add_row(row)
    print(tb)