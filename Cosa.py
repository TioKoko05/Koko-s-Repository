# while True:
#     try:
#         num=int(input("ingresar un numero: "))
#     except:
#         print("Solo numeros enteros")
#     break

code=6969
while True:
    try:
        passw=int(input("Ingresar su clave: "))
        if passw==code:
            print("Ingreso exitoso")
            break
        else:
            print ("ingreso invalido")
    except ValueError as er:
        print("Clave invalida, intente denuevo")
        print(er)