
with open("./data collection/weather.txt",'r') as data:
     read_data = data.readlines()
     
     year=[]
     maxtemp=[]
     mintemp=[]
     
     for i in read_data:
         year.append(i[0:4])
         max

monday = True
freshCoffee = True
if monday:
    if not freshCoffee:
        print('go by a coffee')
    print("have a nice day")
print("now you can start work")


answer = input("XXXXX?")
if answer == "yes":
   print("that will be an extra $10")
print("have a nice day")



month = 'Sep'

if month == 'Sep' or month == 'Apr' \
             or month == 'Oct':
            print('hahaha')