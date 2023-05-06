# EXAMPLE 01 OBJECTIVE: Print square root of negative or positive number using if and operators.


# number= int(input("Enter a number and I'll get its square root!  "))
# if(number>0):
#     print("Since the number is greater than zero, it can be calculated.")
#     root=number**(1/2)
#     print("The root is : ",root)
# else:
#     print("Roots of negative numbers can not be calculated.")
# print("\nThanks for your input!")


# Example: 02 Write conditional statements to print value of 0 to 1 and 1 to 0 and numbers in between.

# number= int(input("Enter a number : "))
# if(number==1):
#     number=0
# if(number==0):
#     number=1
# if(number>2 or number<0):
#     print("The number is between ")
# print(number)


# EXAMPLE#03

# number= int(input("Enter a number between 10-20 : "))
# if(number>=10 and number<=20):
#     print("The condition has been met.")
# else:
#     print("You did it wrong.")


#EXAMPLE#04

# number= int(input("Enter a number between 10-20 or 30-40: "))
# if(number>=10 and number<=20) or (number>=30 and number<=40):
#     print("The condition has been met.")
# else:
#     print("You did it wrong.")


# EXAMPLE#01 : Print Karachi Pakistan 100 times in a separate line

# i=0
# while(i<100):
#     print("Karachi Pakistan\n")
#     i+=1
# i=100
# while(i>=1):
#     print("Karachi Pakistan\n")
#     i-=1


# Example # 2 : Take collection of number input from user. Print the total positive and negative number.

# pcount=0
# ncount=0
# count=int(input("How many numbers you want?"))
# i=0
# while(i<count):
#     num=int(input("Enter the number : "))
#     if(num>=0):
#         pcount+=1
#     else:
#         ncount+=1
#     i+=1
# print("Pcount : ",pcount,"\nNcount : ",ncount)


# Example # 3 : Fixed a Letter from a to e and then ask the user to guess that letter until correct letter entered.

value='c'
userValue=input("Enter a character between a and e. ")
while(userValue!=value):
    print("Incorrect value.")
    userValue=input("Enter a character between a and e. ")
print("Welcome User!")

# EXERCISE # 01
# def volumeRange():
#     height=float(input("Enter height in cm: "))
#     width=float(input("Enter width in cm: "))
#     depth=float(input("Enter depth in cm: "))
#     volume=height*width*depth
#     if(volume>=1 and volume<=10):
#         print("Label is Extra Small.")
#     elif(volume>=11 and volume<=25):
#         print("Label is Small.")
#     elif(volume>=26 and volume<=75):
#         print("Label is Medium.")
#     elif(volume>=76 and volume<=100):
#         print("Label is Large.")
#     elif(volume>=101 and volume<=250):
#         print("Label is Extra Large.")
#     elif(volume>=251):
#         print("Label is Extra-Extra Large.")
#     else:
#         print("Enter valid values.")

# volumeRange()

# def employeeEfficiency():
#     timeReq=int(input("Enter the time required to complete the task : "))
#     if(timeReq>=2 and timeReq<3):
#         print(" The worker is highly efficient.")
#     elif(timeReq>=3 and timeReq<4):
#         print("The worker should be ordered to improve speed.")
#     elif(timeReq>=4 and timeReq<5):
#         print("The worker is to be given training to improve his speed.")
#     else:
#         print("The worker has to leave the company.")

# employeeEfficiency()

# def passVerify():
#     password="abc$123"
#     passWord=input("What is the password? ")
#     passWord=passWord.lower()
#     if(password==passWord):
#         print("Welcome!")
#     else:
#         print("I don't know you!")

# passVerify()

# n = 3
# while n >= 0:
#     n -= 1
#     print(n)
# n = 4
# while n >= 0:
#     n += 1
#     print(n)

# clist = ['Canada','USA','Mexico','Australia']
# for i in range(len(clist)):       #Make a program that lists the countries in the set
#     print(clist[i])

# for i in range(0,101):    #1.Create a loop that counts from 0 to 100
#     print(i)

# n=int(input("Enter the table number : "))     #2.Make a multiplication table using a loop
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# digit=10          #3.Output the numbers 1 to 10 backwards using a loop
# while(digit>0):
#     print(digit)
#     digit-=1

# count=0         #4.Create a loop that counts all even numbers to 10
# for i in range(11):
#     if(i%2==0):
#         count+=1
# print(count)

# num=100         #5.Create a loop that sums the numbers from 100 to 200
# for i in range(100):
#     num=num+i
# print(num)

# clist = ["Canada","USA","Mexico"]       #1.Make a program that lists the countries in the set below using a while loop.
# i=0
# while(i<3):
#     print(clist[i])
#     i+=1


    