import collections

# Simulacion de lineas de un archivo de log (IP - Estado - Marca de tiempo)
# En un caso real, esto se leeria de un archivo .log o .txt
raw_logs = [
    "192.168.1.10 - FAILED - 10:00:01",
    "192.168.1.15 - SUCCESS - 10:00:05",
    "192.168.1.10 - FAILED - 10:00:10",
    "192.168.1.10 - FAILED - 10:00:15",
    "192.168.1.20 - FAILED - 10:00:20",
    "192.168.1.10 - FAILED - 10:00:25", # Cuarto intento fallido
    "192.168.1.15 - SUCCESS - 10:00:30"
]

def analyze_brute_force(logs, threshold=3):
    failed_attempts = collections.defaultdict(int)
    attackers = []

    for entry in logs:
        # Dividimos la linea para extraer la IP y el estado
        parts = entry.split(" - ")
        ip_address = parts[0]
        status = parts[1]

        if status == "FAILED":
            failed_attempts[ip_address] += 1
            
            # Si supera el limite definido, lo marcamos como sospechoso
            if failed_attempts[ip_address] >= threshold:
                if ip_address not in attackers:
                    attackers.append(ip_address)
    
    return attackers, failed_attempts

# --- Ejecucion ---
print("--- ANALIZADOR DE SEGURIDAD: DETECCION DE INTRUSOS ---")

limite_intentos = 3
sospechosos, reporte_total = analyze_brute_force(raw_logs, limite_intentos)

print("\nReporte de intentos fallidos por IP:")
for ip, count in reporte_total.items():
    print(f"IP: {ip} | Intentos: {count}")

print("\n--- ALERTAS DE SEGURIDAD ---")
if sospechosos:
    for ip in sospechosos:
        print(f"ALERTA: Posible ataque de fuerza bruta detectado desde: {ip}")
else:
    print("No se detectaron patrones de ataque.")

