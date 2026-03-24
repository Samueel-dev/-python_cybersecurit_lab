import hashlib
import os

def hash_password_secure(password):
    # Generamos una 'sal' aleatoria de 16 bytes
    salt = os.urandom(16)
    
    # Aplicamos PBKDF2 (Password-Based Key Derivation Function 2)
    # sha256: El algoritmo base
    # iterations: 100,000 (hace que el ataque de fuerza bruta sea muy lento)
    db_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000
    )
    
    return salt, db_hash

def verify_password_secure(stored_salt, stored_hash, input_password):
    # Para verificar, usamos la misma sal y el mismo numero de iteraciones
    new_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        input_password.encode('utf-8'), 
        stored_salt, 
        100000
    )
    return new_hash == stored_hash

# --- Logica Principal ---
print("--- SISTEMA DE SEGURIDAD NIVEL 3: SALTING ---")

password = input("Define tu contrasena maestra: ")
salt, hashed = hash_password_secure(password)

print("\n--- DATOS A GUARDAR EN BASE DE DATOS ---")
print("Sal (hex):", salt.hex())
print("Hash (hex):", hashed.hex())

print("\n--- PRUEBA DE AUTENTICACION ---")
login_attempt = input("Introduce tu contrasena para ingresar: ")

if verify_password_secure(salt, hashed, login_attempt):
    print("\n[OK] Acceso verificado con exito.")
else:
    print("\n[ERROR] Credenciales invalidas.")
