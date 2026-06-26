#Proyecto integrador#
#Sistema de Cajero Automático#
#Estudiante: María José Yanchatipán Almache#
# Asignatura: Lógica de Programación#

#Los datos de cada cuenta están siendo# 
# guardados en un diccionario#

cuentas = {
    134340: {
        "pin": 4991,
        "nombre": "Agust",
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
 
#Indicamos que utilizar una variable global que#
#se puede utilizar en cualquier parte del programa#
 global usuario_actual

 #Solicitamos en numero de cuenta del usuario#
 cuenta = int(input("Ingrese su número de cuenta: "))

#Solicitamos el PIN#
 pin = int(input("Ingrese su PIN: "))

#Verificamos si la cuenta existe#
 if cuenta in cuentas:

        # Verifica si el PIN es correcto
        if cuentas[cuenta]["pin"] == pin:

            usuario_actual = cuenta

            print("\n====================================")
            print(f"Bienvenido(a) {cuentas[cuenta]['nombre']}")
            print("Inicio de sesión exitoso.")
            print("====================================")

            return True

        else:
            print("\nPIN incorrecto.")
            return False

    


