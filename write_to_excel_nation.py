import xlwt 
from xlwt import Workbook 
from calculate_seven_days_average import cal_se_da_av
import numpy as np 
from matplotlib import pyplot as plt 
import openpyxl

def wten(nations_data,date_list,area_list):
    # Workbook is created 
    wb = Workbook() 

    style = xlwt.XFStyle()
    style.alignment.wrap = 1
    # add_sheet is used to create sheet. 
    nation_sheet = wb.add_sheet('Nation') 


    # Add header row 
    nation_sheet.write(0, 0, 'Nation',style) 
    for index in range(3,len(date_list)-3):
        nation_sheet.write(0, index-2, '7d/100k\n'+date_list[index],style) 


    # Add header column
    for index in range(len(area_list)):
        nation_sheet.write(index+1, 0, area_list[index],style) 
    
    # Add row
    for index_1 in range(len(area_list)):
        average_data = cal_se_da_av(nations_data[area_list[index_1]],date_list)
        # plot the graph
        plt.plot(range(len(average_data[0])),average_data[0])
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        plt.savefig("myplot.png", dpi = 150)


        ws = wb.active

        img = openpyxl.drawing.image.Image('myplot.png')
        img.anchor(ws.cell('A5'))
        ws.add_image(img)

        for index_2 in range(len(average_data[0])):
            nation_sheet.write(index_1+1,index_2+1,average_data[2][index_2]+' '+str(average_data[0][index_2])+str(average_data[1][index_2]))
  
    wb.save('UK Covid-19 Data.xls') 

