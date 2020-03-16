ans = int(input())

def fizzBuzz(num):
    if num % 5 == 0 and num % 3 ==0:
        return print("FizzBuzz")
    elif num % 5 == 0:
        return print("Buzz")
    elif num % 3 == 0:
        return print("Fizz")
    else:
        return print(num)


for i in range(1, ans):
    fizzBuzz(i)


