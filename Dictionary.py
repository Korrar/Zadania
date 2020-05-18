"Write Polish-English dictionary. User should be able to add words pairs (public void add(String pol, String eng)"

class PolEng:
    def __init__(self):
        self.pol = []
        self.eng = []

    def add(self, pol, eng):
        self.pol = self.pol + [pol]# dodowanie na koneic tablicy
        self.eng = self.eng + [eng]

    def get(self, pol):
        i = 0
        for item in self.pol:
            if item == pol:
                print(self.eng[i])
            i = i + 1


pol = PolEng()

pol.add('ksiazka', 'book')
pol.add('samochod', 'car')
pol.get('ksiazka')
pol.get('samochod')

