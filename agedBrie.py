from regularItem import RegularItem


class agedBrie(RegularItem):


    def update_quality(self):
        if self.getSellIn() >= 0:
            self.quality += 1
        else:
            self.quality += 2


if __name__ == '__main__':

    # test case 1
    pato = agedBrie('pato', 9, 4)
    pato.update_quality()
    pato.getQuality() == 5
