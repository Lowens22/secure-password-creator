import secrets
import string

def generar_contraseña(longitud=16, usar_mayusculas=True, usar_digitos=True, usar_simbolos=True):
    caracteres = string.ascii_lowercase

    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("No hay caracteres disponibles para generar la contraseña.")

    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

# --- Interfaz simple por consola ---
if __name__ == "__main__":
    print("🔐 Generador de Contraseñas Seguras")
    try:
        longitud = int(input("👉 Longitud de la contraseña (ej. 16): "))
        usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        usar_digitos = input("¿Incluir dígitos? (s/n): ").lower() == 's'
        usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

        contraseña_segura = generar_contraseña(longitud, usar_mayusculas, usar_digitos, usar_simbolos)
        print(f"\n✅ Contraseña generada: {contraseña_segura}")
    except ValueError:
        print("❌ Entrada inválida.")
