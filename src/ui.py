def pause():
    input("presione enter para continuar...")

def box(title: str, padding: int = 1, minWidth: int = 30):
    # ancho interior = len(title) + 2*padding
    inner = max(len(title) + padding * 2, minWidth)
    top = "+" + "-" * inner + "+"
    middle = "|" + " " * padding + title.ljust(inner - padding * 2) + " " * padding + "|"
    print(top)
    print(middle)
    print(top)


def showMainMenu() -> str:
    print("+" + "-"*47 + "+")
    print("|             GESTOR DE CONTRASENAS             |")
    print("+" + "-"*47 + "+")
    print("[1] Agregar nueva contraseña")
    print("[2] Ver contraseñas almacenadas")
    print("[3] Buscar contraseñas por servicio")
    print("[4] Eliminar contraseña")
    print("[5] Cambiar contraseña maestra")
    print("[6] Salir")
    return input("\nSeleccione una opcion: ").strip()

def imprimirTablaBasica(filas):
    if not filas:
        print("(sin entradas)")
        return
    print("#  servicio                      usuario                         fecha")
    print("-"*85)
    for f in filas:
        print(f"{f['id']:<3}{f['servicio'][:26]:<28}{f['usuario'][:30]:<32}{f['creado_en']}")
