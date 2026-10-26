#   Plotting: Dere skal la brukeren skrive inn et årstall og så skal programmet plotte
#   snødybde, nedbør, middeltemperatur og høyeste middelvind hver dag for dette året.
#   Hint: Konverter datoene fra strenger til datetime objekter for å få en finere visning av
#   datoene
def plotting_av_data(aarstall):
    import csv
    import matplotlib.pyplot as plt
    from datetime import datetime

    snodybde = []
    nedbor = []
    middeltemperatur = []
    hoyeste_middelvind = []
    dato = []
    snodybde_dato = []
    akkumulator = 0

    with open("GitHub/DAT120-vingsoppgave-7-Gruppeprosjekt-del-1/Gruppearbeid/csv_fila/sinnes_2014_2025.csv",
            "r", encoding = "UTF-8") as fila:
        leser = csv.reader(fila , delimiter=";")
        next(leser)
        for rad in leser:
            if aarstall in rad[2]:
                try:
                    snodata = float(rad[6])
                    snodybde.append(snodata)
                    akkumulator += 1
                except ValueError:
                    if "-" in rad[6]:
                        try:
                            if snodybde[(akkumulator)-1] >= 0:
                                snodybde.append(snodybde[akkumulator-1])
                                akkumulator += 1
                        except:
                            snodybde1 = rad[6].replace("-","0")
                            snodybde.append(float(snodybde1))
                            akkumulator += 1
                finally:
                        nedbor1 = rad[4].replace(",",".")
                        nedbor.append(float(nedbor1))

                        middeltemperatur1 = rad[3].replace(",",".").replace("-","0")
                        middeltemperatur.append(float(middeltemperatur1))

                        middelvind1 = rad[5].replace(",",".").replace("-","0")
                        hoyeste_middelvind.append(float(middelvind1))
                        dato.append(datetime.strptime(rad[2], "%d.%m.%Y"))

        plt.subplot (2, 2, 1, label=aarstall)
        plt.legend(aarstall)
        plt.bar(dato, snodybde, label="Snødybde i " + aarstall)
        plt.ylabel("cm")
        plt.ylim(min(snodybde), max(snodybde))
        plt.legend()

        plt.subplot (2, 2, 2)
        plt.bar(dato, nedbor, label = "Nedbør i " + aarstall)
        plt.ylabel("mm")
        plt.legend()

        plt.subplot (2, 2, 3)
        plt.bar(dato, middeltemperatur, label = "Middeltemperatur i " + aarstall)
        plt.ylabel("grader Celsius")
        plt.legend()

        plt.subplot (2, 2, 4)
        plt.bar(dato, hoyeste_middelvind, label = "Høyeste_middelvind i " + aarstall)
        plt.ylabel("m/s")
        plt.legend()
        plt.show()

