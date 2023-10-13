import datetime

# Initializing an empty task list
todo_list = []

# Function to add a task
def dodaj_zadanie():
    zadanie = input("Dodaj nowe zadanie: ")
    termin = input("Podaj termin wykonania (RRRR-MM-DD): ")
    try:
        termin = datetime.datetime.strptime(termin, "%Y-%m-%d").date()
        todo_list.append((zadanie, termin))
        print("Zadanie zostało dodane do listy.")
    except ValueError:
        print("Nieprawidłowy format daty. Zadanie nie zostało dodane.")

# Function to delete a task
def usun_zadanie():
    if not todo_list:
        print("Lista zadań jest pusta.")
        return

    print("Twoja lista zadań:")
    for idx, (zadanie, termin) in enumerate(todo_list):
        print(f"{idx + 1}: {zadanie} (Termin: {termin})")

    try:
        nr_zadania = int(input("Podaj numer zadania do usunięcia: "))
        if 1 <= nr_zadania <= len(todo_list):
            usuniete_zadanie, _ = todo_list.pop(nr_zadania - 1)
            print(f"Usunięto zadanie: {usuniete_zadanie}")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Nieprawidłowy numer zadania.")

# Function to display a list of tasks
def wyswietl_liste():
    if not todo_list:
        print("Lista zadań jest pusta.")
    else:
        print("Twoja lista zadań:")
        for idx, (zadanie, termin) in enumerate(todo_list):
            print(f"{idx + 1}: {zadanie} (Termin: {termin})")

# Main loop
while True:
    print("\nCo chciałbyś zrobić?")
    print("1. Dodaj nowe zadanie")
    print("2. Usuń zadanie")
    print("3. Wyświetl listę zadań")
    print("4. Wyjdź z programu")
    
    wybor = input("Wybierz opcję (1/2/3/4): ")
    
    if wybor == "1":
        dodaj_zadanie()
    elif wybor == "2":
        usun_zadanie()
    elif wybor == "3":
        wyswietl_liste()
    elif wybor == "4":
        print("Dziękuję za skorzystanie z programu. Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz ponownie.")
