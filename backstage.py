from regularItem import RegularItem


class Backstage(RegularItem):


    def update_quality(self):
        if self.getSellIn() > 10:
            self.quality += 1
        elif self.getSellIn() <= 5:
            self.quality += 3
        elif 5 <= self.getSellIn() <= 10:
            self.quality += 2
        else:
            self.quality = 0


if __name__ == '__main__':

    # test case 1
    pato = Backstage('pato', 9, 4)
    pato.update_quality()
    assert pato.getQuality() == 6
