#=_=_=_====SIMPLE CALCULATOR====_=_=_=#
# 3 steps are build calculator porgram
#   1. functions for operations
#   2. user input
#   3. print result



# step-1: create function
#function to add two numbers
def add(num1,num2):
    return num1+num2

#function to substract two numbers
def sub(num1,num2):
    return num1-num2

#functions to divide two numbers
def div(num1,num2):  
    return num1/num2

#functions to multiply two numbers
def multiply(num1,num2):
    return num1*num2

#functions to multiply two numbers
def avg(num1,num2):
    return (num1+num2)/2


#step-2: user input
print("\n======SIMPLE CALCULTOR======")
print("Please select a operation:\n "\
       "1. addition:\n" \
        "2. substraction:\n" \
            "3. multiplication:\n" \
                "4.division:\n" \
                    "5.average:\n ")

select=int(input("Select a operation from 1 to 5:"))

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))



#step-3: print the result 

if select == 1:
    print(number1, "+", number2, "= ", \
          add(number1, number2))
    
elif select == 2:
    print(number1, "-", number2, "= ", \
          sub(number1, number2))
    
    
elif select == 3:
    print(number1, "*", number2, "= ", \
          multiply(number1, number2))
    
elif select == 4:
    try: 
       result=div(number1, number2)
       print(number1, "/", number2, "= ", result )

    except ZeroDivisionError:
        print("Can't divide by zero....!" )
    
elif select == 5:
    print("(",number1, "+", number2, ")", "/", "2", "= ", \
          avg(number1, number2))
    
else:
    print("Invalid operation !! pls select again...!")
    


    

