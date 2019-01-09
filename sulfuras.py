from regularItem import RegularItem


class Sulfuras(RegularItem):


    def update_quality(self):
        assert self.quality == 80
        self.quality = 80


if __name__ == '__main__':

    # test case 1
    pato = Sulfuras('pato', 2, 80)
    pato.update_quality()
    assert pato.getQuality() == 80
