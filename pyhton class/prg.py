# '''name="Rithin Rose"
# age=12
# height=182.5
# print(type(name))
# print(type(age))
# print(type(height))


# print(2+5)

# print(f"my name is {name} ,my age is {age} and my height is {height}")'''


# # name=input("enter your name : ")
# # print(name)

# '''num1=int(input("enter a num :"))
# num2=int(input("enter a num :"))

# total=num1+num2
# print(total)
# print(type(total))'''



# # fruits =["apple","Mamgo","grape"]
# # print(type(fruits))

# # color=("red","blue","green")
# # print(type(color))

# # bio={"name":"ROSE", "Age":12, "height":182.5}
# # print(type(bio))

# # hobbies={"music","playing","learning"}
# # print(type(hobbies))

# # isstudent=True
# # print(type(isstudent))





# '''Name=input("Enter your name:")
# print(Name)

# Age=int(input("Enter your age:"))
# print(Age)

# Fav_Sub=input("Enter your fav subject:")
# print(Fav_Sub)

# print(f"My name is {Name}, My age is {Age}, My Favorite Subject is {Fav_Sub}")'''

# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))

# add=(num1+num2)
# sub=(num1-num2)
# div=(num1/num2)
# mul=(num1*num1)
# fdiv=(num1//num2)
# mod=(num1%num1)
# expo=(num1**num2)

# print(add)
# print(sub)
# print(div)
# print(mul)
# print(fdiv)
# print(mod)
# print(expo)


'''num=5
print(num)

num=num+5
print(num)

num+=5
print(num)'''

'''x=10
print(x)

x+=5
print(x)


a=32
b=32

if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")'''

'''Age=18

if Age>=13 and Age<=19:
    print("teenager")

else:
    print("Not Teenager")'''

# num=22

'''if num%3==0 and num%7==0:
    print("Divisible")
else:
    print("Not Divisible")'''
    
#Mark=int(input("Enter the Mark: "))

'''if Mark>=50:
    if Mark>=90:
        print("Exellent")
    else:
        print("pass")
else:
 print("fail")'''


'''num=int(input("Enter the value: "))

if num>0:
   print("positive")
elif num<0:
   print("Negative")
else:
   print("Neutral")'''

'''Age=int(input("Enter your Age: "))
if Age>=18:
    print("Eligble to vote")
else:
    print("Not Eligble")


Voter=True
if Voter==True and Age>=18:
    print("You are elgible to vote")
else:
    print("You not elgible to vote")

ration=True
aadhar=True
if ration==True or aadhar==True:
    print("You can Aplly for voter id" )
else:
    print("you need id for apply voter id")'''



'''Age=int(input("Enter your age: "))

if Age<=0:
    print("Invalid Age")

elif Age>=18 and Age<99:
    print("You can vote")

elif Age<18:
    print("You are not elgible to vote")

elif Age>=100:
    print("You are too old to vote")'''
        

'''Speed=int(input("Enter the speed: "))

if Speed>=120:
    print("Overspeeding")
elif Speed>=80 and Speed<120:
    print("Fast")
elif Speed>=40 and Speed<79:
    print("Moderate")
elif Speed<=40:
    print("Slow")'''
'''
age=int(input("Enter your Age: "))

if age<5:
    print("Free")
elif age>=5 and age<=12:
    print("child ticket")
elif age>=13 and age<=59:
    print("adult ticket")
else:
    print("Senior Ticket")'''
#A loop lets you repeat a block of code multiple times
#for loop fixed number of time automatically incresed
'''for i in range(1,20):    #
    if i%2==0:
        print(i)

word="programming"
# nums=[16,5,67,90]
for letter in word:
    print(letter) '''

#used when you want to repeat something as long as a condition is true Manually increased

'''num=1

while num<=10:
    print(num)
    num+=1'''

'''num=1
while  num<=15:
    if num%2==1:
     print(num)
    num+=1'''

'''n=10
while n>=1:
    print(n)
    n-=1'''

#break    terminate the loop anf even if the loop comdition is true 

'''num=1
for num in range(1,35):
    if num==27:
        break
    print(num)'''


# num=int(input("Enter the value: "))
'''while True:
    num=int(input("Enter the value: "))
    if num==0:
     break
print("loop stop")'''

'''num=int(input("Enter the number: "))
while num!=45:
    num=int(input("Enter the number: "))
print("0  founded")'''


#continue statement skip the current literation and move to next
'''
num=1
for num in range(1,50):
    if num>=30:
        continue
    print(num) '''

'''num=1
for num in range(1,20):
    if num%3==0:
      print(num)'''

'''def welcome():
    print("Welcome to Python Programming")

welcome()'''


'''def student_mark(name,mark):
    mark=(name,mark)
    print(mark)
student_mark("rose",99)
student_mark("ajin",100)'''

'''def area(lenth,breadth):
    rect=(lenth*breadth)
    print(rect)
area(3,8)
area(5,9.8)'''

'''def sum(num1,num2):
    result=(num1-num2)
    print(result)
sum(23,21)
sum(34,9)'''
'''
name="rithinrose"
for i in name:
    print(i)

veg=["cabbage","carrot","tomato","potato","radish"]
for i in veg:
    print(i)'''

'''email="rithinrose@gmail.com"
for i in email:
    if i=="@" or i==".":
        continue
    print(i)'''


'''def add(num1,num2):
    total=(num1+num2)
    print(total)
add(4,12)

def div(num1,num2):
        if  num2==0:
            print("0 cant divisible")
        else:
           total=(num1/num2)
           print(total)
div(4,0)

def sub(num1,num2):
    total=(num1-num2)
    print(total)
sub(4,12)

def mul(num1,num2):
    total=(num1*num2)
    print(total)
mul(4,12)'''




'''def student_mark(name,tamil,eng,math,sci,soc):
    
    print(f"My is",name,"My Tamil mark",tamil,"My English mark",eng,"My Math mark",math,"My Science mark",sci,"My Social mark",soc)


student_mark("Rose",99,67,45,89,60)

def add(a,b):
    return a+b,a-b


ans=add(1,2)


print(ans)'''


# def mul(a):
#     result=a*a*a
#     return result 



# ans=mul(5)

'''def avg(x,y,z):
    result=(x+y+z)/3
    return result


ans=avg(10,20,30)
print(ans)'''
'''
def sum_number(n):
    total=0
    for sum in range(1,n+1):
        total+=sum
    return total
ans=sum_number(6)
print(ans)'''

#callback Function
'''def greet(name):
    print(f"my name is {name}")

def welcome(name):
    print(f"Welcome {name}")



def hii(callback,username):
    return callback(username)


ans=hii(welcome,"Abishek")
ans1=hii(greet,"Abishek")'''
'''
def greetUser(name,callback):
    print(f"Hello {name}")
    return callback(name)

def sayGoodbye(username):
    print(f"Goodbye {username}") 


ans=greetUser("Priya",sayGoodbye)'''

'''def calculateSquare(number, callback):
    print(number*number)
    return callback(doneMessage)

def doneMessage(done):
    print("Square calculation finished")

ans=calculateSquare(3,doneMessage)'''


# creating list
'''fruits=["apple","orange","grapes"]

print(fruits)

print(fruits[1])

fruits.append("mango")
print(fruits)

fruits.pop()

print(fruits)

fruits.remove("apple")
print(fruits)


fruits[1]="cherry"
print(fruits)'''


'''flowers=["Jasmine","Rose","sunflower"]
print(flowers)

flowers.append("lotus")
print(flowers)

flowers.pop()
print(flowers)

flowers.remove("sunflower")
print(flowers)

flowers[0]="LILLY"
print(flowers)'''



'''colors=("red","blue","green")

print(colors[1])'''

'''
car={"brand":"audi","color":"red","no_of_seat":4}
print(car)
print(car["brand"])

car["color"]="blue"
print(car)

car["type"]="petrol"
print(car)


del car["no_of_seat"]
print(car)'''


'''Employee={"name":"ROSE","age":20,"salary":30000,"department":"CS"}
print(Employee)

Employee["location"]="current area"
print(Employee)

Employee["salary"]=40000
print(Employee)

del Employee["salary"]
print(Employee)'''



# student1={"abi","john","ram","ram"}

# student1.add("rose")

# student1.remove("john")
# print(student1)


# print("ram" in student1)


'''
dance={"ram","dena","abi","joe"}
sports={"joel","raghul","ram","dena"}


class1=dance|sports
print(class1)


classRep=dance&sports
print(classRep)

remaing=dance-sports
print(remaing)'''



'''first={30,47,68,90,97}
print(first)

first.add(38)
print(first)

first.remove(68)
print(first)

second={30,57,90,67,48}


both=first|second
print(both)

comon=first&second
print(second)

remain=first-second
print(remain)'''


'''list=[1,2,3,4,5,22,445,6777]

print(max(list))
print(min(list))
print(sum(list))'''

'''numbers=[12,45,67,97,58,66,28,9,32,44]

print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))


sum=sum(numbers)
len=len(numbers)


print(sum/len)'''

'''fav_number=(12,34,56,78,21,43,)
first_three=fav_number[0:3]
print(first_three)
last_two=fav_number[4:]
print(last_two)
print(len(fav_number))'''

'''class clg():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sayhello(self):
        print(f"say hello {self.name} and my age is {self.age}")

    def sayhi(self):
        print(f"say hii {self.name}")

    def sayhow(self):
        print(f"say how {self.name}") 

ans=clg("ROSE",20)

ans.sayhello()
ans.sayhow()
ans.sayhi()'''


'''class rose():
    def __init__(self,username):
        self.username=username
    def usrgreet(self):
        print(f"hello {self.username}")

ans=rose("Rithin rose")

ans.usrgreet()'''

'''class num():
    def __init__(self,number):             # if we add return function we have to store the function into a variable
        self.number=number 
    def add_num(self):
        result=self.number+self.number
        print(result)
ans=num(10)

ans.add_num()'''



# class clg():
#     def __init__(self,name):
#         self.name=name
    
#     def college(self):
#         print(f"{self.name} studies in NMCC")

# class studies(clg):
#     def depart(self):
#         print(f"{self.name} department in PG Computeer Science")
    
# class student(studies):

#     def year(self):
#         print(f"{self.name} studies in III Year")

# class staff(student):

#     def sub(self):
#          print(f"{self.name} have 5 subject in 3rd year")

# staff1=staff("Rithin Rose")

# staff1.college()
# staff1.depart()
# staff1.year()
# staff1.sub()



# a=1
# b=2

# b,a=a,b
# print(b,a)
        
        # 1
        
'''name = "rose"
print(type(name))'''

        #2
        
'''str= "123"
num = int(str)
print(num)
print(type(num))'''


        # 4
'''a="""
name
age"""
print(a)'''

    # 6
'''a=1
b=2

b,a=a,b
print(b,a)'''


        #   7
'''a=12
b=6                #it shows without decimal value
print(a//b)

a=12
b=6                #it shows with float value
print(a/b)
'''

        #    8

'''Name = "Rose"
Age = 20
Qulifation = "Bsc Computer Science"
College = "NMCC"
print(f"My name is", Name,"My Age is", Age,"I have completed", Qulifation,"in",College)'''


# text = "I like Python"
# new_text = text.replace("Python", "Java")
# print(new_text)

# text = "I am learning Python "
# if "Python" in text:
#     print("found")
# else:
#     print("not found")

'''text = "Python"
new_text=text[::5]
print(new_text)'''

# print("Hi" * 3)

