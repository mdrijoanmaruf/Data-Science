from matplotlib import pyplot as plt
import numpy as np


# dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# dev_y = [38496, 42000, 46752, 99320, 53200,
# 56000, 62316, 64928, 27317, 68748, 73752]

# plt.plot(dev_x, dev_y, color = "red" , marker = "D" , linestyle = '' )   
# plt.plot(dev_x, dev_y,"rD-" )        # D -> Marker , r -> rad 
    # 2 lines will same output     
# plt.show()    # it will show data in a graps


            # Matplotlib Tutorial: Axes Labels, Legend, Grid
# days=[1,2,3,4,5,6,7]
# max_t=[50,51,52,48,47,49,46]
# min_t=[43,42,40,44,33,35,37]
# avg_t=[45,48,48,46,40,42,41]

# Axes labels and chart title:
# plt.xlabel('Day')
# plt.ylabel('Temperature')
# plt.title('Weather')
# mfc --> marker face color
# plt.plot(days , max_t , label = "Max" ,mfc = 'r')  # x axis = days and y axis = max_t and lable: Max
# plt.plot(days , min_t , label = "Min")  # x axis = days and y axis = min_t and lable: Min
# plt.plot(days , avg_t , label = "Avg")  # x axis = days and y axis = avg_t and lable: Avg

# plt.legend()    # Lable color 
# plt.legend(loc = "lower left")      # Lable color in lawer left
# plt.legend(loc = "best")            # Lable in best place automatically
# plt.legend(loc = "best" , shadow = True)            # will make lable shadew disign
# plt.legend(loc = "best" )            # will make lable shadew disign
# plt.grid()      # box shape

# plt.show()

# Plotting without x-points:
# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()



                # ***** Bar chart *****
company=['GOOGL','AMZN','MSFT','FB']
revenue=[90,136,89,27]

y = np.array(len(company))

plt.bar(y , revenue)
plt.show()