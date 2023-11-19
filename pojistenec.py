class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo
        self.cele_jmeno = self.jmeno+" "+self.prijmeni

    def __str__(self):
        zaznam = f"{self.cele_jmeno:<20}{self.vek:<5}{self.tel_cislo}"
        return zaznam

