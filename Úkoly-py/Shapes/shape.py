

from math import pi

class Ctverec():
    def __init__(self, a:int):
        self.a = a
    def obsah(self):
        return self.a**2
    def obvod(self):
        return self.a *4
    def write(self):
        print("Obsah čtverce: "+ str(self.obsah()))
        print("Obvod čtverce: "+ str(self.obvod()))

class Obdelnik(Ctverec):
    def __init__(self, a:int, b:int):
        super().__init__(a)
        self.b = b
    def obsah(self):
        return self.a*self.b
    def obvod(self):
        return 2*(self.a + self.b)
    def write(self):
        print("Obsah obdelníka: "+ str(self.obsah()))
        print("Obvod obdelníka: "+ str(self.obvod()))

class Krychle(Ctverec):
    def __init__(self, a:int):
        super().__init__(a)
    def obsah(self):
        return (self.a**2)*6
    def obvod(self):
        return self.a*12
    def objem(self):
        return self.a**3
    def write(self):
        print("Obsah krychle: "+ str(self.obsah()))
        print("Obvod krychle: "+ str(self.obvod()))
        print("Objem krychle: "+ str(self.objem()))

class Kvadr(Obdelnik):
    def __init__(self, a:int, b:int, c:int):
        super().__init__(a,b)
        self.c = c
    def obsah(self):
        return 2*(self.a*self.b+self.a*self.c+self.b*self.c)
    def obvod(self):
        return 4*(self.a+self.b+self.c)
    def objem(self):
        return self.a*self.b*self.c
    def write(self):
        print("Obsah kvádru: "+ str(self.obsah()))
        print("Obvod kvádru: "+ str(self.obvod()))
        print("Objem kvádru: "+ str(self.objem()))

class Kruh():
    def __init__(self, r:int):
        self.r = r
    def obsah(self):
        return 2*(pi**2)
    def obvod(self):
        return 2*pi*self.r
    def write(self):
        print("Obsah kruhu: "+ str(self.obsah()))
        print("Obvod kruhu: "+ str(self.obvod()))
class Valec(Kruh):
    def __init__(self, r:int, v:int):
        super().__init__(r)
        self.v = v
    def obsah(self):
        return (2*pi*self.r*self.v) + (2*pi*(self.r**2))
    def objem(self):
        return pi*(self.r**2)*self.v
    def write(self):
        print("Obsah kvadru: "+ str(self.obsah()))
        print("Objem kvadru: "+ str(self.objem()))

class Koule(Kruh):
    def __init__(self, r:int):
        super().__init__(r)
    def obsah(self):
        return 4*pi*(self.r**2)
    def objem(self):
        return (4/3)*pi*(self.r**2)
    def write(self):
        print("Obsah koule: "+ str(self.obsah()))
        print("Objem koule: "+ str(self.objem()))

ctverec = Ctverec(5)
ctverec.write()
obdelnik = Obdelnik(4,5)
obdelnik.write()
krychle = Krychle(5)
krychle.write()
kvadr = Kvadr(4,5,6)
kvadr.write()
kruh=Kruh(10)
kruh.write()
kvadr = Kvadr(4,5,6)
kvadr.write()
koule = Koule(10)
koule.write()

