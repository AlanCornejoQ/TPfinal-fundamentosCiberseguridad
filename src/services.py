import getpass
from src.ui import box, pause
import src.storage as storage

def _requerirBoveda():
    if not storage.bovedaExiste():
        print("no existe boveda. escriba 'init' en el menu para crear una.")
        pause()
        return False
    return True

def _asegurarSesionAbierta():
    # si no hay boveda, avisa
    if not _requerirBoveda():
        return False
    # si ya esta abierta, OK
    if storage.estaAbierta():
        return True
    # pedir clave y abrir
    mpw = getpass.getpass("clave maestra: ")
    if storage.abrirBoveda(mpw):
        print("sesion abierta.")
        return True
    else:
        print("clave incorrecta.")
        pause()
        return False
def abrirBovedaService():
    
    box("ABRIR BOVEDA", padding=6)
    _asegurarSesionAbierta()
    pause()

def cerrarSesionService():
    if storage.estaAbierta():
        storage.cerrarBoveda()
        print("sesion cerrada.")
    else:
        print("no hay sesion abierta.")
    pause()
    
def inicializarBovedaService():
    
   
    box("INICIALIZAR BOVEDA", padding=10)
    if storage.bovedaExiste():
        print("ya existe una boveda. use las opciones del menu.")
        pause(); return
    while True:
        p1 = getpass.getpass("defina clave maestra: ")
        p2 = getpass.getpass("confirme clave maestra: ")
        if p1 != p2: print("no coinciden.")
        elif len(p1) < 8: print("use al menos 8 caracteres.")
        else: break
    storage.inicializarBoveda(p1)
    print("boveda creada correctamente.")
    pause()

def agregarService():
    box("AGREGAR NUEVA CONTRASENA",padding=10)
    if not _asegurarSesionAbierta(): return; pause()

def listarService():
    box("CONTRASENAS ALMACENADAS",padding=10)
    if not _asegurarSesionAbierta(): return; pause()

def buscarService():
    box("BUSCAR CONTRASENAS POR SERVICIO")
    if not _asegurarSesionAbierta(): return; pause()

def eliminarService():
    box("ELIMINAR CONTRASENA",padding=10)
    if not _asegurarSesionAbierta(): return; pause()

def cambiarClaveMaestraService():
    box("CAMBIAR CONTRASENA MAESTRA / INICIALIZAR")
    if not _asegurarSesionAbierta(): return; pause()