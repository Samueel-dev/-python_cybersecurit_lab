import sqlite3

def find_sensitive_columns(db_file):
    # Lista de palabras clave que suelen contener datos sensibles
    sensitive_patterns = [
        'pass', 'pwd', 'token', 'secret', 'key', 
        'mail', 'phone', 'address', 'card', 'salary',
        'dni', 'ssn', 'birth'
    ]
    
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        print(f"--- AUDITORIA DE PRIVACIDAD: {db_file} ---")
        
        # Obtenemos todas las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()

        findings_count = 0

        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            for col in columns:
                column_name = col[1].lower()
                
                # Verificamos si algun patron sensible esta en el nombre de la columna
                for pattern in sensitive_patterns:
                    if pattern in column_name:
                        print(f"[ALERTA] Columna sensible detectada:")
                        print(f" -> Tabla: {table_name}")
                        print(f" -> Columna: {col[1]} (Tipo: {col[2]})")
                        print("-" * 30)
                        findings_count += 1
                        break
        
        if findings_count == 0:
            print("No se detectaron columnas con nombres sospechosos.")
        else:
            print(f"Auditoria finalizada. Se encontraron {findings_count} posibles fugas de PII.")

    except sqlite3.Error as e:
        print(f"Error durante el escaneo: {e}")
    finally:
        if conn:
            conn.close()

# --- Ejecucion ---
# Prueba con 'sakila.db' o 'chinook.db'
find_sensitive_columns("sakila.db")
                  
