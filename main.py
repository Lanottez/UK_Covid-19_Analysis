
from collect_data_london import cdl
import numpy as np

# 读取数据


areaName_inner_london=np.array([['Westminster','Kensington and Chelsea','Hammersmith and Fulham','Wandsworth','Lambeth','Southwark', #2-7
	'Tower Hamlets','Hackney and City of London','Islington','Camden', #1,8-11
	'Lewisham','Greenwich'],[2,3,4,5,6,7,8,9,10,11,21,22]]) #21-22


areaName_outer_london = np.array([['Brent','Ealing','Hounslow','Richmond upon Thames','Kingston upon Thames','Merton', #12-17
	'Sutton','Croydon','Bromley', #18-20
	'Bexley','Havering','Barking and Dagenham','Redbridge','Newham','Waltham Forest','Haringey','Enfield','Barnet','Harrow','Hillingdon'],
	[12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,29,30,31,32,33]]) #23-33

areaName_central_london = np.array([['Westminster','Kensington and Chelsea','Lambeth','Southwark','Islington','Camden'],
	[2,3,6,7,10,11]])
areaName_west_london = np.array([['Hammersmith and Fulham','Brent','Ealing','Hounslow','Richmond upon Thames','Harrow','Hillingdon'],
	[4,12,13,14,15,32,33]])
areaName_north_london = np.array([['Haringey','Enfield','Barnet'],
	[29,30,31]])
areaName_south_london = np.array([['Wandsworth','Merton','Croydon','Kingston upon Thames','Sutton','Bromley'],
	[5,17,19,16,18,20]])
areaName_east_london = np.array([['Tower Hamlets','Hackney and City of London','Lewisham','Greenwich','Newham','Waltham Forest','Bexley','Barking and Dagenham','Redbridge','Havering'],
	[8,9,21,22,27,28,23,25,26,24]])

areaNames = [areaName_inner_london,areaName_outer_london,areaName_central_london,areaName_west_london,areaName_north_london,areaName_south_london,areaName_east_london]

for area_name in areaNames:
	cdl(area_name)






