from day05 import Polymer
from lib.filehelper import file_to_str_array


class TestDay05:
    def test_init_print(self):
        testinput="baAb"
        testpolymer=Polymer(testinput)
        assert "baAb" == str(testpolymer)
        assert 4 == len(testpolymer)

    def test_react(self):
        testinput="baAb"
        testpolymer=Polymer(testinput)
        testpolymer.reactonce()
        print(testpolymer)
        assert str(testpolymer) == "bb"

    def test_reactlots(self):
        testinput="abcdeEDCBA"
        testpolymer=Polymer(testinput)
        testpolymer.react()
        print(testpolymer)
        assert str(testpolymer) == ""

    def test_example1(self):
        testinput="dabAcCaCBAcCcaDA"
        testpolymer=Polymer(testinput)
        testpolymer.react()
        assert len(testpolymer) ==10

    def test_remove_unita(self):
        testinput="dabAcCaCBAcCcaDA"
        testpolymer=Polymer(testinput)
        testpolymer.remove_unit("a")
        print(testpolymer)
        testpolymer.react()
        assert len(testpolymer) ==6

    def test_remove_unitb(self):
        testinput="dabAcCaCBAcCcaDA"
        testpolymer=Polymer(testinput)
        testpolymer.remove_unit("b")
        print(testpolymer)
        testpolymer.react()
        assert len(testpolymer) ==8
