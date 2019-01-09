from agedBrie import AgedBrie
from backstage import Backstage
from sulfuras import Sulfuras


class GildedRose():


    def __init__(self, stock):
        self.stock = stock


    def getStock(self):
        return self.stock


    def update_stock(self):
        for item in self.stock:
            item.update_quality()


if __name__ == '__main__':

    # test case 1
    stock = [Sulfuras('sulfuras', 10, 80), AgedBrie('agedBrie', 3, 4), Backstage('backstage', 5, 25)]
    tienda = GildedRose(stock)
    tienda.update_stock()
    assert tienda.getStock()[0].getQuality() == 80
    assert tienda.getStock()[0].getName() == 'sulfuras'
    assert tienda.getStock()[0].getSellIn() == 10
