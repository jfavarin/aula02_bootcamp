import math

# exercicio 1 

try:
    n1 = int(input("Insira um numero inteiro: "))
    n2 = int(input("Insira um outro numero inteiro: "))

    res = n1 // n2

    print(res)
except ZeroDivisionError:
    print("cant divide to 0")

# exercicio 2

r_circ = float(input("Enter de circle radius: "))
a_circ = math.pi * r_circ ** 2

# print("{:.2f}".format(a_circ)) # old method
print(f"{a_circ:.2f}")

# exercicio 3

user_date = input("Insert a date on this format dd/mm/yyyy: ")

split_date = user_date.split("/")

print(f"The day is {split_date[0]}")
print(f"The month is {split_date[1]}")
print(f"The year is {split_date[2]}")

# exercicio 4 
#exemplo de tratamento de erro

try:
    #val = len("jonas") #correct
    val = len(3) #with error
    print(val)
except TypeError as e:
    print(e)
else:
    print("everything was ok")
finally:
    print("this will appears on the end if there was a error, or if not")

