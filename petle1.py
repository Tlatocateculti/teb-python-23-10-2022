parzyste = 0
nieparzyste = 0

def zwieksznp(): 
    global nieparzyste
    nieparzyste+=1
def zwiekszp(): 
    global parzyste
    parzyste+=1

# wczytaj pierwsza liczbe
liczba = 0

# 0 konczy wykonywanie
while True:
    # sprawdz czy liczba jest nieparzysta
    liczba = int(input("Wpisz liczbe lub 0, aby zatrzymac: "))
    if liczba==0:
        break
    zwieksznp() if liczba%2 else zwiekszp()
        # zwieksz licznik liczb nieparzystych
    #    nieparzyste += 1
    #else:
        # zwieksz licznik liczb parzystych
    #    parzyste += 1
    # wczytaj kolejna liczbe
    #liczba = int(input("Wpisz liczbe lub 0, aby zatrzymac: "))

# wyswietl wynik
print("Liczb nieparzystych:", nieparzyste)
print("Liczb parzystych:", parzyste)
