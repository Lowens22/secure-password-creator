Generador de Contraseñas Seguras

Este programa en Python genera contraseñas seguras de manera aleatoria utilizando la biblioteca estándar secrets, que es más segura criptográficamente que random.

🚀 Características
✅ Genera contraseñas con:

Letras minúsculas

Opcional: letras mayúsculas

Opcional: dígitos

Opcional: símbolos

✅ Permite elegir la longitud de la contraseña.
✅ Interfaz simple por consola.
✅ Código corto, claro y fácil de modificar.

📦 Requisitos
Python 3.6+ (por el módulo secrets)

No necesita dependencias externas.

▶️ Uso

1.Clona o descarga este archivo:

```bash
    git clone <tu-repo>
    cd <tu-repo>
```

2.Ejecuta el programa:

```bash
    python secure_password.py
```
3.Sigue las instrucciones:

    🔐 Generador de Contraseñas Seguras
    👉 Longitud de la contraseña (ej. 16): 20
    ¿Incluir mayúsculas? (s/n): s
    ¿Incluir dígitos? (s/n): s
    ¿Incluir símbolos? (s/n): n

    ✅ Contraseña generada: fGhwLdjQpxvbnUtzmk48


🔒 ¿Por qué secrets?
El módulo secrets está diseñado para generar datos aleatorios seguros para contraseñas, tokens y claves criptográficas, a diferencia de random, que no es seguro para este propósito.

📜 Licencia
Este proyecto es de uso libre. Puedes modificarlo y adaptarlo según tus necesidades.