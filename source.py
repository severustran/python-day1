import math

def exercise_77():
    #number = 0 --- Should I declare this variable, first?
    while True:
        number_enter_by_user = int(input("Enter number n: "))
        if number_enter_by_user <= 0:
            print("Please enter positive number!")
        else:
            number = number_enter_by_user
            break
        pass
    result_for_loop = 0
    result_while_loop = 0
    # For Loop
    for number in range(1, number + 1):
        result_for_loop += number
    print("Result for loop: {} ".format(result_for_loop))
    # While loop
    while number > 0:
        result_while_loop += number
        number -= 1
        pass
    print("Result while loop: {} ".format(result_while_loop))
    pass

def exercise_78():
    while True:
        number_enter_by_user = int(input("Enter number n: "))
        if number_enter_by_user <= 0:
            print("Please enter positive number!")
        else:
            number = number_enter_by_user
            break
        pass
    result_list = []
    temp_submultiple = number
    while temp_submultiple >= 1:
        if number%temp_submultiple == 0:
            result_list.append(temp_submultiple)
            temp_submultiple = int(math.floor(temp_submultiple/2))
        else:
            temp_submultiple -= 1
        pass
    print(result_list)
    pass

def exercise_132():
    print("Enter positive number, enter 0 to stop!")
    result_list = []
    while True:
        number = int(input("Enter positive number: "))
        if number < 0:
            print("Please enter positive number!")
        elif number == 0:
            if len(result_list) == 0:
                print("There are no even numbers!")
            else:
                print("Even numbers are: {}".format(result_list))
            break
        else:
            if number%2 == 0:
                result_list.append(number)
        pass
    pass

    