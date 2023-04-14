def my_country(country="Rwanda"):
    print(f"Hello from {countyr}")

def greet(*names):
    for name in names:
        print(f"Hello{names}")


def sum(*numbers):
    answer=0
    for number in numbers:
        answer+=number
    return answer
    
#A function named concatenate_args that takes any number of string arguments
# in positional arguments format and concatenates them into a single string
    
def concatenate_args(*words):
    result=""
    for word in words:
        result+=word
    return result

#A function named concatenate_kwargs that takes any number of string
# arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    results=""
    for key,value in kwargs.items():
        results+=value
    return results



            
