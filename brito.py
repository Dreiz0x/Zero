#!/usr/bin/env python3
# cambio.py

import os
import re

def modificar_layout():
    # Ruta del archivo
    file_path = "app/src/main/res/layout/activity_main.xml"
    
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"Error: No se encontró el archivo {file_path}")
        return False
    
    # Leer el contenido actual
    with open(file_path, 'r', encoding='utf-8') as file:
        contenido = file.read()
    
    # Realizar modificaciones específicas
    # Ejemplo 1: Cambiar color de fondo
    contenido = re.sub(
        r'android:background="#0D0D0F"',
        'android:background="#1A1A1F"',
        contenido
    )
    
    # Ejemplo 2: Modificar el texto del bottom navigation
    contenido = re.sub(
        r'android:text="Curriculum"',
        'android:text="Plan de Estudios"',
        contenido
    )
    
    # Ejemplo 3: Cambiar colores de las líneas de los módulos
    # Módulo A - Rojo más vibrante
    contenido = re.sub(
        r'android:background="#E53935"',
        'android:background="#FF1744"',
        contenido
    )
    
    # Módulo B - Azul más vibrante
    contenido = re.sub(
        r'android:background="#1E88E5"',
        'android:background="#00B0FF"',
        contenido
    )
    
    # Módulo C - Verde más vibrante
    contenido = re.sub(
        r'android:background="#43A047"',
        'android:background="#00E676"',
        contenido
    )
    
    # Módulo D - Amarillo más vibrante
    contenido = re.sub(
        r'android:background="#F5C400"',
        'android:background="#FFEA00"',
        contenido
    )
    
    # Ejemplo 4: Agregar padding adicional al ScrollView
    contenido = re.sub(
        r'<ScrollView',
        '<ScrollView\n        android:paddingBottom="8dp"',
        contenido
    )
    
    # Ejemplo 5: Aumentar tamaño de texto del título
    contenido = re.sub(
        r'android:textSize="11sp"',
        'android:textSize="12sp"',
        contenido
    )
    
    # Guardar el archivo modificado
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contenido)
    
    print(f"✅ Archivo modificado exitosamente: {file_path}")
    print("\nCambios realizados:")
    print("  • Fondo cambiado de #0D0D0F a #1A1A1F")
    print("  • Texto 'Curriculum' → 'Plan de Estudios'")
    print("  • Colores de líneas más vibrantes")
    print("  • Padding adicional al ScrollView")
    print("  • Tamaño de texto aumentado de 11sp a 12sp")
    
    return True

def hacer_backup():
    """Crear un backup del archivo original"""
    original_path = "app/src/main/res/layout/activity_main.xml"
    backup_path = "app/src/main/res/layout/activity_main.xml.bak"
    
    if os.path.exists(original_path):
        with open(original_path, 'r', encoding='utf-8') as src:
            with open(backup_path, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
        print(f"📋 Backup creado en: {backup_path}")
        return True
    return False

if __name__ == "__main__":
    print("=== Editor de Layout Android ===\n")
    
    # Crear backup antes de modificar
    hacer_backup()
    
    # Realizar modificaciones
    if modificar_layout():
        print("\n✨ Modificaciones completadas con éxito")
    else:
        print("\n❌ Hubo un error al modificar el archivo")
