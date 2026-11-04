
import csv
import matplotlib.pyplot as plt

def oppgave_c():

    vaerstasjoner = {
        "oslo": "GitHub/Oppgave10/flere_vaerstasjoner_med_makstemperatur/oslo_blindern_1954_2025_med_makstemperatur.csv",
        "roeros": "GitHub/Oppgave10/flere_vaerstasjoner_med_makstemperatur/roeros_1954_2025_med_makstemperatur.csv",
        "tromsoe": "GitHub/Oppgave10/flere_vaerstasjoner_med_makstemperatur/tromsoe_1954_2025_med_makstemperatur.csv",
        "vaernes": "GitHub/Oppgave10/flere_vaerstasjoner_med_makstemperatur/vaernes_1954_2025_med_makstemperatur.csv",
        "venabu": "GitHub/Oppgave10/flere_vaerstasjoner_med_makstemperatur/venabu_1954_2025_med_makstemperatur.csv"
    }

    temperatur_per_aar = {}

    for stasjon, filnavn in vaerstasjoner.items():

        temperatur_per_aar[stasjon] = {}

        with open(filnavn, "r", encoding="UTF-8") as fil:
            leser = csv.reader(fil, delimiter=";")
            next(leser)

            for rad in leser:
                try:
                    middel_temp = float(rad[3].replace(",", "."))
                    dato = rad[2]
                    aar = dato.split(".")[2]

                    if aar not in temperatur_per_aar[stasjon]:
                        temperatur_per_aar[stasjon][aar] = []

                    temperatur_per_aar[stasjon][aar].append(middel_temp)

                except (ValueError, IndexError):
                    continue

    plt.figure(figsize=(15, 6))

    for stasjon in temperatur_per_aar:

        aar_liste = sorted(temperatur_per_aar[stasjon].keys())
        gjennomsnitt_liste = []

        for aar in aar_liste:

            temperaturer = temperatur_per_aar[stasjon][aar]

            if len(temperaturer) >= 300:
                gjennomsnitt = sum(temperaturer) / len(temperaturer)
                gjennomsnitt_liste.append(gjennomsnitt)
            else:
                gjennomsnitt_liste.append(None)

        plt.plot(aar_liste, gjennomsnitt_liste, label=stasjon)

    plt.xlabel("Årstall")
    plt.xticks(rotation=45)
    plt.ylabel("Gjennomsnittstemperatur (°C)")
    plt.title("Gjennomsnittstemperatur per år")
    plt.legend()
    plt.grid()
    plt.show()