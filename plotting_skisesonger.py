

def plotting_skisesonger():
    import os
    import matplotlib.pyplot as plt

    mappe = os.path.join(os.path.dirname(__file__), "flere_vaerstasjoner_med_makstemperatur")

    filer = ["oslo_blindern_1954_2025_med_makstemperatur.csv", 
             "roeros_1954_2025_med_makstemperatur.csv", 
             "tromsoe_1954_2025_med_makstemperatur.csv", 
             "vaernes_1954_2025_med_makstemperatur.csv",
             "venabu_1954_2025_med_makstemperatur.csv"]
    
    resultater = {}

    for filnavn in filer:
        
        try:
            with open(os.path.join(mappe, filnavn), "r", encoding="UTF-8") as fil:

                sesonger = {}

                for i, linje in enumerate(fil):

                    if i == 0:
                        continue

                    rad = linje.strip().split(";")

                    dato = rad[2]

                    if dato == "" or dato == "-":
                        continue

                    dag = int(dato[0:2])
                    maaned = int(dato[3:5])
                    aar = int(dato[6:10])

                    if maaned >=11:
                        sesongaar = aar + 1
                    elif maaned <= 5:
                        sesongaar = aar
                    else:
                        continue

                    snodybde = rad[7]

                    if snodybde == "" or snodybde == "-":
                        continue

                    snodybde = float(snodybde.replace(",", "."))

                    if sesongaar not in sesonger:
                        sesonger[sesongaar] = [0, 0]

                    sesonger[sesongaar][0] += 1

                    if snodybde >= 20:
                        sesonger[sesongaar][1] += 1
                resultater[filnavn] = sesonger
        
        except FileNotFoundError:
            print("Fant ikke filen")


    for filnavn, sesonger in resultater.items():
        aarstall = []
        skidager = []

        for aar in sorted(sesonger):
            verdier = sesonger[aar]

            maalinger = verdier[0]
            antall_skidager = verdier[1]

            if maalinger >= 106:
                aarstall.append(aar)
                skidager.append(antall_skidager)

        plt.plot(aarstall, skidager,
                 label=filnavn.replace("_1954_2025_med_makstemperatur.csv", ""))
        
    plt.xlabel("Skisesong")
    plt.ylabel("Antall_skidager")
    plt.title("Antall skidager per skisesong")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


plotting_skisesonger()

        


