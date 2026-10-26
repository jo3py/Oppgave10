# Skiføre: Hvis vi antar at det er skiføre så lenge snødybden er minst 20cm,
# la brukeren skrive inn et årstall og regn ut for et oppgitt år hvor mange dager 
# det var skiføre den skisesongen.
# En skisesong strekker seg fra november forrige år til mai dette året.

def teller_skidager(aarstall):
    aarstall = int(aarstall)

    if aarstall < 2015 or aarstall > 2025:
        print(f"Utilstrekkelig informasjon til å beregne skidager for skisesongen år {aarstall}")
        return

    antall_skidager = 0

    try:
        fil = open("GitHub/DAT120-vingsoppgave-7-Gruppeprosjekt-del-1/Gruppearbeid/csv_fila/sinnes_2014_2025_med_makstemperatur.csv", "r"
                   , encoding="UTF-8")

        for i, linje in enumerate(fil):
            if i == 0:
                continue

            rad = linje.strip().split(";")
        
            if rad[7] == "-":
                continue
        
            dato = rad[2]
        
            if dato == "":
                continue

            måned = int(dato[3:5])
            år = int(dato[6:10])
        
            snodybde = float(rad[7].replace(",", "."))


            if ((måned >= 11 and år == aarstall - 1) or 
                (måned <= 5 and år == aarstall)):

                if snodybde >= 20:
                    antall_skidager += 1
    
        print(f"Skisesongen {aarstall-1}-{aarstall}: {antall_skidager} skidager")


    except FileNotFoundError:
        print("Fant ikke filen")

