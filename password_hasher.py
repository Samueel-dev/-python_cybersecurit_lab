import hashlib

def hash_password(password):
    # Convertimos el texto a bytes y aplicamos el algoritmo SHA-256
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def verify_password(stored_hash, input_password):
    # Para verificar, hasheamos la entrada y comparamos con el guardado
    new_hash = hash_password(input_password)
    return new_hash == stored_hash

# --- Logica Principal ---
print("--- SISTEMA DE HASHING DE SEGURIDAD ---")

password_original = input("Crea una nueva contrasena: ")
hash_guardado = hash_password(password_original)

print("\nContrasena protegida (SHA-256):")
print(hash_guardado)

print("\n--- SIMULACION DE LOGIN ---")
while True:
    intento = input("Introduce tu contrasena para entrar: ")

    if verify_password(hash_guardado, intento):
        print("ACCESO CONCEDIDO: El hash coincide.")
        break
    else:
        print("ACCESO DENEGADO: La contrasena es incorrecta.")

