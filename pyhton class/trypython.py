
# -------------------------if statement---------------------------

# s= input("Enter the string: ")
# if s==s[::-1]:
#     print("it is a palindrome")
# else:
#     print("is is not a palindrome")
    

# for i in num:
#     if num not in duplicates :
#         duplicates.append(i)
# print("Duplicate elements are:", duplicates)

# str1=input("Enter first string: ")
# str2=input("Enter second string: ")
# if sorted(str1) == sorted(str2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")
    

# '''a=5
# b=10
# a,b=b,a
# print("a=",a)
# print("b=",b)'''

# n=int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n}x{i}={n*i}")
    

# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")


# a=10
# b=20
# c=a+b
# print(c)

# name= "Rithin Rose"
# age=20
# print("He is a new CEO",name,"His age is",age)


# birth_year = input("Enter you birth year : ")
# age = 2026 - int(birth_year)
# print(age)


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)


# temp = int(input("Enter the Temperature: "))

# if temp > 30:
#     print("It's a hot day")
#     print("Drink plenty Water")
# elif temp >20:
#     print("It's a nice day")
# else:
#     print("Warm Weather")

# weight = int(input("Enter the Weight: "))

# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: "+ str(converted))
# else:
#     converted = weight *0.45
#     print("Weight in Kgs: " + str(converted))

# MARK---------------------------------
# mark = int(input("Enter mark: "))

# if (mark>=90) and (mark<=100):
#     print("you got A grade")
# elif (mark>=75) and (mark<=89):
#     print("You got B grade")
# elif (mark>=50) and (mark<=74):
#     print("You got C grade")
# else:
#     print ("You failed")


# LEAP YEAR---------------------------------
# year = int(input("Enter Year: "))

# if year % 4 == 0:
#     print("It's a Leap year")
# else:
#     print("It's not a leap year")

# num =  int(input("Enter the Number: "))


# DIVISIBLE BY 5-------------------------------
# if num % 5 == 0:
#     print("Divisble by 5")
# else:
#     print("not divisble by 5")

# ODD OR EVEN-------------------------------

# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("it's a even number")
# else:
#     print("it's a odd number")

# Positive / Negative / Zero-----------------------
# num = int(input("Enter number: "))
# if num > 0 :
#     print("It's positive number")
# elif num == 0:
#     print("It's zero")
# else:
#     print("It's negative number")


# Voting Eligibility------------------------

# Age = int(input("Enter Age: "))

# if Age >= 18 :
#     Region = input("Enter your region: ").lower()
#     if Region == "india":
#         print(f"You are an indian and ur are {Age} yearls old so u can vote")
#     else:
#         print("You can't able to vote")
    
# else:
#     print("Your are not eligible to vote")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operation (+, -, *, /): ")

# if op == "+":
#     print("Result:", num1 + num2)

# elif op == "-":
#     print("Result:", num1 - num2)

# elif op == "*":
#     print("Result:", num1 * num2)

# elif op == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Cannot divide by zero")

# else:
#     print("Invalid operation")
    
# num = int(input("enter the number"))

# if 1 <= num <= 50:
#     print("Low")

# elif 51 <= num <= 100:
#     print("Medium")

# elif num > 100:
#     print("High")

# else:
#     print("Invalid")

# Age = int(input("Enter your age: "))
# ID = input("Do you have ID: ")

# if Age >= 18  and ID == "yes":
#     print("You can enter ")
# else:
#     print("You cant enter")


'''pin = "1234"
balance = 50
attempts = 3

while attempts > 0:# while 1>0 -> True
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == pin: # if 1234 == 1234 -> True
        print("Login successful")
        
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1": # 2 == 1 -> False
                print("Your balance is:", balance)
                
            elif choice == "2": # 2  == 2 -> True
                deposit = float(input("Enter deposit amount: "))
                
                if deposit > 0: # 100 > 0 -> True
                    balance += deposit
                    print("Deposit successful")
                    print("New balance is:", balance)
                    
                else:
                    print("Invalid deposit amount")
                    
            elif choice == "3":
                withdraw = float(input("Enter withdrawal amount: "))
                
                if withdraw <= 0: # 20000 <= 0 -> False
                    print("Invalid withdrawal amount")
                    
                elif withdraw > balance: # 20 > 50 -> False
                    print("Insufficient balance")
                    
                else:
                    balance -= withdraw
                    print("Withdrawal successful")
                    print("Remaining balance is:", balance)
            elif choice == "4":
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice")
        break
    else:
        attempts -= 1
        print("Wrong PIN")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Your account is locked")'''



# Pyramid Star Pattern

'''rows = int(input("Enter number of rows: "))

for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)'''
    
    
# text = "   Python   "
# clean_text = text.strip()
# print(clean_text)



# text = "apple,banana,mango"
# result = text.split(",")
# print(result)



# text = "Python"
# print(text[4])


# s = "Python"
# print(s[-1])


# color =["red","blue","green"]
# color.pop()
# print(color)


# color = ["red","blue","green"]
# print(color[1])



# numbers = list(range(1, 11))
# print(numbers)



# numbers = [1, 2, 3, 2, 2, 5]
# print(numbers.count(3))


# fruits1 = ["apple", "banana"]
# fruits2 = ["mango", "orange"]

# print(fruits1 + fruits2) 



# Personal_address = {
#     "Name" : "Rose",
#     "Education" : "Bsc.CS"
# }
# print(Personal_address.get("Education"))
# print(Personal_address.get("Age"))

# vegies = {"tomato","potato","cucumber"}
# vegies.add("ladies finger")
# print(vegies)


# num1 = {1,2,3,4,5}
# num2 = {2,3,4,5,6}
# print(num1 & num2)



# personal_adress ={
#     "Name":"Rose",
#     "Age":20
# }
# print(personal_adress.keys())
# if "Age" in personal_adress:
#     print("Yes")


# def greet():
#     print("hello")
# greet()


# num = 1 
# for num in range(10):
#     if num == 5:
#         break
#     print(num)


# i = 1
# for i in range (5):
#     if i == 3:
#         continue
#     print (i)


# num = 24

# if num % 2 == 0:
#     print("its an even number")
# else:
#     print("its an odd number")


# school_staff  = {
#     "IOT_staff" : "Shelin",
#     "AI_staff" : "Abi",
#     "Full_stack" : "Shabin"
# }

# for each_staff in school_staff:
#     print(school_staff[each_staff])


# def add(a, b):
#     return a + b
# result = add(5, 2)
# # print(result)

# def add_args(*args, **kwargs):
#     ...

# def argsss(*args):
#     print(args)
#     print(type(args))
#     print(args[0])
#     print(args[-1])

# # argsss(1,1,23,4,6)

# def keyargsss(**kwargs):
#     print(kwargs)

# # keyargsss(num=1)


# def any_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
            
# any_func()                                 


# def rose_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
# rose_func()

# lambda
# def square_normal(num):
#     return num ** 2
# square = square_normal(5) 
# print(square)


# square = lambda x: x ** 2
# print(square(21))

# list_lambda = lambda i: "Even" if i % 2 == 0 else "Odd"
# print(list_lambda(11))

# func_lambda = lambda i : "Divisble by 3" if i % 3 == 0 else "not"
# print(func_lambda(21))

# Try catch

# while True:
#     try:
#         def num (name, age, course,):
#             return a + b

#         a=int(input("Enter num 1: "))
#         b=int(input("Enter num 2: "))

#         result = num(a, b)
#         print(result)

#     except:
#         print("Invalid input")
        
        
        
        
# while True:
#     try:
#         def num (name, age, course,):
#             return
#         name=(input("enter your name: "))
#         age=(input("enter  your age: "))
#         course = (input("Enter your course: "))
        
#         result = num(name, age, course)
#         print(result)
#         if name==name:
#             continue
#         elif age==age:
#             continue
#         elif course==course:
#             print ("data uploaded")
#             break
#     except:
#         print("give the full details")
            
            
# while True:
#     try:
#         num1 = int(input("Enter num1: "))
#         num2 = int(input("Enter num2: "))
#         operator = input("Enter Operator, To exit Enter X : ")
        
#     except:
#         print("Invalid number")
#         continue
        
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1-num2)
#     elif operator == "/":
#         try:
#             print(num1/num2)
#         except:
#             print("Try Another number")
#     elif operator == "*":
#         print(num1*num2)
#     elif operator == "%":
#         print(num1%num2)
#     elif operator == "X":
#         break
#     else:
#         print("Invalid  Number")


'''Mark = int(input("Enter mark: "))
if Mark >= 90 :
    print("A Grade")
elif Mark >= 75:
    print("B Grade")
elif Mark >= 50:
    print("C Grade")
else:
    print("Failed")'''
    
    
'''Age = int(input("Enter your Age: "))
if Age >= 90 :
    print("A Grade")
elif Age < 13:
    print(" Child")
elif Age < 20:
    print("Teenager")
elif Age < 60 :
    print("Adult")
else:
    print("Senior Citizen")'''
    
    
   
'''vowel = ["A", "E", "I","O","U", "a","e","i","o","u"]
letter = input("Enter a Letter: ")

if letter in vowel:
    print("Its vowel")
else:
    print("Its not a vowel")'''
# if letter.lower() == "a" or letter.lower() == "e":
#     print("Yes")

# word = "shEljin"
# vowels = ["a", "e", "i", "o", "u"]

# count = 0
# for char in word:
#     if char.lower()  in vowels :
#         count += 1
    
# print(count)



# word = "rithinrose"
# vowels = ["a", "e", "i", "o", "u"]

# count = 0
# for char in word:
#     if char.lower() not in vowels :
#         count += 1
    
# print(count)



'''word = "rithin rose"
reverse = ""

for char in word:
    reverse = char + reverse
print(reverse)'''


'''
word = "olo"
if word == word[::-1]:
    print("its palindrom")
else:
    print("not palindrom")'''
    
    
    
    
# num = 5

# fact = 1
# for i in range(1, num + 1):
#     fact*=i
# print(fact)

# human = ["rose", "rithin","sheljin","rose"]
# name = []

# for i in human:
#     if i in name:
#         # print(name)
#         ...
#     else:
#         name.append(i)
#         # print(i)

# print(name)

# print(set(human))


'''number = [12,43,56,78,98]

max = number[0] # 12
for result in number: # 43
    if result > max: # 43 > 12 -> True
        max = result
print(result)'''



'''num = [12,34,56,78,90]

min = num[0]
for i  in num:
    if i < min:
        min = i
print(min)'''


# num = [12,34,56,78,90]

# sum = 0
# for i in num:
#     sum = sum + i
# print(sum)


# def fib(n):
    
#     a = 0
#     b = 1
    
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
        
#         for i in range(4):
            
#             c = a+b
#             a = b
#             b = c
            
#             if c < 100:
#                 print(c)
                
# # user = int(input("Enter the value: "))
# # n = user
# # fib(n)

# n = -1
# # 0,1,1,2,3,5,8,13,21,34,55,....

# res = [0, 1]

# for i in range(n-2):
#     new_fib = res[-1] + res[-2]
#     res.append(new_fib)

# print(res)



'''pyramid'''

# n = 1

# for i in range(1,6):
#     print(n * i)


'''reversed_pyramid'''
# n = ("*")
# count = 5

# for i in range(5):
#     print(n * (count - i))



# n = 10

# for i in range(n-1):
#     print("*" * i)

# for i in range(1,n):
#     print("*" * (n-i))



# n = ("-")

# for i in range(10-1):
#     print(n * i)

# for i in range(1,10):
#     print(n * (10 -i))



# n = ("*")

# for i in range(1,6):
#     print(n * i, "!")
    
  
# n = ("*")  

# for i in range(1,6):
#     print(n * (7 -i))
# for i in range(1,8-1):
#     print(n * i)


# n = (" ")

# for i in range(6+1):
#     print((n * (7-i)+ "*"))


# n = (" ")

# for i in range(6+1):
#     print((n * (7-i)+ "*" * i))


# for i in range(5, 0, -1):
#     print("*" * i)



# n = " "

# for i in range(5,0,-1):
#     print((n * i)+ "*" * i)




# n = 5

# for i in range(5):
#     print("*" * n )


# for i in range(1, 8):
#     print(" " * (7 - i) + "*" * i)
    
# for i in  range(1,6):
#     print(" " *(5-i)+ "*" * i+ "*" * (i -1))


# for i in  range(6,0,-1):
#     print(" " *(7-i)+ "*" * i+ "*" * (i -1))



# for i in range(0,5):
#     print(" " *(4-i)+ "*" + "-" * i+ "-" * (i -1)+"*")
    
# print("**********")

"""
  1
 234
56789


1
23
456
7891
12345
"""


# n = ["1","2","3","4","5","6","7","8","9","10"]
# length = 3

# count = 0           # 0

# for i in range(length):
#     for _ in range(i):
#         print(n[count])
#         count += 1
        
#         if count >= 10:
#             count = 0

# num = 1
# for i in range(1,5):
#     num = num + 1
#     for j in range(i):
#             num = num + 1
#             print(i)


num = 1
val = 5

for i in range(1,5):
    print(" " * (val - i), end="")
    
    for j in range(2*i-1):
        print(num, end="")
        num += 1
        
        if num > 10:
            num = 1
    print()




