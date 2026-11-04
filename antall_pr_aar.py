import csv
import matplotlib.pyplot as plt

#oslo_vaer = "oslo_blindern_1954_2025_med_makstemperatur.csv"
#roeros_vaer = "roeros_1954_2025_med_makstemperatur.csv"
#tromsoe_vaer = "tromsoe_1954_2025_med_makstemperatur.csv"
#vaernes_vaer = "vaernes_1954_2025_med_makstemperatur.csv"
#venabu_vaer = "venabu_1954_2025_med_makstemperatur.csv"

vaerstasjoner = {
    "oslo": "flere_vaerstasjoner_med_makstemperatur/oslo_blindern_1954_2025_med_makstemperatur.csv",
    "roeros": "flere_vaerstasjoner_med_makstemperatur/roeros_1954_2025_med_makstemperatur.csv",
    "tromsoe": "flere_vaerstasjoner_med_makstemperatur/tromsoe_1954_2025_med_makstemperatur.csv",
    "vaernes": "flere_vaerstasjoner_med_makstemperatur/vaernes_1954_2025_med_makstemperatur.csv",
    "venabu": "flere_vaerstasjoner_med_makstemperatur/venabu_1954_2025_med_makstemperatur.csv"
}
vanligdag = 0
sommerdag = 0
hoy_sommerdag = 0
tropedag = 0

total_sommerdager = {}
    
#filer = [oslo_vaer, roeros_vaer, tromsoe_vaer, vaernes_vaer, venabu_vaer]

for stasjon, filnavn in vaerstasjoner.items():
    total_sommerdager[stasjon] = {} #stasjonen lagres inn i ett nested dictionary med årstall som key og antall sommerdager som value

    with open(filnavn, "r", encoding="UTF-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)

        for rad in leser:
            try:
                maks_temp = float(rad[3].replace(",", "."))
                dato = rad[2]
                aar = dato.split(".")[2] #[2] for å hente ut årstallet fra datoen

                if aar not in total_sommerdager[stasjon]:
                    total_sommerdager[stasjon][aar] = {"Sommerdag": 0, "Høy sommerdag": 0, "Tropedag": 0}
            except ValueError:
                continue

            if maks_temp > 30:
                tropedag += 1
                total_sommerdager[stasjon][aar]["Tropedag"] += 1
            elif maks_temp > 25:
                hoy_sommerdag += 1
                total_sommerdager[stasjon][aar]["Høy sommerdag"] += 1
            elif maks_temp > 20:
                sommerdag += 1
                total_sommerdager[stasjon][aar]["Sommerdag"] += 1
            else:
                vanligdag += 1

#for aar, data in total_sommerdager["oslo"].items():
    #print(aar, data)

plt.figure(figsize=(15, 6))

for stasjon in total_sommerdager:

    aar_liste = sorted(total_sommerdager[stasjon].keys())
    sommerdager_liste = []

    for aar in aar_liste:
        sommerdager_liste.append(total_sommerdager[stasjon][aar]["Sommerdag"])

    plt.plot(aar_liste, sommerdager_liste, label=stasjon)

#plt.axhline(y=20, color="green", linestyle="--", label="20 Sommerdag")
#plt.axhline(y=25, color="orange", linestyle="--", label="25 Høy Sommerdag")
#plt.axhline(y=30, color="red", linestyle="--", label="30 Tropedag")


plt.xlabel("Årstall")
plt.xticks(rotation=45)
plt.ylabel("Antall sommerdager")
plt.title("Sommerdager per år")
plt.legend()
plt.grid()
plt.show()