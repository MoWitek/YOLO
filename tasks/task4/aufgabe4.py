test_file = "../../stuff/Aufgabe4/fahrradwerkstatt0.txt"
lines = []

"""
1. Der erste Wert ist der Eingangszeitpunkt in Minuten seit Start t0.
2. Der zweite Wert ist die geschätzte Dauer in Minuten. 
3. t0 ist immer 00:00
4. Marc arbeitet jeden von 9 bis 17
"""

def to_minutes(hours: int):
    return hours * 60

def get_durations():
    durations = []
    with open(test_file, 'r') as f:
        lines = f.readlines()
        tmp = []
        for l in lines:
            tmp = l.split(' ')
            durations.append(int(tmp[1]))
        return durations

def average_duration():
    sum = 0
    for d in get_durations():
        sum += d

    return sum / len(get_durations())


