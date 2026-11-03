import csv
import matplotlib.pyplot as plot

with open(r"C:\Users\vareb\OneDrive\A UIS BACHELOR\Koder DAT-120\Oppgave10\flere_vaerstasjoner_med_makstemperatur\oslo_blindern_1954_2025_med_makstemperatur.csv","r",encoding = "UTF-8") as fila:

    
    def lag_liste(måned_gitt):
        fila.seek(0)
        linje= csv.DictReader(fila, delimiter=";")
        liste_vind = []
        for rad in linje:
            try:
                måned = rad["Tid(norsk normaltid)"].split(".")[1]
                vind = float(rad["Høyeste middelvind (døgn)"].replace(",","."))
                if måned == str(måned_gitt):
                        liste_vind.append(vind)
                
            except:
                continue
            
        return sorted(liste_vind)
    
    måneder = []
    maks_liste = []
    min_liste = []
    median_liste = []

    for i in range(1,13):
        liste_vind= lag_liste(f"{i:02}")   
        midten = len(liste_vind)
        if midten % 2 == 1:
            median = liste_vind[midten // 2]
        else:
            median = (float(liste_vind[midten //2 - 1])+ float(liste_vind[midten // 2])) / 2
        måneder.append(i)
        maks_liste.append(max(liste_vind))
        min_liste.append(min(liste_vind))
        median_liste.append(median)

    plot.plot(måneder, maks_liste, label="Maks")
    plot.plot(måneder, min_liste, label="Min")
    plot.plot(måneder, median_liste, label="Median")

    plot.xlabel("Måned")
    plot.ylabel("Vind")
    plot.title("Vindstatistikk per måned")
    plot.grid()
    plot.show()