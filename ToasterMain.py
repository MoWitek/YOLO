from Toaster import Test, NotHumanConfirmed

import datasets

from tasks.junior1 import AufgabeJunior1
from tasks.junior2 import AufgabeJunior2
from tasks.task1 import Aufgabe1

class AufgabeJunior1Test:
    class bwinf_data_set:

        # not entirely checked
        def test0(self):
            assert AufgabeJunior1.match_rhymes(datasets.JuniorAufgabe1.txt0) == ([('schiene', 'biene'), ('recht', 'knecht'), ('glühen', 'bemühen')], ['schwank', 'schlank', 'hygiene', 'hersagen', 'breitschlagen'])
        # not entirely checked
        def test1(self):
            assert AufgabeJunior1.match_rhymes(datasets.JuniorAufgabe1.txt1) == ([('wildnis', 'bildnis'), ('note', 'brote')], ['xor-funktion', 'paprikaschote', 'konsumption', 'geständnis', 'absorption'])

        def test2(self):
            assert AufgabeJunior1.match_rhymes(datasets.JuniorAufgabe1.txt2) == ([('ypsilon', 'epsilon')], ['tempel', 'poststempel', 'passfoto ', 'foto'])

        def test3(self):
            raise NotHumanConfirmed
            assert AufgabeJunior1.match_rhymes(datasets.JuniorAufgabe1.txt3) == ()

    class custom_data_set:
        pass

class AufgabeJunior2Test:
    class bwinf_data_set:
        def test0(self):
            assert AufgabeJunior2.solve_for_biggest(datasets.JuniorAufgabe2.txt0) is None

        def test1(self):
            assert AufgabeJunior2.solve_for_biggest(datasets.JuniorAufgabe2.txt1) == "4"

        def test2(self):
            assert AufgabeJunior2.solve_for_biggest(datasets.JuniorAufgabe2.txt2) == None

        def test3(self):
            assert AufgabeJunior2.solve_for_biggest(datasets.JuniorAufgabe2.txt3) == None

        # not human confirmed
        # def test4(self):
        #     assert AufgabeJunior2.solve_for_biggest(datasets.JuniorAufgabe2.txt4) == ""

    class custom_data_set:
        def test0(self):
            assert AufgabeJunior2.solve_for_biggest("1 2\n2 1") is None

        def test1(self):
            assert AufgabeJunior2.solve_for_biggest("1 2\n2 3\n3 1") is None

        def test2(self):
            assert AufgabeJunior2.solve_for_biggest("1 2") == "1"

        def test3(self):
            assert AufgabeJunior2.solve_for_biggest("2 4\n4 3\n2 3") == "2"

class AufgabeNormal1Test:
    class bwinf_data_set:
        def test0(self):
            assert Aufgabe1.regex_search(datasets.NormalAufgabe1.txt0) == [['das', 'kommt', 'mir', 'gar', 'nicht', 'richtig', 'vor']]

        def test1(self):
            assert Aufgabe1.regex_search(datasets.NormalAufgabe1.txt1) == [['ich', 'muß', 'in', 'clara', 'verwandelt'], ['ich', 'muß', 'doch', 'clara', 'sein']]

        def test2(self):
            assert Aufgabe1.regex_search(datasets.NormalAufgabe1.txt2) == [['fressen', 'katzen', 'gern', 'spatzen'], ['fressen', 'katzen', 'gern', 'spatzen'], ['fressen', 'spatzen', 'gern', 'katzen']]

        def test3(self):
            assert Aufgabe1.regex_search(datasets.NormalAufgabe1.txt3) == [['das', 'spiel', 'fing', 'an'], ['das', 'publikum', 'fing', 'an']]

        def test4(self):
            assert Aufgabe1.regex_search(datasets.NormalAufgabe1.txt4) == [['ein', 'sehr', 'schöner', 'tag']]

        def test5(self):
            assert Aufgabe1.regex_search(datasets.NormalAufgabe1.txt5) == [['wollen', 'sie', 'so', 'gut', 'sein']]



Test([
    AufgabeJunior1Test,
    AufgabeJunior2Test,
    AufgabeNormal1Test,
])
