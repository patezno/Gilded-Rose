from regularItem import RegularItem


class ConjuredItem(RegularItem):


    def update_quality(self):
        if self.getSellIn() >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)


if __name__ == '__main__':

    # test case 1
    pato = ConjuredItem('pato', 15, 20)
    pato.update_quality()
    assert pato.getQuality() == 18
