print('*********BINARY CALCULATOR**********')

from multiplication import *
from addition import *
#Determines the operation user wants to perform
def determineOperation(response):
    if response == 1:
        addbuild()
    elif response == 2:
        print('binarySubtraction')
    elif response == 3:
        multbuild()
    elif response == 4:
        print('binaryDivision')

while True:
    try:
        #Ask for user input and returns the value as a string
        response = input('What do you want to do (Enter the number)\n 1.Binary Addition  2.Binary Subtraction 3.Binary Multiplication 4.Binary Division \n ->' )
        #Checks if the response is either 1,2,3 or 4
        if( response == '1' or response == '2' or response == '3' or response == '4' ):
            #Based on the response determines the operation to be performed
            determineOperation(int(response))
            break
    #Runs when user enters and invalid input and gives user opportunity to enter another value
    except:
        pass
    print('Invalid Input')
    
    
