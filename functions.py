import os
import glob
import shutil
import re

def eliminarCarpetasVacias(ruta):
    if ruta:
        elementos = os.listdir(ruta)
        carpetas = [elemento for elemento in elementos if os.path.isdir(os.path.join(ruta, elemento))]

        vacias = 0

        if carpetas:
            for carpeta in carpetas:
                carpeta_ruta = os.path.join(ruta, carpeta)

                if not os.listdir(carpeta_ruta):
                    vacias += 1
                    print("Eliminando: " + carpeta_ruta)
                    os.rmdir(carpeta_ruta)
            mensaje = "No hubo carpetas vacias." if vacias == 0 else "Se eliminaron las carpetas vacías."
            return True, mensaje
        else:
            mensaje = "No hay carpetas en la ruta."
            return True, mensaje
    else:
        mensaje = "No has introducido una ruta."
        return True, mensaje
    
def organizarCarpetas(ruta):
    if ruta:
        #Extensiones de los archivos:
        tiposDeArchivos = {
        "--Documentos--":["*.pdf", "*.docx", "*.txt", "*.doc", "*.odt", "*.docm", "*.rtf", "*.csv", "*.xls", "*.xlsx", "*.xlsm", "*.ods", "*.pps", "*.ppt", "*.ppsx", "*.pptx", "*.ppsm", "*.pptm", "*.potx", "*.odp"],
        "--Videos--":["*.mp4", "*.mkv", "*.avi", "*.mov", "*divx", "*.flv", "*.mpg", "*.wmv", "*.wpl", "*.mpeg"],
        "--Fotos--":["*.png", "*.jpg", "*jpeg", "*.svg", "*.bmp", "*.ico", "*.webp", "*.gif", "*.heic", "*.nef", "*.crw", "*.id"],
        "--Audios--":["*.wav", "*.mp3", "*.acc", "*.wma", "*.flac", "*.midi", "*.ogg", "*.m3u"],
        "--Photoshop--":["*.psd"],
        "--Ilustrator--":["*.ai"],
        "--Comprimidos--":["*.rar", "*.zip", "*.rar5", "*.7z", "*.ace", "*.gz"],
        "--Imagenes CD o DVD--":["*.iso", "*.cue", "*.img", "*.rom"],
        "--Internet--":["*.html", "*.xml", "*.url", "*.css", "*.css", "*.js", "*.php", "*.swf"],
        "--Ejecutables--":["*.exe"],
        "--Archivos temporales--":["*.sfk", "*.camrec"],
        "--Codigo--":["*.py", "*.vim", "*.md"],
        "--Desconocido--": ["*.mb", "*.abr"],
        "--Minecraft--": ["*.mcpack"],
        "--Packet_tracer--": ["*.pkt", "*.pka", "*.pksz"],
        "--Drawio--": ["*.drawio", "*.dwg", "*.sv$"]
        }

        movidos = 0

        for carpetaDeArchivo in tiposDeArchivos:
            if os.path.exists(os.path.join(ruta, carpetaDeArchivo)):
                for formato in tiposDeArchivos[carpetaDeArchivo]:
                    archivos = glob.glob(os.path.join(ruta + "\\", formato))
                    for archivo in archivos:
                        if os.path.exists(os.path.join(ruta, carpetaDeArchivo, os.path.basename(archivo))):
                            nombre_sin_extension = re.match(r'(.+?)(\.\w+)?$', archivo).group(1)
                            nuevo_nombre = nombre_sin_extension + "_Duplicado" + formato[1:]
                            os.rename(archivo, nuevo_nombre)
                            archivo = nuevo_nombre
                        shutil.move(archivo, os.path.join(ruta, carpetaDeArchivo))
                        movidos += 1
            else:
                for formato in tiposDeArchivos[carpetaDeArchivo]:
                    archivos = glob.glob(os.path.join(ruta + "\\", formato))
                    if archivos and not (os.path.exists(os.path.join(ruta, carpetaDeArchivo))):
                        os.mkdir(os.path.join(ruta, carpetaDeArchivo))
                    for archivo in archivos:
                        shutil.move(archivo, os.path.join(ruta, carpetaDeArchivo))
                        movidos += 1

        mensaje = "No hay archivos para ordenar" if movidos == 0 else "El ordenamiento termino correctamente."
        return True, mensaje

    else:
        mensaje = "No has introducido una ruta."
        return True, mensaje