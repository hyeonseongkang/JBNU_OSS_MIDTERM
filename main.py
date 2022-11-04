# Program make a simple calculator
from package import calculator
from package import log
import logging

# success, fail logger 생성
success_logger = log.get_logger("success", logging.DEBUG, './logs/success.log')
fail_logger = log.get_logger("fail", logging.ERROR, './logs/fail.log')

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # 더하기
        if choice == '1':
            log_str = '%0.1f + %0.1f = %0.1f' % (num1, num2, calculator.add(num1, num2))
            print(log_str)
            success_logger.debug(log_str)

        # 뺴기
        elif choice == '2':
            log_str = '%0.1f - %0.1f = %0.1f' % (num1, num2, calculator.subtract(num1, num2))
            print(log_str)
            success_logger.debug(log_str)

        # 곱하기
        elif choice == '3':
            log_str = '%0.1f * %0.1f = %0.1f' % (num1, num2, calculator.multiply(num1, num2))
            print(log_str)
            success_logger.debug(log_str)
            
        # 나누기
        elif choice == '4':
            value = calculator.divide(num1, num2)
            log_str = '%0.1f / %0.1f = %0.1f' % (num1, num2, value)
            success_logger.debug(log_str)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
