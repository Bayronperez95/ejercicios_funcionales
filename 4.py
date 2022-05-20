#Crear un diccionario de géneros literarios con el siguiente contenido
#Narrativa                   Dramático                 Lirico
#La Vorágine                 El hechizo del agua       Los Heraldos negros
#Don Quijote de la mancha    Primero es ella           Los versos del capitán
#Con la soga al cuello       Hasta que salga el sol    cantar de Mio Cid
#Se debe mostrar la información organizada por categorías

def diccionario(gen): 
    print('\n\t<--genero_literarios-->\n')
    for i in gen: 
        print(i,":",gen[i])

#generos literarios 

gen_narrativo={"genero_narrativo":"la voragine," "don quijote de la mancha," "con la soga al cuello"}
print(gen_narrativo)

gen_dramatico={"genero_dramatico":"el hechico del agua, ""primero es ella, " "hasta que salga el sol"}
print(gen_dramatico)

gen_lirico={"genero_lirico":"los heraldos negros," "los versos del capitan, " "cantar de mio cid"}
print(gen_lirico)