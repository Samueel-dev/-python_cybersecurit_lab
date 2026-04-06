import hashlib
import os

def calculate_file_hash(filepath):
    # Usamos SHA-256 por su alta seguridad y resistencia a colisiones
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Leemos el archivo en bloques para no saturar la RAM
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def main():
    print("--- MONITOR DE INTEGRIDAD DE ARCHIVOS ---")
    filename = input("Introduce el nombre del archivo a monitorear: ")
    
    if not os.path.exists(filename):
        print("Error: El archivo no existe.")
        return

    # Paso 1: Generar el hash inicial (Base de referencia)
    current_hash = calculate_file_hash(filename)
    print(f"\nHash actual (SHA-256): {current_hash}")
    
    # Paso 2: Simulacion de verificacion
    print("\n[!] Realiza cambios en el archivo y presiona Enter para verificar...")
    input("Presiona Enter cuando estes listo...")
    
    new_hash = calculate_file_hash(filename)
    
    if current_hash == new_hash:
        print("\n[OK] El archivo no ha sido modificado. Integridad garantizada.")
    else:
        print("\n[ALERTA] EL ARCHIVO HA SIDO MODIFICADO O CORROMPIDO.")
        print(f"Hash original: {current_hash}")
        print(f"Hash nuevo:    {new_hash}")

if __name__ == "__main__":
    main()
  
