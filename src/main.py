from src.ui import showMainMenu, pause, box
from src.services import *

def main():
    import src.storage as storage
    
    while True:
        if not storage.bovedaExiste():
            box("NO HAY BOVEDA")
            print("No se encontro una boveda.")
            print("Escriba 'init' para crear una nueva boveda.\n")
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
            if storage.estaAbierta():
                storage.cerrarBoveda()
            print("Cerrando!!")
            break
        elif op.lower() == "init":
            inicializarBovedaService()
        elif op.lower() == "logout":
            cerrarSesionService()  
        else:
            print("Opcion invalida.")
            pause()

if __name__ == "__main__":
    main()
