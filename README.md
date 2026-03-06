# 🔓 ZIP-Lock Brute Force 

![Kali Linux](https://img.shields.io/badge/OS-Kali_Linux-blue) ![Python](https://img.shields.io/badge/Code-Python_3-yellow) ![Security](https://img.shields.io/badge/Type-Pentesting_Tool-red)

> **⚠️** Herramienta desarrollada estrictamente con **FIN EDUCATIVO** .
---

### 📋 Descripción 
Motor de ataque por **fuerza bruta (diccionario)** desarrollado en Python. Diseñado para verificar la robustez de contraseñas en archivos comprimidos `.zip` cifrados.
El script automatiza la inyección de *payloads* desde diccionarios estándar (como `rockyou.txt`) para verificar la seguridad del cifrado.

### 🚀 Funcionalidades
* **Carga Optimizada:** Capaz de procesar diccionarios masivos sin saturar la memoria.
* **Interfaz Visual (CLI):** Feedback en tiempo real con código para identificar éxitos/fallos.
* **Gestión de Errores:** Control de excepciones para evitar paradas en archivos corruptos o bloqueados.

### 📸 PoC
![cracker_py](https://github.com/user-attachments/assets/8d17e3ae-72b0-407b-901d-d778c4547a26)


### 🛠️ Instrucciones de Uso
Ejecutar en entorno Linux/Kali:

```bash
python3 cracker.py
