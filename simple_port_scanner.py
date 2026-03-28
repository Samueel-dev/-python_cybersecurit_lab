import socket

def scan_ports(target_host, port_list):
    print(f"--- ESCANEO DE SEGURIDAD EN: {target_host} ---")
    print("Analizando puertos abiertos...\n")

    for port in port_list:
        # Creamos un objeto socket: AF_INET para IPv4, SOCK_STREAM para TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Definimos un tiempo de espera corto (1 segundo)
        sock.settimeout(1)
        
        # connect_ex devuelve 0 si la conexion fue exitosa (puerto abierto)
        result = sock.connect_ex((target_host, port))
        
        if result == 0:
            # Intentamos obtener el nombre del servicio comun para ese puerto
            try:
                service = socket.getservbyport(port)
            except:
                service = "Desconocido"
            
            print(f"[ ABIERTO ] Puerto {port}: {service}")
        
        sock.close()

# --- Configuracion del Escaneo ---
# 127.0.0.1 es tu propio dispositivo (localhost)
# Es la forma mas segura y legal de probar tu script
target = "127.0.0.1"
common_ports = [21, 22, 80, 443, 3306, 5432, 8080]

scan_ports(target, common_ports)

