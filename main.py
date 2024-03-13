bandas=[]


#Construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100
while(opcion!=5):
    banda={}
    print("1. Registrar Banda")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una Bnada")
    print("5. SALIR")

    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        #creando los datos del diccionario
        banda["id"]=int(input("Digita el id: ")) #Como mostrar el imput con el radoom
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ") #Como validar entradas de string
        banda["Clasificacion"]=input("Clasificacion: ") #Como validar entradas de string
        banda["timepo"]=int(input("Tiempo: ")) 
        banda["costo"]=int(input("Costo: $"))
        
        #Agregando un diccionario a una lista
        bandas.append(banda)

    elif opcion==2:

        bandaBuscada=input("Digita el nombre de la Banda que estas Buscando: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                #Como lo encontre muestro los datos de bandaAuxiliar
                print(f"id: {bandaAuxiliar["id"]} --- nombre: {bandaAuxiliar["nombre"]}")
            else:
                print("Parce siga buscando....")
    
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass


