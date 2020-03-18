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

# The following is "FizzBuzz" written in one line.
# arr =["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)]
# print(arr)
