num = int(input("Escribe un número positivo por favor"))

while num < 0:
    print("El número ingresado es inferior a 0")
    num = int(input("Escribe un número positivo por favor"))
pass

print(num, " gracias =)")
