import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")  #buscar ruta
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"): #contador de archivos dentro de ruta
        contador += 1
    return contador

READ_RECIPE = 1
CREATE_RECIPE = 2
CREATE_CATEGORY = 3
DELETE_RECIPE = 4
DELETE_CATEGORY = 5
EXIT = 6

def inicio():
    system("cls")
    print("*" * 50)
    print("*" * 5 + " Bienvenido al administrador de recetas " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas de encuentran en {mi_ruta}")         # mi ruta variable previa via Path
    print(f"total recetas es: {contar_recetas(mi_ruta)}")  # funcion contar .glob(**/*.txt)

    # limitar o condicionar el imput, isnumeric(), no permite colocar str, y se limitaon los int a 6
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion: ")
        print('''
        [1] Leer receta
        [2] Crear receta nueva
        [3] Crear categoria nueva 
        [4] Eliminar receta
        [5] Eliminar categoria
        [6] Salir del programa''')
        eleccion_menu = input()   # imput para cerrar el loop, cuando la opcion sea valida
    return int(eleccion_menu)         # retun un valor valido

def mostrar_categoria(ruta):
    print("categorias")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():   #.iterdir iterar dentro del dir, cada un de sus elementos
        carpeta_str = str(carpeta.name)         #carpeta es str  solo queremos el nombre
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\n Elije una categoria: ")
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("**/*txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = "x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) +1):
        eleccion_receta = input("\nElije una receta: ")

    return  lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada.")
            existe = True
        else:
            print("Lo siento esta receta ya existe")


def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu categoria")
        nombre_categoria = input()

        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada.")
            existe = True
        else:
            print("Lo siento esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\n Presione V para volver al menu: ")

def handle_menu_options(menu):
    
    if menu == CREATE_CATEGORY:
        crear_categoria(mi_ruta)
        return

    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)

    if menu == READ_RECIPE:
        mis_recetas = mostrar_recetas(mi_categoria)

        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
            return
        
        mi_receta = elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        
    elif menu == CREATE_RECIPE:
        crear_receta(mi_categoria)
    elif menu == DELETE_RECIPE:
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
    elif menu == DELETE_CATEGORY:
        eliminar_categoria(mi_categoria)

while True:

    menu = inicio()

    if  menu == EXIT:
        break

    handle_menu_options()

    volver_inicio()
