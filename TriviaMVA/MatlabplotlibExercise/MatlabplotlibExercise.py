

#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np 




with open("./data collection/weather.txt",'r') as data:
     font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

     read_data = data.readlines()
     
     year=[]
     maxtemp=[]
     mintemp=[]
     avtemp=[]
     
     for i in read_data:
         #year.append(i[0:4])
         #convert string to float
         year.append(float(i[0:4]))
         maxtemp.append(float(i[5:9]))
         mintemp.append(float(i[10:14]))
         avtemp.append((float(i[10:14])+float(i[5:9]))/2.0)
     #trend
     plt.title('Temperature since 1980')
     plt.xlabel('Year')
     plt.ylabel('Degrees in F')
     plt.plot(year,maxtemp)
     plt.text(0.5, 0.5, "maxtemp" , rotation=90)
     plt.plot(year,mintemp)
     plt.plot(year,avtemp)
     #here be attention tjat year must be a float number, cos year.append will reutn string
     plt.xticks(np.arange(1980,max(year),10.0))
     plt.show()