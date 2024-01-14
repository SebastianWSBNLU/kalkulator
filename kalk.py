def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero!"

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ program")

    wybor = input("Wprowadź numer operacji (1/2/3/4/5): ")

    if wybor == '5':
        print("Koniec programu.")
        break

    if wybor not in ('1', '2', '3', '4'):
        print("Nieprawidłowy wybór. Wybierz ponownie.")
        continue

    liczba1 = float(input("Wprowadź pierwszą liczbę: "))
    liczba2 = float(input("Wprowadź drugą liczbę: "))

    if wybor == '1':
        print("Wynik:", dodawanie(liczba1, liczba2))
    elif wybor == '2':
        print("Wynik:", odejmowanie(liczba1, liczba2))
    elif wybor == '3':
        print("Wynik:", mnozenie(liczba1, liczba2))
    elif wybor == '4':
        wynik_dzielenia = dzielenie(liczba1, liczba2)
        print("Wynik:", wynik_dzielenia)
