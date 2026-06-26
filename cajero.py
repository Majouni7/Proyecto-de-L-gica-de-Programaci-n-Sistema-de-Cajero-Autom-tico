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