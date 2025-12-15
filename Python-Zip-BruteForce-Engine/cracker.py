import zipfile
import time
import sys
from termcolor import colored  

# --- CONFIGURACIÓN ---
zip_file = "archivo_seguro.zip"
wordlist = "diccionario.txt"

def print_banner():
    print(colored("""
    ========================================
     🔓 ZIP-LOCK BRUTE FORCE ENGINE v1.0
     Target: {}
    ========================================
    """, 'cyan').format(zip_file))

def crack_password(zip_filename, password_list):
    # Abrimos el archivo zip
    zip_obj = zipfile.ZipFile(zip_filename)
    
    
    n_words = len(list(open(password_list, "rb")))
    print(colored(f"[+] Diccionario cargado: {n_words} payloads.", 'yellow'))
    print(colored("[*] Iniciando ataque de fuerza bruta...", 'blue'))
    time.sleep(1) # Pausa dramática

    with open(password_list, "rb") as f:
        for line in f:
            for word in line.split():
                try:
                    
                    zip_obj.extractall(pwd=word)
                    
                    
                    print(colored("\n[!!!] CONTRASEÑA ENCONTRADA: ", 'green') + colored(word.decode(), 'white', attrs=['bold', 'blink']))
                    return True
                except:
                    
                    # print(f"[-] Fallo: {word.decode()}") 
                    continue
    
    print(colored("\n[X] Ataque fallido. Contraseña no encontrada.", 'red'))
    return False

# --- EJECUCIÓN ---
if __name__ == "__main__":
    try:
        print_banner()
        crack_password(zip_file, wordlist)
    except Exception as e:
        print(e)