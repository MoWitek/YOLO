from datetime import datetime

test_file = "../../stuff/Aufgabe4/fahrradwerkstatt0.txt"
lines = []
"""
1. Der erste Wert ist der Eingangszeitpunkt in Minuten seit Start t0.
2. Der zweite Wert ist die geschätzte Dauer in Minuten. 
3. t0 ist immer 00:00
4. Marc arbeitet jeden von 9 bis 17
"""

"""
Plan:
    - convert minutes to hh:mm                          DONE
    - convert hh:mm to datetime for better comparison   DONE
    - check if between 09:00 and 17:00                  DONE
    - add as many minutes as possible
"""

def convert_time(minutes: int):
    time = '{:02d}:{:02d}'.format(*divmod(minutes, 60))
    dt = datetime.combine(datetime.today(), datetime.strptime(time, '%H:%M').time())
    return dt

def read_lines():
    with open(test_file, 'r') as f:
        lines = f.readlines()
    return lines

def to_pairs(lines):
    

# bad name i know, converts every time of an array
def convert_lines(lines):
    

def is_day(minutes: int):
    t = convert_time(minutes)
    return t.hour >= 9 and t.hour < 17
