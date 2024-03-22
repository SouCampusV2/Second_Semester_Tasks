# Question n.4 - false, it is 2 different object and have diff cell(spot) in the memory

# class School:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# sch = School(100,7)
# sch2 = School(100,7)
# print(sch is sch2)



# Question n.5 - will be 17

# class School:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# sch = School(100,7)
# sch2 = School(300,17)

# sch = sch2

# print(sch.b)



# Question n.7 - we can't create instance of class in class without function for example

# class Abit():
#     def __init__(self, name):
#         self.name = name
    
#     def apply(self, un):
#         return f"{self.name} tries to apply to {un}"
#     abiturient = Abit()
#     print(abiturient.apply())



# Question n.11 - b is остаток(рус.) but it is int, so b is int

# a = 10
# b = a // 3
# print(isinstance(a,type(b)), isinstance(b,float))



# Question n.12 - object a and b have different links, they are not in one cell(spot)

# class Bank: 
#     def __init__(self, money):
#         self.money = money

# a = Bank(100)
# b = Bank(100)

# print(a is b, a == b, a.money == b.money)
# print(a)
# print(b)
# print(type(a))
# print(type(b))



# Question n.13 - in t we have 2 link to arrays, and when we change arrays than we can see changes in t

# a = [1, 7]
# b = [1, 7]
# t = (a, b)

# a.append(11)
# b.append(10)
# print(t[0] is not t[1], t[0][2])



# Question n.14 - Will show information about function

# print(print)



# Question n.15 - Car/Ckass is object

# class Car:
#     def __init__(self, speed):
#         self.speed = speed

# print(isinstance(Car, object))



# Question n.17 a and b different objects, have diff cell(spot) in memory, but the data itself ==

# a = {1, 2, 3}
# b = {1, 2, 3}

# print(a is b, a == b)



# Question n.18

# The difference is that one counts the number of references, 
# and as soon as the variable disappears, there are fewer references 
# by 1 and the variable is removed from memory. 
# And the second option, this works when the variable has no references; 
# it is deleted by the Garbage Collection



# Question n.19

# Immutable objects, you assign only once; 
# when assigning a new value, a new object is created with its own place in memory. 
# And mutable ones, for example, are an array, you can always change its values, etc.



# Question n.19

# Args accepts a tuple of data, and quargs accepts data as a dictionary
