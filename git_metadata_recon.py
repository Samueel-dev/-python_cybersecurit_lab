import subprocess

def get_git_metadata():
    print("--- RECONOCIMIENTO DE METADATOS DE GIT ---")
    print("Analizando los ultimos 5 commits del repositorio...\n")

    # Definimos el comando para obtener: Hash abreviado, Autor, Email y Fecha
    # %h = hash, %an = author name, %ae = author email, %ar = date relative
    cmd = ["git", "log", "-n", "5", "--pretty=format:%h | %an | %ae | %ar"]

    try:
        # Ejecutamos el comando y capturamos la salida
        result = subprocess.check_output(cmd).decode('utf-8')
        
        if not result:
            print("No se encontraron commits en este repositorio.")
            return

        # Cabecera de la tabla
        header = f"{'HASH':<8} | {'AUTOR':<15} | {'EMAIL':<25} | {'FECHA'}"
        print(header)
        print("-" * len(header))

        print(result)

    except subprocess.CalledProcessError:
        print("Error: No parece ser un repositorio de Git o Git no esta instalado.")
    except FileNotFoundError:
        print("Error: El comando 'git' no se encuentra en el sistema.")

if __name__ == "__main__":
    get_git_metadata()
  
