import sys

if len(sys.argv) != 2:
    print("Uso: python word_count.py <archivo_txt>")
    sys.exit(1)

ruta_archivo = sys.argv[1]

try:
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        texto = file.read()
except FileNotFoundError:
    print(f"No se encontró el archivo: {ruta_archivo}")
    sys.exit(1)

# Contar caracteres distintos
caracteres_distintos = set(texto)

# Contar palabras distintas
palabras = texto.split()
palabras_distintas = set(palabras)

print(f"El número de caracteres distintos es: {len(caracteres_distintos)}")
print(f"El número de palabras distintas es: {len(palabras_distintas)}")