from ui import showMainMenu, pause ,box
from services import *

def main():
    while True:
        op = showMainMenu()
        if op == "1":
            agregarService()
        elif op == "2":
            listarService()
        elif op == "3":
            buscarService()
        elif op == "4":
            eliminarService()
        elif op == "5":
            cambiarClaveMaestraService()
        elif op == "6":
            print("Cerrando!!")
            break
        elif op.lower() == "init":
            inicializarBovedaService()     
        else:
            print("Opcion invalida.")
            pause()

if __name__ == "__main__":
    main()
