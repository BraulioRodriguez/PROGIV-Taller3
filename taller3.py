### Programacion de Computadoras IV
## Taller 3
# Braulio Rodriguez 8-899-1093

from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

db = cliente["Taller3"]
base = db['SlangsPanameños']
col = base["Panama"]


#Funciones
def add(var1, var2):
    base.insert_one(({'Slangs': var1, 'Significado': var2}))


def edit(var3, var4):
    base.update_one(({'Slangs': var3}, {'$set': {'Significado': var4}}))


def delete(var5):
    base.delete_many({'Slangs': var5})


def view():
    for palabras in base.find({}):
        print(palabras)


def search(var6):
    for palabras in base.find({'Slangs': var6}):
        print("El significado es: " + palabras)


# Menu de opciones
print("""
1. Insertar
2. Editar
3. Borrar
4. Visualizar
5. Buscar
6. Salir
""")

resp = 1
while(resp == 1):
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        print("Ingresar nuevo registro")
        var1 = input("Ingrese un slang panameno: ")
        var2 = input("Ingrese su significado: ")
        add(var1, var2)

    elif opcion == 2:
        print("Edite un registro: ")
        var3 = input("Ingrese un slang panameno ya existente: ")
        var4 = input("Ingrese su nuevo significado: ")
        edit(var3, var4)

    elif opcion == 3:
        print("Borre un registro")
        var5 = input("Ingrese el slang que desea eliminar")
        delete(var5)

    elif opcion == 4:
        print("Ver listado de palabras")
        view()

    elif opcion == 5:
        print("Buscar significado de palabra")
        var6 = input("Ingrese un slang panameno: ")
        search(var6)

    elif opcion == 6:
        break

    else:
        print("ERROR! OPCION INVALIDA")
    resp = input("Si desea continuar presione [1]")