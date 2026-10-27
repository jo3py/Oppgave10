#   Dere skal plotte de samme dataene som i
#   øvingsoppgave 7 deloppgave d for hele tidsserien, men for hver måned heller enn
#   for hver dag. Dere skal regne maks snødybde, total nedbør, maks og min
#   middeltemperatur og maks middelvind for hver måned. For nedbør kan dere
#   regne alle måneder med fler enn 20 gyldige måli

import csv
import matplotlib.pyplot as plt
from datetime import datetime

snodybde_month = list()
nedbor_month = []
middeltemperatur_month_maks = []
middeltemperatur_month_min = []
hoyeste_middelvind_month_maks = []
dato = []
normal_dato = []

akkumulator = 0

with open("GitHub/Oppgave10/Oppgave_7/csv_fila/sinnes_2014_2025.csv",
        "r", encoding = "UTF-8") as fila:
    leser = csv.reader(fila , delimiter=";")
    next(leser)
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    for month in range(0, 12):
        snodybde = []
        nedbor = []
        middeltemperatur = []
        hoyeste_middelvind = []

        nedbor_akkumulator = 0
        akkumulator_months = 0
        month_controller = []
        for rad in leser:
            try:
                akkumulator_months += 1
                dato_rad = (rad[2].split("."))
                month = dato_rad[1]
                month_controller.append(month)
                if month == month_controller[akkumulator_months-2] or len(month_controller) == 1:
                        try:
                            snodata = float(rad[6])
                            snodybde.append(snodata)
                            akkumulator += 1
                        except ValueError:
                            if "-" in rad[6]:
                                try:
                                    if snodybde[(akkumulator)-1] >= 0:
                                        snodybde.append(float(snodybde[akkumulator-1]))
                                        akkumulator += 1
                                except:
                                    snodybde1 = rad[6].replace("-","0")
                                    snodybde.append(float(snodybde1))
                                    akkumulator += 1
                        finally:
                                nedbor1 = float(rad[4].replace(",",".").replace("-","0"))
                                if nedbor1 <= 0:
                                    nedbor_akkumulator += 0
                                    nedbor.append(nedbor1)
                                elif nedbor1 > 0:
                                    nedbor_akkumulator += 1
                                    nedbor.append(nedbor1)

                                middeltemperatur1 = rad[3].replace(",",".").replace("-","0")
                                middeltemperatur.append(float(middeltemperatur1))

                                middelvind1 = rad[5].replace(",",".").replace("-","0")
                                hoyeste_middelvind.append(float(middelvind1))
                                dato.append(datetime.strptime(rad[2], "%d.%m.%Y"))
                                normal_dato.append((rad[2]).split("."))
                else:
                    try:
                        if nedbor_akkumulator > 20:
                            nedbor_month.append(max(nedbor))
                        
                        if snodybde == []:
                            pass
                        else:
                            snodybde_month.append(max(snodybde))

                        if middeltemperatur == []:
                            pass
                        else:
                            middeltemperatur_month_maks.append(max(middeltemperatur))
                            middeltemperatur_month_min.append(min(middeltemperatur))
            
                        if hoyeste_middelvind == []:
                            pass
                        else:
                            hoyeste_middelvind_month_maks.append(max(hoyeste_middelvind))
                    except ValueError or IndexError:
                        print("Dette er Value eller Index Error!")
                    finally:
                        snodybde = []
                        nedbor = []
                        middeltemperatur = []
                        hoyeste_middelvind = []
                
                        nedbor_akkumulator = 0
                        akkumulator_months = 0
                        month_controller = []
            except IndexError:
                pass
print()
print("Liste for maks snødybde for hver måned i tidsserien")
print(snodybde_month)
print("---")
print("Liste for maks nedbor for hver måned i tidsserien")
print(nedbor_month)
print("---")
print("Liste for maks middeltemperatur for hver måned i tidsserien")
print(middeltemperatur_month_maks)
print("---")
print("Liste for minimum middeltemperatur for hver måned i tidsserien")
print(middeltemperatur_month_min)
print("---")
print("Liste for maks middelvind for hver måned i tidsserien")
print(hoyeste_middelvind_month_maks)
print("---")
print(len(snodybde_month))
print(len(nedbor_month))
print(len(middeltemperatur_month_maks))
print(len(middeltemperatur_month_min))
print(len(hoyeste_middelvind_month_maks))
print()