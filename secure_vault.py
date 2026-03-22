import sqlite3

# --- CRYPTO ENGINE (Symmetric) ---
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # If decrypting, we just reverse the shift
    actual_shift = shift if mode == 'encrypt' else -shift
    for char in text:
        result += chr((ord(char) + actual_shift))
    return result

# --- 🗄️ DATABASE SETUP ---
db = sqlite3.connect("vault.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY, service TEXT, data TEXT)")
db.commit()

# ---  MAIN PROGRAM ---
SECRET_KEY = 7 # This is your master key

print("--- WELCOME TO YOUR SECURE VAULT (DAY 21) ---")
choice = input("Do you want to (A)dd a secret or (V)iew secrets? ").upper()

if choice == 'A':
    service = input("Service name (e.g., GitHub): ")
    content = input("Secret content: ")
    # Encrypt before saving!
    encrypted_content = caesar_cipher(content, SECRET_KEY)
    cur.execute("INSERT INTO secrets (service, data) VALUES (?, ?)", (service, encrypted_content))
    db.commit()
    print("Secret encrypted and stored safely.")

elif choice == 'V':
    cur.execute("SELECT service, data FROM secrets")
    print("\n--- YOUR STORED SECRETS ---")
    for service, encrypted_data in cur.fetchall():
        # Decrypt to show it to the owner
        decrypted = caesar_cipher(encrypted_data, SECRET_KEY, mode='decrypt')
        print(f"Service: {service.ljust(15)} | Secret: {decrypted}")

db.close()

