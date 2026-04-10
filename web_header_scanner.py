import requests

def audit_headers(url):
    # Aseguramos que la URL tenga el protocolo correcto
    if not url.startswith("http"):
        url = "https://" + url

    print(f"--- AUDITORIA DE CABECERAS DE SEGURIDAD: {url} ---")
    
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Lista de cabeceras de seguridad esenciales
        security_headers = {
            "Content-Security-Policy": "Previene ataques XSS e inyecciones de datos.",
            "Strict-Transport-Security": "Fuerza el uso de conexiones HTTPS seguras.",
            "X-Frame-Options": "Protege contra ataques de Clickjacking.",
            "X-Content-Type-Options": "Evita que el navegador adivine el tipo de contenido.",
            "Referrer-Policy": "Controla cuanta informacion de referencia se envia."
        }

        found_count = 0
        missing_count = 0

        for header, description in security_headers.items():
            if header in headers:
                print(f"[ OK ] {header} esta presente.")
                found_count += 1
            else:
                print(f"[ !! ] {header} NO detectada.")
                print(f"       Info: {description}")
                missing_count += 1
        
        print("\n--- RESUMEN DE LA AUDITORIA ---")
        print(f"Cabeceras configuradas: {found_count}")
        print(f"Cabeceras faltantes:    {missing_count}")

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servidor: {e}")

# --- Ejecucion ---
# Prueba con un sitio conocido o uno de prueba legal
target_url = input("Introduce la URL a analizar (ej. google.com): ")
audit_headers(target_url)
