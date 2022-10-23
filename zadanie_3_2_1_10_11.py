# Poproś użytkownika o wprowadzenie słowa
# i przypisz je do zmiennej slowo_uzytkownika
slowo_uzytkownika=input("Podaj dowolne słowo:").upper()
slowo=""
for litera in slowo_uzytkownika:
    # Uzupełnij pętlę for poniżej. Rozwiązanie najmniej efektowne
    """
    if litera=='A':
        continue
    elif litera=='E':
        continue
    elif litera=='I':
        continue
    elif litera=='O':
        continue
    elif litera=='U':
        continue
    """
    #rozwiązanie efektowniejsze
    #if litera=='A' or litera=='E' or litera=='I' or litera=='O' or litera=='U':
    #    continue
    #rozwiązanie efektowne i efektywne (mało kodu, taka sama praca)
    if litera in ('A','E','I','O','U'):
        continue
    slowo+=litera #rozwiązanie 3.2.1.11
    print(litera)

print(slowo)#rozwiązanie 3.2.1.11
