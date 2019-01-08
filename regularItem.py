from item import Item
from updateable import Updateable


class RegularItem(Item, Updateable):

    def setSellIn(self):
        return self.sell_in - 1


    def update_quality(self):
        if self.sell_in > 0:
            return self.quality - 1
        else:
            return self.quality -2


if __name__ == '__main__':

    pato = RegularItem('pato', 0, 4)

    assert pato.setSellIn() == -1
    assert pato.update_quality() == 2
