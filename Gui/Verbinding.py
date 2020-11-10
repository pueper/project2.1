# import serial


# ser = serial.Serial('COM3', 19200)

# Elke keer als er een temperatuur/lichtintensiteit binnekomt, dan een element toevoegen die 60 (seconden) hoger is dan het vorige element
tijd = []

temperatuur = []
lichtintensiteit = []


# while True:

# In de while loop kan de gelezen waarde toegevoegd worden aan deze arrays

# In de while loop kan je ook deze gemiddelde berekeningen zetten (dan wordt deze constant bijgewerkt)


if (len(tijd) > 10 | len(temperatuur) > 10 | len(lichtintensiteit) > 10):
    tijd.pop(0)
    temperatuur.pop(0)
    lichtintensiteit.pop(0)

# HIER DE gelezen data in de lijsten stoppen


gemiddelde_lichtintensiteit = str(
    sum(lichtintensiteit) / len(lichtintensiteit))
gemiddelde_temperatuur = str((sum(temperatuur) / len(temperatuur)))
