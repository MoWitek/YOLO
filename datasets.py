from dataset_creator import read
from json import loads

_bloat = loads(read("datasets.json"))

class JuniorAufgabe1:
    txt0 = _bloat["jr1"]["txt0"]
    txt1 = _bloat["jr1"]["txt1"]
    txt2 = _bloat["jr1"]["txt2"]
    txt3 = _bloat["jr1"]["txt3"]

class JuniorAufgabe2:
    txt0 = _bloat["jr2"]["txt0"]
    txt1 = _bloat["jr2"]["txt1"]
    txt2 = _bloat["jr2"]["txt2"]
    txt3 = _bloat["jr2"]["txt3"]
    txt4 = _bloat["jr2"]["txt4"]

class NormalAufgabe1:
    alice= _bloat["nr1"]["alice.txt"]
    txt0 = _bloat["nr1"]["txt0"]
    txt1 = _bloat["nr1"]["txt1"]
    txt2 = _bloat["nr1"]["txt2"]
    txt3 = _bloat["nr1"]["txt3"]
    txt4 = _bloat["nr1"]["txt4"]
    txt5 = _bloat["nr1"]["txt5"]

del _bloat


