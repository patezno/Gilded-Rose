from item import Item
from updateable import Updateable


class RegularItem(Item, Updateable):


    def setSellIn(self):
        self.sell_in -= 1


    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality += value
        else:
            self.quality = 0


    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)


if __name__ == '__main__':

    # caso test 1
    pato = RegularItem('pato', 9, 4)
    pato.update_quality()
    assert pato.getQuality() == 3

    # caso test 2
    pato.update_quality()
    pato.update_quality()
    pato.update_quality()
    assert pato.getQuality() == 0

    # caso test 3
    carlos = RegularItem('carlos', -4, 6)
    carlos.update_quality()
    assert carlos.getQuality() == 4
