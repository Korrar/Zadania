"Write Polish-English dictionary. User should be able to add words pairs (public void add(String pol, String eng)"

class PolEng:
    def __init__(self):
        self.N = 2
        self.dit = [0] * self.N


    def add(self, pol, eng):
        self.N = self.N + 2
        dit_new = [0] * (self.N + 2)
        i = 0
        for item in self.dit:
            dit_new[i] = self.dit[i]
            i = i + 1
        dit_new[self.N] = pol
        dit_new[self.N-1] = eng
        self.dit = dit_new


    def get(self, pol):
        i = 0
        for item in self.dit:
            if item == pol:
                print(self.dit[i-1])
            i = i + 1


pol = PolEng()

pol.add('ksiazka', 'book')
pol.add('samochod', 'car')
pol.get('ksiazka')
pol.get('samochod')

