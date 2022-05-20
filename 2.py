#Diseñe un algoritmo que defina una lista vacia
#luego le agregue valores a la lista, teniendo en cuenta que su longitud debe ser menor a la digita por el usuario

print("----")
list1=[]
length = int(input("Digite el tamaño de la lista: "))
length = length-1
i = 0
while i !=length:
    user = int(input("Digite el valor de la lista: "))
    i += 1
    list1.append(user)
print(list1)