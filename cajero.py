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

            print("====================================")
            print("Bienvenido(a)", cuentas[cuenta]["nombre"])
            print("Inicio de sesión exitoso.")
            print("====================================")
        
        #Muestra al menu pricipal#
            mostrar_menu() 
        #Indica que la sesion termino con exito#
            return True

        #La siguiente condicion indica que termino con error#
        else:
            print("PIN incorrecto.")
            return False
 else:
        print("La cuenta no existe.")
        return False
 

#Menu Principal#

#Esta funcion se encarga unicamente del menu principal#
def mostrar_menu():

#Guarda la opcion que selecciona el usuario#
    opcion = 0

#El bucle indica que mientras la opcion sea diferente de(!) 6,#
# el menu seguira apareciendo# 
    while opcion != 6:

        print("====================================")
        print("         MENÚ PRINCIPAL")
        print("====================================")

#Se usa para mostrar una a una todas las opciones almacenadas en la tupla#
        for i in range(len(menu)):
            print(i + 1, ".", menu[i])

        opcion = int(input("Seleccione una opción: "))

#Compara la opcion elegida por el usuario, al escribir "1" entrara#
#al bloque de consultar saldo#
        if opcion == 1:
            consultar_saldo()

#Al no cumplirse con la opcion anterior, revisa otra#
        elif opcion == 2:
            depositar_dinero()

        elif opcion == 3:
            retirar_dinero()

        elif opcion == 4:
            transferir_dinero()
        elif opcion == 5:
            ver_historial()

        elif opcion == 6:
           print("Hasta luego", cuentas[usuario_actual]["nombre"])
#Se aplica cuando el usuario escribe una opcion que no existe#
        else:
            print("Opción no válida.")

#El objetivo de esta funcion es mostrar el saldo#
def consultar_saldo():

#Accede al saldo del usuario actual utilizando el diccionario#
    saldo = cuentas[usuario_actual]["saldo"]

    print("====================================")
    print("        CONSULTA DE SALDO")
    print("====================================")
    print("Titular:", cuentas[usuario_actual]["nombre"])
    print("Saldo disponible: $", saldo)

    #Depositar dinero#
    #Esta función permite al usuario depositar dinero en su cuenta.
def depositar_dinero():

    #Solicita el monto que desea depositar.
    monto = int(input("Ingrese el monto a depositar: "))

    #Verifica que el monto sea mayor que cero.
    if monto > 0:

        #Actualiza el saldo del usuario.
        cuentas[usuario_actual]["saldo"] = cuentas[usuario_actual]["saldo"] + monto

        #Guarda el movimiento en el historial.
        cuentas[usuario_actual]["historial"].append("Depósito: $" + str(monto))

        #Muesta al usuario la informacion realizada y actualizada#
        print("Depósito realizado con éxito.")
        print("Nuevo saldo:", cuentas[usuario_actual]["saldo"])

      #Al no cumplir con el primer condicional no puede ingresar para relizar movimientos#  
    else:
        print("El monto debe ser mayor que cero.")
        