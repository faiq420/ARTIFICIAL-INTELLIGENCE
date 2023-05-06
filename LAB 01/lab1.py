import math

# s='abc'
# print(dir(s))
# help(s.find)

# a=int(input("Value of a: "))
# b=int(input("Value of b: "))
# c=int(input("Value of c: "))
# d=int(input("Value of d: "))
# a,b,c,d=d,c,b,a
# print("After swapping:\n","a ",a," b ",b," c ",c," d ",d)

# print("Do you want to convert to celsius or fahrenheit?\n If celsius to fahrenheit,press a else press b")
# option=input()
# if(option=="a"):
#     Celsius=float(input("Temperature in Celsius: "))
#     Fahrenheit=Celsius*(9/5)+32
#     print("Temperature in Fahrenheit : ",Fahrenheit)
# elif(option=="b"):
#     Fahrenheit=float(input("Temperature in Fahrenheit: "))
#     Celsius=5*((Fahrenheit-32)/9)
#     print("Temperature in Celsius : ",Celsius)
# else:
#     print("Enter a valid option!")

print(dir(list))
# help(list.reverse)
# lst=[1,2,3]
# lst.reverse()
# print(lst)

# l= ['abc', 'xyz', 'aba', '1221'] 
# count=0
# for i in range(len(l)):
#     if(len(l[i])>=2 and l[i][0]==l[i][len(l[i])-1]):
#         count+=1
# print("Count :- ",count)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={**dic1,**dic2,**dic3}
# print(dic4)
# print(dir(dic1))

# colors= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']
# for i in range(len(colors)):
#     if len(colors[i])>5:
#         colors[i]=colors[i].lower()
# print(colors)
# del colors[4:6]
# colors.remove('Red')
# print(colors)

# x = 6
# if (type(x) is int): 
#  print ("true") 
# else: 
#  print ("false")

# x = 7.2
# if (type(x) is not int): 
#  print ("true") 
# else: 
#  print ("false")

# list1=[1,2,3,4,5] 
# list2=[6,7,8,9] 
# for item in list1: 
#  if item in list2: 
#     print("overlapping") 
#  else: 
#     print("not overlapping")

# a=6.5
# a//=3
# print("floor divide=",a)
# a**=5
# print("exponent=",a)

# a=60
# b=13
# c=a&b   #and
# d=a|b   #or
# e=a^b   #xor
# f=~a    #not/complement
# g=a<<2  #left shift
# h=a>>2  #right shift
# print("Line 1 ",c)
# print("Line 2 ",d)
# print("Line 3 ",e)
# print("Line 4 ",f)
# print("Line 5 ",g)
# print("Line 6 ",h)

# f= 10.9
# i=4
# print ("Our float value is %i and Our integer value is %f." % (f, i))

# def primeNumber(n):
#     primes=[]
#     for i in range(2,n):
#             boolean=False
#             j=2
#             while j<(math.sqrt(n)):
#                 if(n%j==0):
#                     boolean=True
#                     break
#                 j+=1
#             if(boolean==False):
#                 primes.append(j)
#                 # print("It is a prime number.")
#             # else:
#                 # print("It is not prime number.")
#     print(primes)
# primeNumber(13)
# def primeNumbers():
#     primes=[]
#     limit=int(input("Prime no.s within range: "))
#     for i in range(2,limit+1): 
#         j=2
#         while j<limit+1:
#             if i%j==0:
#                 break
#             j+=1
#         if i == j:
#             primes.append(i)
#     print(primes)

# primeNumbers()