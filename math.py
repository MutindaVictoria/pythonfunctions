def add(a,b):
    answer= a+b
    return answer


def multiply(a,b):
    answer= a*b
    return answer

def subtract(a,b):
    answer= a-b
    return answer

def divide(a,b):
    answer= a/b
    return answer

def remainder(a,b):
    answer=  a%b
    return answer  



def multiply(*numbers):
    answer=1
    for number in numbers:
        answer*=number
    return answer

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")



