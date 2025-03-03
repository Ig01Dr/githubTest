# main.py
# Przykład prostego programu w Pythonie

def przywitaj_sie(imie):
    """Funkcja przywitania użytkownika."""
    print(f"Witaj, {imie}!")

def dodaj(a, b):
    """Funkcja dodawania dwóch liczb."""
    return a + b

def main():
    """Główna funkcja programu."""
    przywitaj_sie("Ania")
    
    x = 5
    y = 3
    wynik = dodaj(x, y)
    
    print(f"{x} + {y} = {wynik}")

if __name__ == "__main__":
    main()
