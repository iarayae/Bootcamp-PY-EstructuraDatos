recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Agregar evento del 02 de Febrero
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

# Corregir fecha del evento del 15/07 al 16/07
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# Eliminar el evento del 01/05 (día del trabajo)
recordatorios = [evento for evento in recordatorios if not (evento[0] == '2021-05-01' and evento[2] == 'No trabajar')]

# Agregar cena de navidad (24/12) y cena de año nuevo (31/12) a las 22:00
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Ordenar cronologicamente
recordatorios.sort()

for evento in recordatorios:
    print(evento)