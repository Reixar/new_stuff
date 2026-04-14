def main():
    print("Let's get our math on!")  
    math = get_choice()
    num1 = float(input("Great now I just need your first number: "))
    num2 = float(input("Now your second "))
    print("Processing...")
    
        
    if math == 1:
        print(multi(num1,num2)) 
    elif math == 2:
        if num2 == 0:
            print("You can't devide by zero")
        else:
            print(divide(num1,num2))
    elif math == 3:
        print(minus(num1,num2)) 
    elif math == 4:
        print(plus(num1,num2)) 

    
    while True:

        exit_question = input("Do you want to continue calculator? (Y/N) ").upper()
            
        if exit_question == "N":
            break
        elif exit_question == "Y":
            main()
        else:
            exit_question = input("Please use Y/N")
        

def get_choice():
    while True:
        try:
            math = int(input("1 Multiply  2 Divide  3 Subtract  4 Add: "))

            if math in [1, 2, 3, 4]:
                return math

            print("Invalid option, try again.")

        except ValueError:
            print("Please enter a number only.")

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


main()