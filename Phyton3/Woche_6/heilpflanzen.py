class Heilpflanze:
    def __init__(self, name, wirkungen):
        self.name = name
        self.wirkungen = wirkungen

    def __gt__(self, other):
        return len(self.wirkungen) > len(other.wirkungen)
    
    def hat_wirkung(self, wirkung):
        return wirkung in self.wirkungen
    
if __name__ == "__main__":
    a = Heilpflanze("Arnika", ["wundheilend", "schmerzstillend"])
    b = Heilpflanze("Arnika", ["beruhigend"])
    print(a > b)
    print(a.hat_wirkung("schmerzstillend"))