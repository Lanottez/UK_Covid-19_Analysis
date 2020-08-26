
def print_array(data1,data2):
    if data1 > data2:
        return '\u2191'
    elif data1 < data2:
        return '\u2193'
    else:
        return '\u2192'


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
    sda_n5 = round(sum(cases_list[5:12])/7)
    sda_n6 = round(sum(cases_list[6:13])/7)
    sda_list = [sda_0,sda_n1,sda_n2,sda_n3,sda_n4,sda_n5,sda_n6]
    sda_diff_list = [sda_0-sda_n1,sda_n1-sda_n2,sda_n2-sda_n3,sda_n3-sda_n4,sda_n4-sda_n5,sda_n5-sda_n6,'-']
    array_list = [print_array(sda_0,sda_n1),print_array(sda_n1,sda_n2),print_array(sda_n2,sda_n3),print_array(sda_n3,sda_n4),print_array(sda_n4,sda_n5),print_array(sda_n5,sda_n6),' ']
    return [sda_list,sda_diff_list,array_list]

