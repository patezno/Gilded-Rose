from regularItem import RegularItem


class AgedBrie(RegularItem):


    def update_quality(self):
        if self.getSellIn() >= 0:
            self.setQuality(1)
        else:
            self.setQuality(2)


if __name__ == '__main__':

    # test case 1
    pato = AgedBrie('pato', 9, 4)
    pato.update_quality()
    pato.getQuality() == 5
