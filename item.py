from updateable import Updateable

class Item(Updateable):


    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


    def getName(self):
        return self.name


    def getSellIn(self):
        return self.sell_in


    def getQuality(self):
        return self.quality


    def __repr__(self):
        return '%s, %s, %s' % (self.getName(), self.getSellIn(), self.getQuality())


if __name__ == '__main__':

    pato = Item('pato', '20', '4')

    print(pato)

    assert pato.update_quality() == None
    assert pato.getName() == 'pato'
    assert pato.getSellIn() == '20'
    assert pato.getQuality() == '4'
