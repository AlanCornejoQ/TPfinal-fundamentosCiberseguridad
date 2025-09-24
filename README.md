# TPfinal-fundamentosCiberseguridad
# Gestor de Contraseñas Seguro (CLI)
## Nombre: Elmer Alan Cornejo Quito

Este proyecto corresponde al trabajo final de la materia **Fundamentos de Ciberseguridad**.  
Desarrollé un **gestor de contraseñas en consola (CLI)** que permite almacenar y administrar credenciales de manera segura, aplicando buenas prácticas de criptografía y manejo de datos.

El sistema fue implementado en **Python**, con almacenamiento en **SQLite** y cifrado mediante **AES-GCM**, además del uso de **hashes bcrypt** para proteger la clave maestra. Se aplicó también un control básico de versiones siguiendo la convención de commits.

---
## Funcionalidades principales

- **Inicializar bóveda** con una clave maestra (hash bcrypt + sal aleatoria).
- **Agregar nuevas contraseñas** para distintos servicios, usuarios o correos.
- **Listar todas las contraseñas** mostrando id, servicio, usuario y fecha de creación, con opción de ver el detalle descifrado.
- **Buscar por servicio** con filtro, mostrando resultados y permitiendo ver el detalle.
- **Eliminar contraseñas** por id, con confirmación.
- **Cambiar la clave maestra**, actualizando el hash y la sal en la base de datos.
- **Cerrar sesión** o salir del programa, cerrando la bóveda.

---
## Tecnologías empleadas

- **Lenguaje:** Python 3.11 (tested en Linux y Windows con Miniconda).  
- **Librerías principales:**
  - [bcrypt](https://pypi.org/project/bcrypt/) → hash de la clave maestra.
  - [cryptography](https://pypi.org/project/cryptography/) → cifrado simétrico AES-GCM.
  - [sqlite3](https://docs.python.org/3/library/sqlite3.html) → persistencia local de datos.  
- **Control de versiones:** Git con ramas feature (`main`,`feat/squeleto`, `feat/services`.) y merges descriptivos.  
- **Entorno:** Miniconda para gestionar dependencias de forma portable.

---
## Entorno (Conda / Miniconda)

Este proyecto usa **Conda/Miniconda** para asegurar un entorno reproducible.

### Crear el entorno desde `environment.yml` (adjunto en el repositorio)

#### Clonar el repositorio
```bash
git clone https://github.com/AlanCornejoQ/TPfinal-fundamentosCiberseguridad.git
cd TPfinal-fundamentosCiberseguridad
```
#### Crear el entorno
```bash
conda env create -f environment.yml
```
#### Activar el entorno
```bash
conda activate password-manager
```

### Para ejecutar la palicacion desde la raiz del proyecto
```bash
python -m src.main
```
---
## Uso básico

1. Al iniciar por primera vez, el sistema indica que no hay bóveda.  
   Para crearla, escribir el comando secreto:
   ```bash
   init
   ```
    y definir la clave maestra.

2. Opciones del menú principal:
```
[1] Agregar nueva contrasena
[2] Ver contrasenas almacenadas
[3] Buscar contrasenas por servicio
[4] Eliminar contrasena
[5] Cambiar contrasena maestra
[6] Salir
```


3. Ejemplo de flujo:
- Crear bóveda (`init`).
- Agregar entrada con opción `[1]`.
- Listar con opción `[2]` y seleccionar un id para ver la contraseña descifrada.
- Buscar con opción `[3]` escribiendo parte del nombre del servicio.
- Eliminar entrada con `[4]`.
- Cambiar la clave maestra con `[5]`.
