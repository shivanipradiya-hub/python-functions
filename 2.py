# What is a Function?
# A function is a block of code that runs only when it is called.

# Why use Functions?

# 1. Avoid repeating code
# 2. Makes program clean & organized
# 3. Easy to debug and reuse

# Syntax:
# def function name():
    # code
# ex:
 def greet():
     print ("Hello Students")

# Syntax:
# def function_name():
    # code
# ex:
def greet():
      print ("Hello Students")
greet()

# Function with Parameters
# Used to pass values

def greet (name):
      print (f"Hello {name}")

greet()
greet("shreyarth")
greet("AICW")

#Task 2 
# Create a function to creat if a number is even or odd
num=int(input("enter a num"))
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
# check_even_odd(4)
# check_even_odd(7)
result=check_even_odd(num)
print(result)

#task 3
#create a function to find the factorial of a number
#input n=5
n=5
def factorial(n):
    result = 1
    for i in range(1, n+1):
       result = result * i
    return result
print(factorial(n))

#task 4
#create a find maximum of three numbers
a = 5
b = 10
c = 3
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(find_max(a, b, c))
#output
10

#task 5

def is_palindrome(s):
    return s == s[::-1]

# Example
text = input("Enter string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")


#task 6 create a function to  calculate the area of circle

 def area_of_circle(radius):
return 3.14 * radius * radius

# Example
r = float(input("Enter radius: "))
print("Area of circle:", area_of_circle(r))