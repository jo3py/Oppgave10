#Antall pr. år: Tell antall sommerdager, høysommerdager og tropedager i det aktuelle året
#og skriv ut dette. En sommerdag er en dag med maksimaltemperatur over 20 grader. En
#høysommerdag har maksimaltemperatur over 25 grader og en tropedag har
#maksimaltemperatur over 30 grader.
def teller_sommedager(aarstall):
    import csv

    with open("GitHub/DAT120-vingsoppgave-7-Gruppeprosjekt-del-1/Gruppearbeid/csv_fila/sinnes_2014_2025_med_makstemperatur.csv",
            "r", encoding = "UTF-8") as fila:
        leser = csv.reader(fila , delimiter=";")
        next(leser)
        sommerdager = 0
        hoysommerdager = 0
        tropedager = 0
        for rad in leser:
            if aarstall in rad[2]:
                rad = float(rad[3].replace(",",".").replace("-","0"))
                if rad > 20:
                    sommerdager += 1
                elif rad > 25:
                    hoysommerdager += 1
                elif rad > 30:
                    tropedager += 1
        print(f"I år {aarstall}:\nTotalt: {sommerdager} sommerdager\nTotalt: {hoysommerdager} høysommerdager\nTotalt: {tropedager} tropedager")
