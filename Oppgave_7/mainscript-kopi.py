from oppgave_d import plotting_av_data
from oppgave_e import teller_skidager
from oppgave_f import forenklet_plantevekst
from oppgave_g import null_nedbor
from oppgave_h import teller_sommedager


startverdi = True
while startverdi:
    try:
        aarstall = input("Skriv inn aarstall (yyyy): ")
        intervall = int(aarstall)
        if intervall >= 2014 and intervall <= 2025:
            startverdi = False
        else:
            print("Årstallet må være i mellom 2014 og 2025")
            startverdi = True
    except ValueError:
        print("Ugyldig input. Skriv inn et årstall.")
        startverdi = True



plotting_av_data(aarstall)
print()
teller_skidager(aarstall)
print()
forenklet_plantevekst(aarstall)
print()
null_nedbor()
print()
teller_sommedager(aarstall)
print()
