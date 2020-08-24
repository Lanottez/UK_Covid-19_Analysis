
def cal_se_da_av(nation_data,date_list):
    seven_day_average_today = 0
    seven_day_average_yesterday = 0
    cases_list = []

    for index_2 in range(len(date_list)):
        cases_list.append(nation_data[date_list[index_2]])
    seven_day_average_today = round(sum(cases_list[:-1])/7)
    seven_day_average_yesterday = round(sum(cases_list[1:])/7)
    return [seven_day_average_today,seven_day_average_today-seven_day_average_yesterday] + cases_list 