import sys
firstNumber = float(input("Enter a number\n"))
secondNumber = float(input("Enter a number\n"))

"""
except:
    #sys.exc_info() will return list of error info.where/what
    error = sys.exc_info()[0]
    #print("please correct the input")
    print(error)
"""

try:
    result = firstNumber/secondNumber
    print(result)
    print("this line is executing")


except ZeroDivisionError:
    print("The answer is infinity")
    #will force the program to exit if you don't want to continue
    sys.exit()

except:
    #if this ZeroDivisionError triggered, the except block below will not execute
    error = sys.exc_info()[0]
    print("I'm sorry something went wrong")
    print(error)

finally:
    #close connection
    #this block will be triggered even if there's a sys.exit
    print("I will always run!")
#if there's a sys.exit(), the line below will not execute
#print("This message only displays if there is no error!!!!!!!!!!!!!!!!!!!!!!!!!!")
