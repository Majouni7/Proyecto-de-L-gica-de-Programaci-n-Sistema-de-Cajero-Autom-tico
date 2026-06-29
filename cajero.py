#Proyecto integrador#
#Sistema de Cajero Automático#
#Estudiante: María José Yanchatipán Almache#
# Asignatura: Lógica de Programación#

#Los datos de cada cuenta están siendo guardados en un diccionario#

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



#En las opciones del menú se utiliza la tupla porque 
# los datos son estaticos#

menu = (
    "Consultar saldo",
    "Depositar dinero",
    "Retirar dinero",
    "Transferir dinero",
    "Ver historial",
    "Cerrar sesión"
)


#Se guarda en número de cuenta del usuario que inicie sesión#
usuario_actual = None

#La siguinte funcion permite al usuario iniciar sesión#
def iniciar_sesion():
 
#Indicamos que vamos a utilizar la variable que creamos al inicio
#  del programa y asi poder#
#guardar el número de cuenta#

 global usuario_actual

 #Solicitamos en número de cuenta del usuario#
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
        
        #Muestra al menú pricipal#
            mostrar_menu() 
        #Return True devuelve el valor True para indicar 
        # que la sesión fue exitosa#
            return True

        #La siguiente condición indica que terminó con error#
        else:
            print("PIN incorrecto.")
            return False
 else:
        print("La cuenta no existe.")
        return False
 

#####Menu Principal#####


#Esta función se encarga únicamente del menú principal#
def mostrar_menu():

#Guarda la opción que selecciona el usuario#
    opcion = 0

#El bucle indica que mientras la opción sea diferente de(!) 6,#
# el menu seguira apareciendo# 
    while opcion != 6:

        print("====================================")
        print("         MENÚ PRINCIPAL")
        print("====================================")

        #Se usa para mostrar una a una todas las 
        # opciones almacenadas en la tupla#
        for i in range(len(menu)):
            print(i + 1, ".", menu[i])


#En esta línea de código se solicita al usuario 
# que seleccione una opción del menú#
        opción = int(input("Seleccione una opción: "))

#Compara la opción elegida por el usuario, al escribir "1" entrara#
#al bloque de consultar saldo#
        if opción == 1:
            consultar_saldo()

       #Al no cumplirse con la opción anterior, revisa otra#
        elif opción == 2:
            depositar_dinero()

        elif opción == 3:
            retirar_dinero()

        elif opción == 4:
            transferir_dinero()

        elif opción == 5:
            ver_historial()

        elif opción == 6:
           print("Hasta luego", cuentas[usuario_actual]["nombre"])


       #Se aplica cuando el usuario escribe una opción que no existe#
        else:
            print("Opción no válida.")




#El objetivo de esta función es mostrar el saldo#
def consultar_saldo():

    print("====================================")
    print("      CONSULTA DE SALDO")
    print("====================================")



    #Accede al saldo del usuario actual utilizando el diccionario#
    saldo = cuentas[usuario_actual]["saldo"]

    print("Titular:", cuentas[usuario_actual]["nombre"])
    print("Saldo disponible: $", saldo)


######Depositar dinero#######


#Esta función permite al usuario depositar dinero en su cuenta.
def depositar_dinero():

    print("====================================")
    print("      DEPÓSITO DE DINERO")
    print("====================================")


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


###### Retirar dinero####


#Esta función permite retirar dinero de la cuenta.
def retirar_dinero():

    print("====================================")
    print("       RETIRO DE DINERO")
    print("====================================")


    #Solicita el monto que desea retirar.
    monto = int(input("Ingrese el monto a retirar: "))

    #Verifica que el monto sea mayor que cero #
    # y el usuario no retire más dinero del que tiene#
    if monto > 0:

        #Comprueba que exista saldo suficiente, menor
        #o igual en saldo base#
        if monto <= cuentas[usuario_actual]["saldo"]:

            #Actualiza el saldo y utilizamos la resta (-) para descontar el dinero del saldo##
            cuentas[usuario_actual]["saldo"] = cuentas[usuario_actual]["saldo"] - monto

            #Guarda el movimiento en el historial.
            cuentas[usuario_actual]["historial"].append("Retiro: $" + str(monto))

            print("Retiro realizado con éxito.")
            print("Nuevo saldo:", cuentas[usuario_actual]["saldo"])

        #Al no cumplir con el primer condicional no podra realizar movimientos#
        else:
            print("Saldo insuficiente.")

    else:
        print("El monto debe ser mayor que cero.")




        #### Transferir dinero###


#Esta función permite transferir dinero a otra cuenta.
def transferir_dinero():

#Realizamos una presentacion para la opcion de transferencia#
    print("====================================")
    print("       TRANSFERENCIA")
    print("====================================")

    #Solicita el número de la cuenta destino.
    cuenta_destino = int(input("Ingrese la cuenta destino: "))

    #Solicita el monto a transferir.
    monto = int(input("Ingrese el monto a transferir: "))

    #Verifica que la cuenta exista.
    if cuenta_destino in cuentas:

        #Verifica que el monto sea mayor que cero#
        if monto > 0:

            #Comprueba que exista saldo suficiente,
            #  el monto debe ser menor o igual al saldo disponible#
            if monto <= cuentas[usuario_actual]["saldo"]:

                #Resta el dinero de la cuenta actual.
                cuentas[usuario_actual]["saldo"] = cuentas[usuario_actual]["saldo"] - monto

                #Suma el dinero a la cuenta destino.
                cuentas[cuenta_destino]["saldo"] = cuentas[cuenta_destino]["saldo"] + monto

                #Guarda el movimiento en el historial.
                cuentas[usuario_actual]["historial"].append("Transferencia: $" + str(monto))

                print("Transferencia realizada con éxito.")

        ###Al no cumplir con alguna de las dos condicionales 
        #contamos con tres acciones por defecto##
            else:
                print("Saldo insuficiente.")

        else:
            print("El monto debe ser mayor que cero.")

    else:
        print("La cuenta no existe.")


        ## Historial##

#Esta función muestra todos los movimientos realizados.
def ver_historial():


    #Realizamos una presentación para la opción del historial#

    print("====================================")
    print("         HISTORIAL")
    print("====================================")

    ## De ser el caso de no tener movimientos, 
    # simplemente aparecerá el título y no mostrará movimientos# 
    for movimiento in cuentas[usuario_actual]["historial"]:
        print(movimiento)

#"Esta parte está al final porque primero es necesario definir todas 
# las funciones del programa. Una vez que ya están creadas, se llama a iniciar_sesion(), 
# que es la función que inicia la ejecución del sistema#

#==========================================================
# Programa principal
#==========================================================

#Inicia la ejecución del sistema.
iniciar_sesion()