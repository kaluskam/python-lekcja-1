# Python - Lekcja 4

**Temat:** Pętle – zagnieżdżanie, `break`, `continue` i praktyczne wzorce

---

## 👋 Wprowadzenie

Na poprzedniej lekcji poznałeś podstawy pętli `while` i `for`. Teraz pójdziemy o krok dalej – nauczysz się **zagnieżdżać pętle**, kontrolować ich przepływ za pomocą `break` i `continue`, oraz poznasz praktyczne wzorce programistyczne.

---

## 🎯 Cel lekcji

Po tej lekcji będziesz potrafił/a:

* Tworzyć zagnieżdżone pętle (pętla w pętli)
* Używać `break` do przerywania pętli
* Używać `continue` do pomijania iteracji
* Stosować pętle do rozwiązywania praktycznych problemów
* Pracować z listami (wprowadzenie)

---

## 🛠️ Mini projekt: Generator Wzorów i Gra Zgadywanka

Podczas lekcji stworzysz programy, które:

* generują różne wzory z gwiazdek
* implementują prostą grę zgadywankę
* wyszukują dane spełniające określone kryteria

---

## ⏱️ Przebieg lekcji

### 1. Zagnieżdżone pętle

Pętla zagnieżdżona to **pętla wewnątrz innej pętli**. Zewnętrzna pętla wykonuje się raz, a wewnętrzna wykonuje się **w całości** przy każdej iteracji zewnętrznej.

#### Przykład – siatka współrzędnych:

```python
for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print()  # nowa linia po każdym wierszu
```

Wynik:

```
(0, 0) (0, 1) (0, 2) 
(1, 0) (1, 1) (1, 2) 
(2, 0) (2, 1) (2, 2) 
```

📌 Co warto zapamiętać:

* zewnętrzna pętla kontroluje **wiersze**
* wewnętrzna pętla kontroluje **kolumny**
* `end=" "` sprawia, że `print()` nie przechodzi do nowej linii

---

#### Przykład – prostokąt z gwiazdek:

```python
width = 5
height = 3

for row in range(height):
    for col in range(width):
        print("*", end="")
    print()
```

Wynik:

```
*****
*****
*****
```

---

#### Przykład – trójkąt:

```python
height = 5

for row in range(1, height + 1):
    for col in range(row):
        print("*", end="")
    print()
```

Wynik:

```
*
**
***
****
*****
```

📌 W każdym wierszu liczba gwiazdek równa się numerowi wiersza.

---

#### 🔹 Ćwiczenie 1:

Napisz program, który wyświetla trójkąt odwrócony:

```
*****
****
***
**
*
```

---

### 2. Tabliczka mnożenia z zagnieżdżonymi pętlami

```python
print("Tabliczka mnożenia 1-5:")
print()

for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result:4}", end="")
    print()
```

Wynik:

```
Tabliczka mnożenia 1-5:

   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

📌 `{result:4}` formatuje liczbę na 4 znaki szerokości (wyrównanie).

---

### 3. Instrukcja `break`

`break` **natychmiast kończy** pętlę, nawet jeśli warunek jest nadal prawdziwy.

#### Przykład – szukanie liczby:

```python
target = 7

for i in range(1, 20):
    print(f"Sprawdzam: {i}")
    if i == target:
        print(f"Znaleziono: {i}")
        break

print("Koniec przeszukiwania")
```

Wynik:

```
Sprawdzam: 1
Sprawdzam: 2
...
Sprawdzam: 7
Znaleziono: 7
Koniec przeszukiwania
```

📌 Pętla kończy się po znalezieniu liczby 7, nie sprawdza dalszych wartości.

---

#### Przykład – gra zgadywanka:

```python
secret_number = 42
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Próba {attempt}: Zgadnij liczbę (1-100): "))
    
    if guess == secret_number:
        print(f"Brawo! Zgadłeś w {attempt} próbie!")
        break
    elif guess < secret_number:
        print("Za mało!")
    else:
        print("Za dużo!")
else:
    print(f"Przegrałeś! Liczba to była: {secret_number}")
```

📌 Blok `else` po pętli `for` wykonuje się tylko wtedy, gdy pętla **nie została przerwana przez `break`**.

---

### 4. Instrukcja `continue`

`continue` **pomija resztę** bieżącej iteracji i przechodzi do następnej.

#### Przykład – pomijanie liczb parzystych:

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

Wynik:

```
1
3
5
7
9
```

📌 Gdy `i` jest parzyste, `continue` pomija `print()` i przechodzi do kolejnej liczby.

---

#### Przykład – filtrowanie danych:

```python
words = ["apple", "", "banana", "", "cherry", ""]

for word in words:
    if word == "":
        continue
    print(f"Słowo: {word}")
```

Wynik:

```
Słowo: apple
Słowo: banana
Słowo: cherry
```

---

#### 🔹 Ćwiczenie 2:

Napisz program, który:

1. Wyświetla liczby od 1 do 20
2. Pomija liczby podzielne przez 3
3. Zatrzymuje się, gdy napotka liczbę 17

---

### 5. Wprowadzenie do list

**Lista** to kolekcja elementów w jednym miejscu. Poznasz je dokładniej w przyszłości, ale już teraz możesz ich używać z pętlami.

#### Tworzenie listy:

```python
fruits = ["apple", "banana", "cherry", "orange"]
numbers = [10, 20, 30, 40, 50]
```

#### Iteracja po liście:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

---

#### Iteracja z indeksem:

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

Wynik:

```
0: apple
1: banana
2: cherry
```

📌 `len(fruits)` zwraca liczbę elementów w liście.

---

### 6. Praktyczne wzorce

#### Znajdowanie maksimum:

```python
numbers = [23, 45, 12, 67, 34, 89, 21]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(f"Największa liczba: {maximum}")
```

---

#### Zliczanie elementów:

```python
text = "programming"
target = "m"

count = 0

for letter in text:
    if letter == target:
        count = count + 1

print(f"Litera '{target}' występuje {count} razy")
```

---

#### Walidacja hasła:

```python
password = input("Podaj hasło: ")

has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Hasło jest silne")
else:
    print("Hasło jest za słabe")
```

---

#### 🔹 Ćwiczenie 3:

Napisz program, który:

1. Ma listę ocen: `[4, 5, 3, 5, 4, 2, 5, 3]`
2. Oblicza średnią ocen
3. Zlicza ile jest ocen 5

---

## 📝 Praca domowa

### Zadanie 1: Piramida

Napisz program, który rysuje piramidę:

```
Podaj wysokość: 5

    *
   ***
  *****
 *******
*********
```

💡 Wskazówka: każdy wiersz ma spacje przed gwiazdkami.

---

### Zadanie 2: Gra w zgadywanie

Napisz program, który:

* losuje liczbę od 1 do 50 (użyj `import random` i `random.randint(1, 50)`)
* daje użytkownikowi 7 prób
* po każdej próbie mówi "Za mało" lub "Za dużo"
* kończy się sukcesem lub porażką

---

### Zadanie 3: Analiza tekstu

Napisz program, który:

* pyta użytkownika o zdanie
* zlicza:
  * liczbę liter
  * liczbę cyfr
  * liczbę spacji
* wyświetla statystyki

Przykład:

```
Podaj zdanie: Python 3 jest super!
Litery: 15
Cyfry: 1
Spacje: 3
```

💡 Wskazówki:

* `char.isalpha()` – sprawdza czy znak jest literą
* `char.isdigit()` – sprawdza czy znak jest cyfrą
* `char == " "` – sprawdza czy znak jest spacją

---

### Zadanie 4: Ramka (⭐ dodatkowe)

Napisz program, który rysuje ramkę:

```
Podaj szerokość: 7
Podaj wysokość: 4

*******
*     *
*     *
*******
```

💡 Pierwszy i ostatni wiersz to same gwiazdki, środkowe mają gwiazdki tylko na brzegach.

---

### Zadanie 5: Liczby pierwsze (⭐ dodatkowe)

Napisz program, który:

* pyta użytkownika o liczbę `n`
* wyświetla wszystkie liczby pierwsze od 2 do `n`

💡 Liczba pierwsza dzieli się tylko przez 1 i siebie.

---

## 📌 Co dalej?

Na kolejnej lekcji nauczysz się:

* czym są funkcje
* jak definiować własne funkcje
* jak przekazywać argumenty do funkcji

---

💪 Świetna robota! Zagnieżdżone pętle i kontrola przepływu to potężne narzędzia!
