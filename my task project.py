#!/usr/bin/env python
# coding: utf-8

# #  LEVEL 1: Task 1

# # Task: String Reversal 

# In[6]:


print (" Task _1 - String Reversal")
print("--------------------------")

def string_reversal(input_string):
    revers=(input_string[::-1])
    return revers

input_string = input ("Enter a string to revers::")
print(string_reversal(input_string))


# # Task 2

# # Task: Temperature Conversion

# In[7]:


print ("Temperature Conversion")
print("-----------------------")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temperature = float(input("Enter the temperature value:"))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

if unit.lower() == "c":
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} °C  is equal to {converted_temperature}°F ")

elif unit.lower() == "f":
    converted_temperature = celsius_to_fahrenfeit(temperature)
    print(f"{temperature}°C is equal to {converted_temperature:.2f}°C")
else:
    print("Invlid unit of measurement please enter (c or f) .")


# # Task 3

# # Task: Email Validator

# In[ ]:


print("Email validator")
print('----------------')

import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
         print(f"{email} is NOT a valid email address.")

email=input()
is_valid_email(email)


# # Task 4

# # Task: Calculator Program

# In[ ]:


print("Basic Calculator")
print("-----------------")

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = (num1+num2)
elif operator == "-":
    result = (num1-num2)
elif operator == "*":
    result =(num1*num2)
elif operator == "/":
    result = (num1//num2)
elif operator == "%":
    result = (num1%num2)
else:
    print("Invalid operator. Please enter a valid operator.")

print(f"Result: {num1} {operator} {num2} = {result}")


# # Task 5

# # Task: palindrome Checkers

# In[ ]:


print("Palindrome checker")
print("-------------------")

def palindrome_checker(input_string):
    input_string=input_string.replace(" ","")
    if input_string[0:]==input_string[::-1]:
        print("Given string is a palindrome")
    else:
        print("Given string is Not a palindrome")

input_string=input("Enter a string:").lower()
palindrome_checker(input_string)


# 

# In[ ]:




