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
    box("AGREGAR NUEVA CONTRASEÑA",padding=10)
    if not storage.bovedaExiste():
        print("no existe boveda. escriba 'init' para crear una.")
        pause(); return
    if not storage.estaAbierta():
        mpw = getpass.getpass("clave maestra: ")
        if not storage.abrirBoveda(mpw):
            print("clave incorrecta."); pause(); return

    servicio = input("Ingrese el nombre del servicio: ").strip()
    usuario  = input("Ingrese el usuario o correo: ").strip()
    pw1 = getpass.getpass("Ingrese contrasena: ")
    pw2 = getpass.getpass("Confirmar contrasena: ")

    if not servicio or not usuario:
        print("servicio y usuario no pueden ser vacios.")
    elif pw1 != pw2:
        print("no coinciden, no se guardo.")
    elif len(pw1) == 0:
        print("contrasena no puede ser vacia.")
    else:
        try:
            storage.agregarEntrada(servicio, usuario, pw1)
            print(f"contrasena para '{servicio}' guardada correctamente")
        except Exception as e:
            print(f"error al guardar: {e}")

    pause()

def listarService():
    box("CONTRASEÑAS ALMACENADAS",padding=10)
    if not storage.bovedaExiste():
        print("no existe boveda. escriba 'init' para crear una.")
        pause(); return
    if not storage.estaAbierta():
        mpw = getpass.getpass("clave maestra: ")
        if not storage.abrirBoveda(mpw):
            print("clave incorrecta."); pause(); return

    try:
        filas = storage.listarEntradas()
        from src.ui import imprimirTablaBasica
        imprimirTablaBasica(filas)

        # pedir id para ver detalle
        sel_txt = input("\nSeleccione numero para ver detalles o 0 para volver: ").strip()
        try:
            sel = int(sel_txt)
        except ValueError:
            sel = 0

        if sel != 0:
            try:
                claro = storage.obtenerEntrada(sel)
                print(f"\nDetalle id={sel}:")
                print(f"contrasena (descifrada): {claro}")
            except Exception as e:
                print(f"error al obtener detalle: {e}")

    except Exception as e:
        print(f"error al listar: {e}")

    pause()

def buscarService():
    box("BUSCAR CONTRASEÑAS POR SERVICIO")
    if not _asegurarSesionAbierta(): return; pause()

def eliminarService():
    box("ELIMINAR CONTRASEÑA",padding=10)
    if not _asegurarSesionAbierta(): return; pause()

def cambiarClaveMaestraService():
    box("CAMBIAR CONTRASEÑA MAESTRA / INICIALIZAR")
    if not _asegurarSesionAbierta(): return; pause()