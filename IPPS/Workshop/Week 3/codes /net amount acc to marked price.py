MP = float (input ("Enter the marked price:"))
if MP>10000:
    print (f"Net amount = {MP - (0.2 * MP):,.2f}")
elif MP>7000:
    print (f"Net amount = {MP - (0.15 * MP):,.2f}")
else:
    print (f"Net amount = {MP - (0.1 * MP):,.2f}")
