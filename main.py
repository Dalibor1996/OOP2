class Kniha:
    def __init__(self, nazov, autor, ISBN, rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupna = True
        self.rok_vydania = rok_vydania

    def vypozicat(self):
        self.dostupna = False
class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def pozicaj_knihu(self, ISBN_knihy):
        for kniha in self.zoznam_knih:
            if









kniha1 = Kniha("Harry Potter", "Rowlingova", 123, 2010)
kniha2 = Kniha("Pan prstenov", "Tolkien", 321, 2003)
kniha3 = Kniha("Nejaka", "Dalibor", 222, 2010)

print(kniha.price)
kniha.price = 20
print(kniha.price)
