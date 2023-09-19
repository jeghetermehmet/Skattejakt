def skriv_ut_skattekart(kart):
    for rad in kart:
        print(" ".join(rad))

# Oppretter skattekart
skattekart =  []
stoerrelse = 5
for e in range(stoerrelse):
    a = []
    for e in range(stoerrelse):
        a.append("O")
    skattekart.append(a)

skriv_ut_skattekart(skattekart)

# Lar spiller 1 gjette
print("Spiller 1, du skal gjemme skatten!")
gyldig = False
# Ber om input frem til vi faar gyldige koordinater
while not gyldig:
    print("Hvor vil du gjemme skatten?")
    in_x = input("Oppgi x-koordinat: ")
    in_y = input("Oppgi y-koordinat: ")
    if in_y.isdigit() and in_y.isdigit():
        x = int(in_x)
        y = int(in_y)
        if 0 <= x < stoerrelse and 0 <= y < stoerrelse:
            skattekart[y][x] = "X"
            gyldig = True
        else:
            print("Ugyldig plassering!")
    else:
        print("Ugyldig input!")

# "Visker ut" skjermen for aa skjule informasjon for spiller 2
for e in range (100):
    print("\n")

# Lar spiller 2 gjette paa plassering
print("Spiller 2, du skal finne skatten!")
antall_gjett = 3
funnet_skatt = False
# Lar spiller 2 fortsette aa gjette saa lenge skatten ikke er funnet
# og de har flere forsoek igjen
while antall_gjett > 0 and not funnet_skatt:
    print("Antall forsoek igjen:", antall_gjett)
    gyldig = False
    while not gyldig:
        print("Hvor vil du lete etter skatten?")
        in_x = input("Oppgi x-koordinat: ")
        in_y = input("Oppgi y-koordinat: ")
        if in_y.isdigit() and in_y.isdigit():
            x = int(in_x)
            y = int(in_y)
            if 0 <= x < stoerrelse and 0 <= y < stoerrelse:
                gyldig = True
                if skattekart[y][x] == "X":
                    funnet_skatt = True
                    antall_gjett = 0
                else:
                    skattekart[y][x] = "#"
            else:
                print("Ugyldig plassering!")
        else:
            print("Ugyldig input!")
    antall_gjett -= 1

# Gir tilbakemelding til spiller 2
print()    # tom linje
if funnet_skatt:
    print("Gratulerer, spiller 2, du fant skatten! ")
else:
    print("Spiller 2 fant ikke skatten, så spiller 1 vinner!")

# Skriver ut skattekartet paa nytt
skriv_ut_skattekart(skattekart)