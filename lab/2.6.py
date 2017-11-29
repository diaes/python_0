n = int(raw_input("Daj n"))
pierwsza = 0
druga = 1
x = 1

while (x <= n):
    print pierwsza
    x = x + 1
    pierwsza = pierwsza + druga
    if (x <= n):
        print druga
        x = x + 1
        druga = druga + pierwsza
    else:
        break



