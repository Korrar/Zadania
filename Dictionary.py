"Write Polish-English dictionary. User should be able to add words pairs (public void add(String pol, String eng)"




class PolEng:
    def __init__(self):
        self.N = 10
        self.dit = [None] * self.N

    def getindex(self, key):
        index = 0
        for char in str(key):
            index += ord(char)
        return index % self.N

    def add(self, pol, eng):
        index = self.getindex(pol)
        value = [pol, eng]

        if self.dit[index] is None:
            self.dit[index] = list([value])
            return True
        else:
            for tupl in self.dit[index]:
                if tupl[0] == pol:
                    tupl[1] = eng
                    return True
            self.dit[index] = value
            return True

    def get(self, pol):
        index = self.getindex(pol)

        if self.dit[index] is not None:
            for tupl in self.dit[index]:
                if tupl[0] == pol:
                    return tupl[1]
        return None


pol = PolEng()

pol.add('ksiazka', 'book')
pol.add('samochod', 'car')
print(pol.get('ksiazka'))
print(pol.get('samochod'))

