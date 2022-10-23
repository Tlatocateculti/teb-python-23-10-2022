tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
while True:
    wejscie=int(input("Podaj sekrtn numer:"))
    if tajny_numer==wejscie:
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
        break
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")