person1 = { "name": "John",
"age": 36,
"country": "Norway"
}
def greeting(name): 
    print("Hello, " + name)


import datetime
import random
import time
import math



#TASK 1.1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(numbers)
# print("\nSquare every number of the said list:")
# square_numbers = list(map(lambda x: x ** 2, numbers))
# print(square_numbers)
# print("\nCube every number of the said list:")
# cube_numbers = list(map(lambda x: x ** 3, numbers))
# print(cube_numbers)

#TASK 1.2
# string = lambda x: True if x.startswith('K') else False
# print(string('Karachi'))
# string = lambda x: True if x.startswith('k') else False
# print(string('Karachi'))
# string = lambda x: True if x.startswith('K') else False
# print(string('University'))

# #TASK 1.3
# # present = datetime.datetime.now()
# # year = lambda x: x.year
# # month = lambda x: x.month
# # day = lambda x: x.day
# # time = lambda x: x.time()
# # print("DATETIME :-",present ,"\nYEAR :- ",year(present),"\nMONTH :-",
# # month(present),"\nDAY :-",day(present),"\nTIME :-",time(present))

#TASK 2.1
# f=open('cities.txt','a')
# num=int(input("Enter number of cities : "))
# for i in range(num):
#     name=input("Enter city:- ")
#     population=input("Enter population:- ")
#     mayor=input("Enter mayor:- ")
#     data="\n"+name+","+str(population)+","+mayor
#     f.write(data)

#TASK 2.2
# f=open('student.txt','w')
# data="Now we are AI students"
# f.write(data)


# print(time.time(),"Milliseconds from 1970")
# print(time.ctime(),"Present Datetime")
# print(math.sqrt(9))
# print(random.randint(1, 10))
# x = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(x)
# print("shuffled",x)
# y=random.sample(x, 2)
# print("sampled",y)