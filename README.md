# INSTRUCCIONES PARA EJECUTARLO Y COMPILARLO:

## Para correrlo:

- Crear entorno virtual.
- Instalar flet con: **pip install flet**.

## Para desplegarlo:

### Dependencias a instalar:

- **pip install pillow** para convertir el icono jpeg a ico
- **pip install pyinstaller** para crear el ejecutable

## Crear ejecutable con icono:

- Ejecutar el siguiente comando para empaquetar para windows: **flet pack app.py --icon .\assets\LogoSuperExplorer.jpeg --add-data "assets;assets"**
- Para empaquetar para Linux o MacOS usar el comando: **flet pack app.py --icon .\assets\LogoSuperExplorer.jpeg --add-data "assets:assets"**
