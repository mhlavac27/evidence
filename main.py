from evidence import Evidence

# vytvoření instance evidence pojištěných
evidence = Evidence()
evidence.zobraz_logo()
while True:
    print("\nVyberte akci:")
    print("1. Vytvořit pojištěného")
    print("2. Zobrazit seznam pojištěných")
    print("3. Hledat pojištěného")
    print("4. Konec")


    volba = input("Zadejte číslo akce: ")

    match volba:
        case "1":
            opakovani = evidence.pridej_pojistence()
            while opakovani == "A":
                opakovani = evidence.pridej_pojistence()
        case "2":
            evidence.zobraz_vsechny()
        case "3":
            evidence.najdi_zaznam()
        case "4":
            break
        case _:
            print("Neplatná volba. Zadejte znovu.")
