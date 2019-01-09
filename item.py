from updateable import Updateable

class Item():


    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


    def __repr__(self):
        return '%s, %s, %s' % (self.getName(), self.getSellIn(), self.getQuality())


if __name__ == '__main__':

    pato = Item('pato', '20', '4')

    print(pato)
