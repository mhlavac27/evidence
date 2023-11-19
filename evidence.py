from pojistenec import Pojistenec
class Evidence:
    # inicializace pole, pro vkládání záznamu
    def __init__(self):
        self.seznam_evidovanych = []

    # metody ověřují zda je vstup číslo
    def overeni_vek(self, vek):
        return vek.isnumeric()

    def overeni_tel_cisla(self, tel_cislo):
        return tel_cislo.isnumeric() and len(tel_cislo) == 9

    # metoda přidává nového pojištěnce
    def pridej_pojistence(self):
        jmeno = input("Zadej jméno: ")
        prijmeni = input("Zadej přijmení: ")
        vek = input("Zadej věk: ")
        tel_cislo = input("Zadej telefonní číslo /9číslic/: ")

        #cyklus zajišťuje správně zadané vstupy uživatele
        while not (jmeno and prijmeni and self.overeni_vek(vek) and self.overeni_tel_cisla(tel_cislo)):
            if jmeno == "":
                print("Jméno je povinný údaj!")
                jmeno = input("Zadej jméno: ")

            if prijmeni == "":
                print("Příjmení je povinný údaj!")
                prijmeni = input("Zadej přijmení: ")

            if self.overeni_vek(vek) != "True" or vek == "":
                print("Věk musí být číslo!")
                vek = input("Zadej věk: ")

            if self.overeni_tel_cisla(tel_cislo) != "True" or tel_cislo == "":
                print("Telefonní číslo musí obsahovat pouze 9 číslic!")
                tel_cislo = input("Zadej telefonní číslo /9číslic/: ")

        # vytvoření instance pojistence a nasledné uložení do listu
        pojistenec = Pojistenec(jmeno, prijmeni, vek, tel_cislo)
        self.seznam_evidovanych.append(pojistenec)
        print(f"Pojištěnec {pojistenec.cele_jmeno} byl vytvořen.")

        # interakce s uživatelem
        return input("Přidat dalšího? A/N: ").upper()

    # metoda pro výpis všech vytvořených instancí
    def zobraz_vsechny(self):
        if self.seznam_evidovanych == []:
            print("Nejsou evidovány žádné osoby.")
            return

        self.vypis_zahlavi()

        for radek in self.seznam_evidovanych:
            print(radek)


    #metoda k vyhledání záznamu podle jména
    def najdi_zaznam(self):
        if not self.seznam_evidovanych:
            print("Nejsou evidovány žádné osoby.")
            return

        jmeno = input("Zadej jméno, které chceš najít: ").lower()
        prijmeni = input("Zadej příjmení, které chceš najít: ").lower()

        # nacte vyhledany zaznam do listu, nasledně jej vypíše
        vysledek = []
        for pojistenec in self.seznam_evidovanych:
            if pojistenec.jmeno.lower() == jmeno or pojistenec.prijmeni.lower() == prijmeni:
                vysledek.append(pojistenec)

        if vysledek:
            self.vypis_zahlavi()
            for nalezeny_pojistenec in vysledek:
                print(nalezeny_pojistenec)
        else:
            print("Pojištěný nebyl nalezen.")



    # metoda pro výpis zahlaví seznamu
    def vypis_zahlavi(self):
        jmeno = "Jméno"
        vek = "Věk"
        tel_c = "Telefonní číslo"

        print(f"{jmeno:<20}{vek:<5}{tel_c}")

    #metoda pro uvítací logo
    def zobraz_logo(self):
        print("*******************************************")
        print("* VÍTEJTE V PROGRAMU EVIDENCE POJIŠTĚNÝCH *")
        print("*******************************************")
