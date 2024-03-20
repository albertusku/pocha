#!/bin/bash

# Verificar si Python 3 está instalado
if ! command -v python3 &>/dev/null; then
    echo "Python 3 no está instalado. Instalando Python 3..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Verificar si existe un archivo llamado "requirements.txt" en el directorio actual
if [ -f "requirements.txt" ]; then
    echo "El archivo requirements.txt existe en el directorio actual."
    
    # Leer los nombres de los paquetes del archivo requirements.txt
    while IFS= read -r package; do
        # Verificar si el paquete está instalado
        if ! pip3 show "$package" > /dev/null 2>&1; then
            echo "Instalando el paquete $package..."
            pip3 install "$package"
        else
            echo "El paquete $package ya está instalado."
        fi
    done < "requirements.txt"
else
    echo "El archivo requirements.txt no existe en el directorio actual."
    echo "Ejecutando pipreqs . para generar el archivo requirements.txt..."
    pipreqs .
    echo "Verificando los paquetes generados..."
    
    # Leer los nombres de los paquetes del archivo requirements.txt generado
    while IFS= read -r package; do
        # Verificar si el paquete está instalado
        if ! pip3 show "$package" > /dev/null 2>&1; then
            echo "Instalando el paquete $package..."
            pip3 install "$package"
        else
            echo "El paquete $package ya está instalado."
        fi
    done < "requirements.txt"
fi

# Ejecutar el script interface.py
echo "Ejecutando el script interface.py..."
python3 interface.py