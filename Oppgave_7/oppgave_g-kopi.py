def null_nedbor():
    import csv
    with open("GitHub/DAT120-vingsoppgave-7-Gruppeprosjekt-del-1/Gruppearbeid/csv_fila/sinnes_2014_2025_med_makstemperatur.csv", "r", encoding="UTF-8") as fila:
        leser =csv.reader(fila, delimiter=";")

        next(leser) #Hopper over overskrift

        lengde_naa = 0
        start_naa = ""

        lengst = 0 
        start_lengst = ""
        slutt_lengst = ""
        feildata = 0

    
        for rad in leser:

            if(len(rad) < 6):
                continue

            dato = rad[2]

            try:
                nedbor = float(rad[5].replace(",", "."))
            except ValueError:
                feildata += 1
                continue


            if nedbor == 0:
                if lengde_naa ==0:
                    start_naa = dato

                lengde_naa += 1
                slutt_naa = dato
            else:
                if lengde_naa > lengst:
                    lengst = lengde_naa
                    start_lengst = start_naa
                    slutt_lengst = slutt_naa

                lengde_naa = 0

        if lengde_naa > lengst:
            lengst = lengde_naa
            start_lengst = start_naa
            slutt_lengst = slutt_naa
    print(f"Lengde av sammenhengende periode uten nedbør er: {lengst} dager")
    print(f"Startdato: {start_lengst}")
    print(f"Sluttdato: {slutt_lengst}")
    print(f"Rader hoppet over: {feildata}")
