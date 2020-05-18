"Write Polish-English dictionary. User should be able to add words pairs (public void add(String pol, String eng)"


class PolEng:
    def __init__(self):
        self.N = 1
        self.pol = [0] * self.N
        self.eng = [0] * self.N

    def add(self, pol, eng):
        self.N = self.N + 1
        eng_new = [0] * (self.N + 1)
        pol_new = [0] * (self.N + 1)
        i = 0
        for item in self.pol:
            pol_new[i] = self.pol[i]
            eng_new[i] = self.eng[i]
            i = i +1
        pol_new[self.N] = pol
        eng_new[self.N] = eng
        self.pol = pol_new
        self.eng = eng_new


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

