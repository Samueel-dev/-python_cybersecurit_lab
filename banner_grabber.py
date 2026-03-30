import socket

def grab_banner(ip_address, port):
    # Intentamos obtener la informacion de servicio de un puerto abierto
    print(f"--- ANALISIS DE SERVICIO: {ip_address}:{port} ---")
    
    try:
        # Creamos el socket y definimos un timeout para no esperar siempre
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        
        # Conectamos al objetivo
        sock.connect((ip_address, port))
        
        # Algunos servicios envian el banner apenas te conectas (ej. SSH, FTP)
        # Otros esperan una peticion (ej. HTTP), aqui probamos la lectura directa
        banner = sock.recv(1024)
        
        if banner:
            # Decodificamos los bytes y limpiamos espacios en blanco
            decoded_banner = banner.decode('utf-8', errors='ignore').strip()
            print(f"Banner detectado: {decoded_banner}")
        else:
            print("No se recibio respuesta automatica del servicio.")
            
    except socket.timeout:
        print("Error: El tiempo de espera se agoto (Timeout).")
    except ConnectionRefusedError:
        print("Error: La conexion fue rechazada. El puerto podria estar cerrado.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
    finally:
        sock.close()

# --- Configuracion del Objetivo ---
# Para pruebas seguras, puedes usar servidores de prueba legales como:
# scanme.nmap.org (Puerto 22 para SSH)
target_ip = "45.33.32.156" # IP de scanme.nmap.org
target_port = 22

grab_banner(target_ip, target_port)

