# length = float(input("lenght"))
# width = float(input("width"))
# area = length*width
# show = f"With width {width} and length {length} of the room, its area is equal to {area}"
# print(show)

# name = "Dmitry"
# age = 34
# is_active = True
# subscription = ()

# name = input("Your name? ")
# email = input("Your email? ")
# age = int(input("Your age? "))
# height = float(input("Your height? "))
# is_active =  True

#Списки
# my_list = []
# my_list = [2024, 3.12]
# some_data = ['Python']
# my_list.extend(some_data)
# my_list.insert(1, 'Python')
# my_list.reverse()
# print(my_list)

#Slovnik
# data = {"year": 2024, "lang": "Python", "version": 3.12}

# cat = {"nick": "Simon", "age": 7, "characteristics": ["лагідний", "кусається"]}
# info = {"status": "vaccinated", "breed": True}
# age = cat.get("age")
# cat.update(info)
# print(cat)


                                    # 1 MODUL 1 LESSON

#a = 2.2
#print(type(a))

# a = None
# print(type(a))
# <class 'NoneType'>

#____a = 4
#print(a )

# a = input("chislo : ")
# b = input("chislo : ")
# print(f"sum {int(a)+int(b)}")

                                  # 1 MODUL 2 LESSON

                                  # 2 MODUL 1 LESSON

# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)  # Виведе: Привіт, Олексій!

# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал

# def string_to_codes(string: str) -> dict:
#     # Ініціалізація словника для зберігання кодів
#     codes = {}  
#     # Перебір кожного символу в рядку
#     for ch in string:  
#         # Перевірка, чи символ вже є в словнику
#         if ch not in codes:
#             # Додавання пари символ-код в словник  
#             codes[ch] = ord(ch)  
#     return codes

# result = string_to_codes("qwertyuiopoijhgfdsazxcvbnmm")
# print(result)

# x = 50

# def func() -> None:
#     x = 2
#     print('Зміна локального x на', x)  # Зміна локального x на 2

# func()
# print('Глобальний x як і раніше', x)  # x як і раніше 50

# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x

# result = func_outer()  # 5

# x = 50

# def func():
#     global x
#     print('x дорівнює', x)  # x дорівнює 50
#     x = 2
#     print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2

# func()
# print('Значення x складає', x)# Значення x складає 2

# def greet(name, message="Привіт"):
#     print(f"{message}, {name}!")

# greet("Dima")
# greet("Olia", message="Hi")

# def func(a, b=5, c=10):
#     print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)

# # a дорівнює 3, b дорівнює 7, а c дорівнює 10
# func(3, 7)

# # a дорівнює 25, b дорівнює 5, а c дорівнює 24
# func(25, c=24)

# # a дорівнює 100, b дорівнює 5, а c дорівнює 50
# func(c=50, a=100)

# def print_all_args(*args):
#     for arg in args:
#         print(arg)

# print_all_args(1, 'hello', True)

# def factorial(n):
#     if n == 0: # базовий випадок
#         return 1
#     else:
#         return n * factorial(n-1) # рекурсивний випадок

# print(factorial(5)) # виведе 120

# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(15))

# is_next = None
# num = int(input("Enter the number of points: "))
# if num >= 83:
#     is_next = True
# else:
#     is_next = False

# work_experience = int(input("Enter your full work experience in years: "))

# if work_experience > 5:
#     developer_type = "Senior"
# elif work_experience >1 :
#     developer_type = "Middle"
# else :
#     developer_type = "Junior"
# print(developer_type)

# num = int(input("Enter a number: "))

# if num > 0 :
#     if  num % 2 == 0 :
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0 :
#         result = "Negative number"
# else:
#         result = "It is zero"
# print(result)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num >= 0:
#     sum = sum + num
#     num = num - 1    
# print(sum)

# message = "Never argue with stupid people, they will drag you down to\
#             their level and then beat you with experience."
# search = "r"
# result = 0
# for chair in message:
#     if chair == search:
#         result = result + 1
# print(result)
  
pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
       
except ZeroDivisionError:
        print('Divide by zero completed!')   

