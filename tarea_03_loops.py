diccionario = {"Felipe": 4, "Xavi": 55, "Ros": 3}

for k,v in diccionario.items():
    print("Participante: ", k, ", Valor: ", v)

pass

nums = diccionario.values()
maxNum = max(nums)
minNum = min(nums)
print("El número más alto es, ", maxNum,", y el más bajo,", minNum)
