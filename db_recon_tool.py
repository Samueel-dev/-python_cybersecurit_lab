import sqlite3

def run_db_recon(db_file):
    try:
        # Conexión a la base de datos objetivo
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        print(f"--- INFORME DE RECONOCIMIENTO: {db_file} ---")

        # 1. Extraer todos los nombres de las tablas existentes
        query_tables = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        cursor.execute(query_tables)
        tables = cursor.fetchall()

        if not tables:
            print("No se encontraron tablas accesibles.")
            return

        for table in tables:
            table_name = table[0]
            print(f"\n[TABLA DETECTADA] {table_name}")

            # 2. Extraer metadatos de las columnas de cada tabla
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            # Cabecera de la auditoria de columnas
            header = f"{'ID':<4} | {'NOMBRE':<20} | {'TIPO':<15} | {'PK':<5}"
            print(header)
            print("-" * len(header))

            for col in columns:
                # col[0]=id, col[1]=name, col[2]=type, col[5]=primary_key
                cid, name, dtype, _, _, pk = col
                is_pk = "SI" if pk == 1 else "NO"
                print(f"{cid:<4} | {name:<20} | {dtype:<15} | {is_pk:<5}")

    except sqlite3.Error as e:
        print(f"Error de acceso a la base de datos: {e}")
    finally:
        if conn:
            conn.close()

# --- Ejecucion ---
# Puedes probarlo con 'sakila.db' o 'chinook.db'
run_db_recon("sakila.db")
          
