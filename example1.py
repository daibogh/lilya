a = input("введите имя и фамилию через пробел: ")

a = a.split(" ")
print(len(a))
print(type(a))# type(a) выводит тип переменной a
print(a[0])
print(a[1])
print(a[-1])# a[-1] = последний элемент a
# a[0] = a[0][0].upper() + a[0][1:]
# a[1] = a[1][0].upper() + a[1][1:]
# print("привет, ", end= "")
# print(" ".join(a), end="")
# print("!!!")