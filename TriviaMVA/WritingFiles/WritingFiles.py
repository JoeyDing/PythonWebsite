"""
filename = 'demo.txt'
#filename = 'demo.csv'
#this will overwrite the txt file
#accessmode = 'w'
#this will append content at the end
accessmode = 'a'

data = input('please enter file info\n')
file = open(filename,accessmode)
#file = open(filename,mode = accessmode)
#WRITE = 'w'
#file = open(filename,mode = WRITE)
file.write('\n'+data)
#file.write('How are you,line2?')
#open sth, close it, like open a doc inside word, with the os says you are using it, you program might crashes cos yout file is used by someone else.
file.close()

print('File written successfully')  
"""

#Reading file
employeefileName = 'employees.txt'
accessMode = 'r'
employeeFile = open(employeefileName,accessMode)

employeeList = []
employee = ''

#calculate the number of lines
num_lines = sum(1 for line in open(employeefileName))

for employee in range(0,num_lines):
    fileContent = employeeFile.readline()
    employeeList.append(fileContent)
print(employeeList)





