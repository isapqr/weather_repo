import requests # Importiere das Requests-Modul für API-Anfragen

def holeWetterDaten(stadt): # Funktion, um Wetterdaten von einer API zu holen
    apiSchlüssel = '1fb87269c7a756df23755ec6a7824732' # Dein API-Schlüssel hier
    url = f'http://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={apiSchlüssel}&units=metric'
    antwort = requests.get(url)
    daten = antwort.json()
    return daten # Gibt JSON-Daten zurück

def gibKleidungsempfehlung(temperatur): # Funktion für Kleidungsempfehlung
    if temperatur > 25: # Wenn es warm ist
        return "Es ist heiß! Trage leichte Kleidung wie T-Shirts und Shorts."
    elif temperatur > 15: # Milder Bereich
        return "Es ist mild. Ein T-Shirt und eine leichte Jacke sollten reichen."
    elif temperatur > 5: # Etwas kühl
        return "Es ist kühl, eine Jacke und lange Hosen sind sinnvoll."
    else: # Wenn es kalt ist
        return "Es ist kalt! Trage einen Mantel, Schal und Mütze."

stadt = input("Gib eine Stadt ein: ") # Nutzer gibt eine Stadt ein
wetterDaten = holeWetterDaten(stadt)
temperatur = wetterDaten['main']['temp']
empfehlung = gibKleidungsempfehlung(temperatur)

print(f"Aktuelle Temperatur in {stadt}: {temperatur}°C") # Zeigt die Temperatur an
print(empfehlung) # Zeigt die Kleidungsempfehlung an