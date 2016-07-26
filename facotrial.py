

def factorial(number):
    if (number==1):
        return 1
    result=factorial(number-1)*number

    return result

num=int(input("your number:  "))
print ("the result is:  %d"%factorial(num))
