
import csv
from pathlib import Path
import matplotlib.pyplot as plt
def funksjon_c():
    mappe = Path(__file__).resolve().parent

    filer = {
        "Oslo Blindern": "oslo_blindern_1954_2025_med_makstemperatur.csv",
        "Roeros": "roeros_1954_2025_med_makstemperatur.csv",
        "Tromsoe": "tromsoe_1954_2025_med_makstemperatur.csv",
        "Vaernes": "vaernes_1954_2025_med_makstemperatur.csv",
        "Venabu": "venabu_1954_2025_med_makstemperatur.csv"
    }

    def les_stasjon(filnavn):
        temperatur_per_aar = {}

        with open(mappe / filnavn, "r", encoding="utf-8") as fil:
            leser = csv.DictReader(fil, delimiter=";")

            for rad in leser:
                try:
                    dato = rad["Tid(norsk normaltid)"]
                    temperatur = rad["Middeltemperatur (døgn)"]

                    if temperatur == "":
                        continue

                    temperatur = float(temperatur.replace(",", "."))

                    aar = int(dato.split(".")[2])

                    if aar not in temperatur_per_aar:
                        temperatur_per_aar[aar] = []

                    temperatur_per_aar[aar].append(temperatur)

                except:
                    pass

        aar_liste = []
        gjennomsnitt_liste = []

        for aar in sorted(temperatur_per_aar):

            temperaturer = temperatur_per_aar[aar]

            if len(temperaturer) >= 300:
                gjennomsnitt = sum(temperaturer) / len(temperaturer)

                aar_liste.append(aar)
                gjennomsnitt_liste.append(gjennomsnitt)

        return aar_liste, gjennomsnitt_liste



    for navn, filnavn in filer.items():
        aar, temperaturer = les_stasjon(filnavn)
        plt.plot(aar, temperaturer, label=navn)

    plt.title("Gjennomsnittstemperatur per år")
    plt.xlabel("År")
    plt.ylabel("Temperatur (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()

