from ui import showMainMenu, pause ,box


def main():
    while True:
        op = showMainMenu()
        if op == "1":
            pause()
        elif op == "2":
            pause()
        elif op == "3":
            pause()
        elif op == "4":
            pause()
        elif op == "5":
            pause()
        elif op == "6":
            print("Cerrando!!")
            break
        elif op.lower() == "init":
            pause()    
        else:
            print("Opcion invalida.")
            pause()

if __name__ == "__main__":
    main()
