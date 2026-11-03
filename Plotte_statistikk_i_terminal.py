import csv
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
    

    for i in range(1,13):
        liste_vind= lag_liste(f"{i:02}")   
        midten = len(liste_vind)
        if midten % 2 == 1:
            median = liste_vind[midten // 2]
        else:
            median = (float(liste_vind[midten //2 - 1])+ float(liste_vind[midten // 2])) / 2
        print("max vind i", i,max(liste_vind))
        print("min vind i", i,min(liste_vind))
        print("median vind i", i,median)
        
    