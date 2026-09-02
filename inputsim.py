# Este es un comentario jaja
import getpass
import time
# este es otro comentarios
print("=== SIMULADOR DE CONEXIÓN CISCO IOS ===")

# 1. Solicitar los inputs al administrador (Funciona igual que en producción)
ip_router = input("Dirección IP del equipo Cisco (Ej. 192.168.1.1): ")
usuario = input("Usuario SSH: ")
contrasena = getpass.getpass("Contraseña SSH (Prueba con 'cisco123'): ")
comando = input("¿Qué comando deseas ejecutar? (Opciones: 'show ip int brief' o 'show version'): ")

# --- SIMULACIÓN DE CONEXIÓN ---
print(f"\n[...] Conectándose a {ip_router} vía SSH...")
time.sleep(1.5)  # Simula el retraso de red

# 2. Validación artificial de credenciales
if contrasena != "cisco123":
    print("\n[!] Error de conexión: Authentication failed (Password invalid).")
else:
    print("[+] Conexión establecida de forma segura.")
    print(f"[...] Enviando comando: '{comando}'\n")
    time.sleep(1)

    # 3. Base de datos artificial con respuestas típicas de Cisco IOS
    if comando.strip().lower() == "show ip int brief":
        print("--- RESULTADO DEL COMANDO (SIMULADO) ---")
        print("Interface              IP-Address      OK? Method Status                Protocol")
        print("GigabitEthernet0/0     192.168.1.1     YES manual up                    up      ")
        print("GigabitEthernet0/1     unassigned      YES unset  administratively down down    ")
        print("Loopback0              10.1.1.1        YES manual up                    up      ")
        
    elif comando.strip().lower() == "show version":
        print("--- RESULTADO DEL COMANDO (SIMULADO) ---")
        print("Cisco IOS Software, C1900 Software (C1900-UNIVERSALK9-M), Version 15.4(3)M3, RELEASE SOFTWARE (fc2)")
        print("Technical Support: http://cisco.com")
        print("System Uptime is 4 weeks, 2 days, 1 hour, 32 minutes")
        print("System image file is \"flash:c1900-universalk9-mz.SPA.154-3.M3.bin\"")
        
    else:
        print("--- RESULTADO DEL COMANDO (SIMULADO) ---")
        print(f"% Invalid input detected at '^' marker.")
        print(f"Router# {comando}")
        print("        ^")

print("\n=== FIN DE LA SIMULACIÓN ===")
