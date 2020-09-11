from process_data import pro_da
from read_borough import rb
def cdl(areaName_array):
	total_number = 0
	areaType = 'ltla'
	return_borough = rb(len(areaName_array[0]))
	print(return_borough+':')
	[nations_data,date_list] = pro_da(areaType,areaName_array[0])

	area_list = list(nations_data.keys())
	for name in areaName_array[0]:
		date = sorted(nations_data[name])[-1]
		print('    ',name+':',nations_data[name][date])
		total_number = total_number + nations_data[name][date]
	print('    ','Total case:',total_number)