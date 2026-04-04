def extract_temp(l):
    num = 0
    for ch in l:
        if '0' <= ch <= '9':
            num = num * 10 + (ord(ch) - ord('0'))
    print(num)
line = "The high today will be 75 degrees"
extract_temp(line)
