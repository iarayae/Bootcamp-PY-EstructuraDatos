import sys

if len(sys.argv) != 5:
    print("Uso: python conversiones.py <sol> <peso_arg> <usd> <monto>")
    sys.exit(1)

sol = float(sys.argv[1])
peso_arg = float(sys.argv[2])
usd = float(sys.argv[3])
monto = int(sys.argv[4])

print(f"Los {monto} pesos equivalen a:\n")
print(f"{monto * sol} Soles")
print(f"{monto * peso_arg} Pesos Argentinos")
print(f"{monto * usd} Dólares")