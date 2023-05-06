# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# x = lambda a, b: a * b
# print("product :- ",x(5, 6))

# x = lambda a, b: a + b
# print("sum :- ",x(5, 6))

# cars = ["Ford", "Volvo", "BMW"]
# print("length :- ",len(cars))
# print(cars[0])
# for x in cars:
#     print(x)

import task
# task.greeting("Miss Humera Basher")

# a=task.person1["age"]
# print(a)


# person1 = { "name": "John", "age": 36,
# "country": "Norway"
# }

# f = open("demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

f=open("demofile.txt","x")

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())
