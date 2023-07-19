# Este archivo es para descargar y descomprimir de lotus y descomprimir en una carpeta %temp%
import subprocess
import zipfile


if __name__ == '__main__':
 #subprocess.call([r'down.bat']) # Descargar el .zip
 with zipfile.ZipFile(r'package.zip', 'r') as zip_ref:
    zip_ref.extractall(r'unzip')
 print("Done")

