import secrets
import string

def generate_secure_key(length=32):
    # Definimos los caracteres: letras, números y símbolos
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generamos una llave criptográficamente segura
    secure_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_key

print("--- CYBERSECURITY TOOL: KEY GENERATOR ---")
new_key = generate_secure_key()
print(f"Tu nueva llave simétrica de 256-bits es:\n{new_key}")
print("\n  Guarda esta llave en un lugar seguro.")

