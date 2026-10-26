# Ifølge oppgaven gir minusgrader negativ vekst lik antall minusgrader.
# Derfor kan temperaturen legges direkte til planteveksten.

def beregn_plantevekst():
    from pathlib import Path

    import pandas as pd
    import matplotlib.pyplot as plt

    # Bruk mappen der dette skriptet ligger, uansett hvorfra det kjøres.
    mappe = Path(__file__).resolve().parent

    # Leser inn temperaturdata
    # CSV-filen bruker semikolon som skilletegn og komma som desimaltegn.
    data = pd.read_csv(
        mappe / "temperatur.csv",
        sep=";",
        decimal=",",
        encoding="utf-8-sig",
        na_values=["-"],
    )

    # Renamer kolonner slik at resten av koden fungerer
    # Tid(norsk normaltid) blir Dato
    # Middeltemperatur (døgn) blir Middeltemperatur
    data = data.rename(
        columns={
            "Tid(norsk normaltid)": "Dato",
            "Middeltemperatur (døgn)": "Middeltemperatur",
        }
    )

    # Gjør om dato til datoformat
    # dayfirst=True sørger for at datoer som 01.01.2014 leses riktig
    # Jeg dropper eventuelle rader uten gyldig dato eller temperatur for å unngå feil i beregningen.
    data["Dato"] = pd.to_datetime(data["Dato"], dayfirst=True)
    data["Middeltemperatur"] = pd.to_numeric(
        data["Middeltemperatur"],
        errors="coerce",
    )
    data = data.dropna(subset=["Dato", "Middeltemperatur"]).reset_index(drop=True)

    # Jeg tester bare startdatoer fram til 1. april i csv filen, da veksten etter dette ikke er relevant for oppgaven.
    sluttdato = pd.Timestamp("2024-04-01")

    # Summer fra hver dato til slutten av datasettet uten langsomme, nøstede løkker.
    data["TotalPlantevekst"] = (
        data["Middeltemperatur"].iloc[::-1].cumsum().iloc[::-1]
    )
    resultater_df = data.loc[
        data["Dato"] <= sluttdato,
        ["Dato", "TotalPlantevekst"],
    ].rename(columns={"Dato": "Startdato"})

    # Finne maksimal vekst
    maks_vekst = resultater_df["TotalPlantevekst"].max()

    # Finne datoen som ga størst vekst
    beste_dato = resultater_df.loc[
        resultater_df["TotalPlantevekst"].idxmax(),
        "Startdato"
    ]

    print("Beste startdato:", beste_dato.date())
    print("Maksimal plantevekst:", round(maks_vekst, 2))

    plt.figure(figsize=(12, 6))
    plt.plot(
        resultater_df["Startdato"],
        resultater_df["TotalPlantevekst"]
    )

    plt.title("Plantevekst for ulike startdatoer")
    plt.xlabel("Startdato")
    plt.ylabel("Total plantevekst")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    beregn_plantevekst()