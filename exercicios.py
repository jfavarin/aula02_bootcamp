import math

# exercicio 1 

n1 = int(input("Insira um numero inteiro: "))
n2 = int(input("Insira um outro numero inteiro: "))

res = n1 // n2

print(res)

# exercicio 2

r_circ = float(input("Enter de circle radius: "))
a_circ = math.pi * r_circ ** 2

# print("{:.2f}".format(a_circ)) # old method
print(f"{a_circ:.2f}")