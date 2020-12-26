from day21 import AllergenList


class TestDay21:
    def test_example_import(self):
        inputvalue = 'tests/day21_testinput.txt'
        testrec = AllergenList(inputvalue)
        assert 'mxmxvkd' in testrec.recipies[0][0]
        assert 'mxmxvkd' in testrec.recipies[1][0]
        assert 'fish' in testrec.recipies[0][1]
        assert 'soy' in testrec.recipies[2][1]

    def test_all_allergens(self):
        inputvalue = 'tests/day21_testinput.txt'
        testrec = AllergenList(inputvalue)
        assert 'soy' in testrec.allallergens
        assert len(testrec.allallergens) == 3
        
    def test_determine_allergens(self):
        inputvalue = 'tests/day21_testinput.txt'
        testrec = AllergenList(inputvalue)
        result=testrec.determine_allergen('dairy')
        assert result == 'mxmxvkd'
        
    def test_determine_all_allergens(self):
        inputvalue = 'tests/day21_testinput.txt'
        testrec = AllergenList(inputvalue)
        result=testrec.determine_all_allergens()
        result=testrec.determine_all_allergens()
        assert testrec.allergens['dairy'] == 'mxmxvkd'
        assert testrec.allergens['fish'] == 'sqjhc'
        assert testrec.allergens['soy'] == 'fvjkl'


    def test_run_example1(self):
        inputvalue = 'tests/day21_testinput.txt'
        testrec = AllergenList(inputvalue)
        result=testrec.run()
        assert result == 5
