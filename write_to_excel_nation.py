import xlwt 
from xlwt import Workbook 
  
def wten(nation_data,date_list,area_list):
    # Workbook is created 
    wb = Workbook() 

    # add_sheet is used to create sheet. 
    nation_sheet = wb.add_sheet('Nation') 


    # Add default row 
    nation_sheet.write(0, 0, 'Rank') 
    nation_sheet.write(0, 1, 'Nation') 
    nation_sheet.write(0, 2, '7 days per 100k') 
    nation_sheet.write(0, 3, '1 day change') 
    for index in range(len(date_list)):
        nation_sheet.write(0, index+4, 'Added on ' + date_list[index]) 




    # Add default column


  
    wb.save('UK Covid-19 Data.xls') 