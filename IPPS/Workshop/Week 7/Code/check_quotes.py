def check_quotes(line):
    single = 0
    double = 0
    for ch in line:
        if ch in ("'", "’", "‘"):
            single += 1
        elif ch in ('"', '“', '”'):
            double += 1
    return single % 2 == 0 and double % 2 == 0
line = "Today’s high temperature will be 75 degrees" #taken from a text file 
print (check_quotes(line))
