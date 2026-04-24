# Explicacion y uso de FOR

# for i in range(5):
#     print(i+1)

# num=int(input("Ingrese un numero"))
# for i in range(1,num+1):
#     print("repeticion", i)

# num=int(input("Ingrese un numero para ver tabla de multiplicacion hasta el 10: "))
# for i in range(10):
#     print(f"{num} X {i+1} = {num*(i+1)}")

# notas=int(input("Ingrese el total de pruebas que tiene: "))
# suma=0
# for i in range(notas):
#     n=float(input(f"ingrese su {i+1}° nota: "))
#     suma=suma+n
# prom=suma/notas
# print(f"El promedio de sus notas es: {round(prom)}")

# num=int(input("Ingrese un numero: "))
# total=0
# for i in range(1, num+1):
#     total+=i
# print(f"El resultado es {total}")

# Factorial

num=int(input("Ingrese un numero: "))
total=0
for i in range(1, num+1):
    total+=i
print(f"El resultado es {total}")