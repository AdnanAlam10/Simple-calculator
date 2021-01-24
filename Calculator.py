#!/usr/bin/env python
# coding: utf-8

# In[17]:


def calculate():
    operator = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if operator == "+":
        print("{} + {} = {}" .format(number_1, number_2, number_1+number_2))
    elif operator == "-":
        print("{} - {} = {}" .format(number_1, number_2, number_1-number_2))
    elif operator == "*":
        print("{} * {} = {}" .format(number_1, number_2, number_1*number_2))
    elif operator == "/":
        print("{} ÷ {} = {}" .format(number_1, number_2, number_1/number_2))
    else:
        print("Enter an appropriate operator")
    
    again()

        
def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

print("Welcome to the calculator")
calculate()


# In[ ]:




