
def cal_se_da_av(nation_data,date_list):
    sda_0 = 0
    sda_n1 = 0
    cases_list = []

    for index_2 in range(len(date_list)):
        cases_list.append(nation_data[date_list[index_2]])
    sda_0 = round(sum(cases_list[0:7])/7)
    sda_n1 = round(sum(cases_list[1:8])/7)
    sda_n2 = round(sum(cases_list[2:9])/7)
    sda_n3 = round(sum(cases_list[3:10])/7)
    sda_n4 = round(sum(cases_list[4:11])/7)
    return [sda_0,sda_0-sda_n1,sda_n1-sda_n2,sda_n2-sda_n3,sda_n3-sda_n4] + cases_list 