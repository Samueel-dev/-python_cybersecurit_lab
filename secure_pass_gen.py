import secrets
import string

def generate_secure_password(length=16):
    # Definimos los caracteres posibles
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Generamos una contraseña usando entropía del sistema operativo
    # Esto la hace virtualmente imposible de predecir por un ataque
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        
        # Verificamos que cumpla requisitos mínimos de seguridad
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
            
    return password

# --- Lógica de Ejecución ---
print("--- GENERADOR DE CONTRASEÑAS CRIPTOGRÁFICAS ---")

try:
    size = int(input("Longitud de la contraseña (recomendado 16+): "))
    if size < 8:
        print("Error: Por seguridad, la longitud minima es 8.")
    else:
        new_pass = generate_secure_password(size)
        print("\nTu nueva contraseña segura es:")
        print("-" * len(new_pass))
        print(new_pass)
        print("-" * len(new_pass))
        print("\n[INFO] Esta clave usa la libreria secrets (entropa real).")

except ValueError:
    print("Error: Introduce un numero valido.")
    
