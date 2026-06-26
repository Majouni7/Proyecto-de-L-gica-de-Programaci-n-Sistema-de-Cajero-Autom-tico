#Proyecto integrador#
#Sistema de Cajero Automático#
#Estudiante: María José Yanchatipán Almache#
# Asignatura: Lógica de Programación#

#Los datos de cada cuenta están siendo# 
# guardados en un diccionario#

cuentas = {
    134340: {
        "pin": 3991,
        "nombre": "Agust D",
        "saldo": 1000,
        "historial": []
    },

    130613: {
        "pin": 7991,
        "nombre": "April",
        "saldo": 500,
        "historial": []
    }
}
#Menu principal#
#En las opciones del menu se utiliza la tupla#
#porque los datos son estaticos#

menu = (
    "Consultar saldo",
    "Depositar dinero",
    "Retirar dinero",
    "Transferir dinero",
    "Ver historial",
    "Cerrar sesión"
)
#Se guarda en nuemero de cuenta del ussuario que inicie sesion#
usuario_actual = None

#La sigueinte funcion permite al usuario iniciar sesion#
def iniciar_sesion():
 
#Indicamos que vamos a utilizar la variable#
#que creamos al inicio del programa, asi poder#
#guardar el numero de cuenta#
 global usuario_actual

 #Solicitamos en numero de cuenta del usuario#
 cuenta = int(input("Ingrese su número de cuenta: "))

#Solicitamos el PIN#
 pin = int(input("Ingrese su PIN: "))

#Verificamos si la cuenta existe dentro del diccionario#
 if cuenta in cuentas:

        # Verifica si el PIN es correcto para la cuenta ingresada#
        if cuentas[cuenta]["pin"] == pin:

            #Guarda cual usuario inicio sesion#
            usuario_actual = cuenta

            print("\n====================================")
            print(f"Bienvenido(a) {cuentas[cuenta]['nombre']}")
            print("Inicio de sesión exitoso.")
            print("====================================")
        

        #Indica que la sesion termino con exito#
            return True

        #La siguiente condicion indica que termino con error#
        else:
            print("\nPIN incorrecto.")
            return False
 else:
        print("\nLa cuenta no existe.")
        return False
 
 #Programa Principal#
 # Definimos a la función para iniciar el programa
iniciar_sesion()
    
#Menu Principal#

#Esta funcion se encarga unicamente del menu principal#
def mostrar_menu():

#Guarda la opcion que selecciona el usuario#
    opcion = 0

#El bucle indica que mientras la opcion sea diferente de(!) 6,#
# el menu seguira apareciendo# 
    while opcion != 6:

        print("\n====================================")
        print("         MENÚ PRINCIPAL")
        print("====================================")

#Se usa para mostrar una a una todas las opciones almacenadas en la tupla#
        for i in range(len(menu)):
            print(f"{i + 1}. {menu[i]}")

        opcion = int(input("\nSeleccione una opción: "))

#Compara la opcion elegida por el usuario, al escribir "1" entrara#
#al bloque de consultar saldo#
        if opcion == 1:
            print("Consultar saldo")

#Al no cumplirse con la opcion anterior, revisa otra#
        elif opcion == 2:
            print("Depositar dinero")

        elif opcion == 3:
            print("Retirar dinero")

        elif opcion == 4:
            print("Transferir dinero")

        elif opcion == 5:
            print("Ver historial")

        elif opcion == 6:
            print(f"\nHasta luego {cuentas[usuario_actual]['nombre']}")

#Se aplica cuando el usuario escribe una ipcion que no existe#
        else:
            print("Opción no válida.")
