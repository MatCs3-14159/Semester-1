def check_nondigit(a):
    for ch in a:
        if not ('0' <= ch <= '9'):
            return True
    return False
ss_num = input ("Social security number: ")
print (check_nondigit (ss_num))
