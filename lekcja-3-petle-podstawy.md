# Python - Lekcja 3

**Temat:** Pętle – podstawy (`while` i `for`)

---

## 👋 Wprowadzenie

Na tej lekcji poznasz **pętle** – jeden z najważniejszych elementów programowania. Pętle pozwalają wykonywać ten sam kod **wielokrotnie**, bez konieczności pisania go za każdym razem od nowa.

---

## 🎯 Cel lekcji

Po tej lekcji będziesz potrafił/a:

* Wyjaśnić, czym są pętle i do czego służą
* Używać pętli `while` do powtarzania kodu
* Używać pętli `for` do iteracji po elementach
* Korzystać z funkcji `range()` do generowania sekwencji liczb
* Napisać prosty program wykorzystujący pętle

---

## 🛠️ Mini projekt: Licznik i Generator Powtórzeń

Podczas lekcji stworzysz programy, które:

* odliczają od zadanej liczby do zera
* powtarzają tekst określoną liczbę razy
* sumują liczby podane przez użytkownika

---

## ⏱️ Przebieg lekcji

### 1. Czym jest pętla?

Wyobraź sobie, że chcesz wyświetlić "Cześć!" 5 razy. Bez pętli musiałbyś napisać:

```python
print("Cześć!")
print("Cześć!")
print("Cześć!")
print("Cześć!")
print("Cześć!")
```

Z pętlą wystarczy:

```python
for i in range(5):
    print("Cześć!")
```

📌 Pętla pozwala:

* wykonać kod wielokrotnie
* uniknąć powtarzania się
* pracować z dużą ilością danych

---

### 2. Pętla `while`

Pętla `while` wykonuje kod **dopóki warunek jest prawdziwy**.

#### Składnia:

```python
while condition:
    # kod do wykonania
```

#### Przykład – odliczanie:

```python
count = 5

while count > 0:
    print(count)
    count = count - 1

print("Start!")
```

📌 Co warto zapamiętać:

* `while` sprawdza warunek **przed każdym wykonaniem**
* kod wewnątrz pętli musi być **wcięty**
* musisz zadbać o to, by warunek kiedyś stał się fałszywy (inaczej pętla nigdy się nie skończy!)

---

#### ⚠️ Pętla nieskończona

Jeśli warunek nigdy nie stanie się fałszywy, pętla będzie działać w nieskończoność:

```python
# ❌ NIE RÓB TEGO - pętla nieskończona!
count = 5
while count > 0:
    print(count)
    # brakuje: count = count - 1
```

📌 Aby zatrzymać taką pętlę, użyj `Ctrl + C` w terminalu.

---

#### 🔹 Ćwiczenie 1:

Napisz program, który:

1. Pyta użytkownika o liczbę
2. Wyświetla wszystkie liczby od 1 do tej liczby

Przykład:

```
Podaj liczbę: 4
1
2
3
4
```

---

### 3. Pętla `for`

Pętla `for` służy do **iteracji** – przechodzenia przez elementy jeden po drugim.

#### Iteracja po tekście:

```python
name = "Python"

for letter in name:
    print(letter)
```

Wynik:

```
P
y
t
h
o
n
```

📌 Pętla `for` automatycznie przechodzi przez każdy element.

---

### 4. Funkcja `range()`

`range()` generuje sekwencję liczb. Jest bardzo często używana z pętlą `for`.

#### Podstawowe użycie:

```python
for i in range(5):
    print(i)
```

Wynik:

```
0
1
2
3
4
```

📌 Ważne:

* `range(5)` generuje liczby od **0 do 4** (5 liczb)
* ostatnia liczba **nie jest uwzględniona**

---

#### `range()` z początkiem i końcem:

```python
for i in range(1, 6):
    print(i)
```

Wynik:

```
1
2
3
4
5
```

📌 `range(start, stop)` – zaczyna od `start`, kończy przed `stop`.

---

#### `range()` z krokiem:

```python
for i in range(0, 10, 2):
    print(i)
```

Wynik:

```
0
2
4
6
8
```

📌 `range(start, stop, step)` – trzeci argument określa **krok** (co ile zwiększać).

---

#### 🔹 Ćwiczenie 2:

Napisz program, który wyświetla liczby parzyste od 2 do 20.

---

### 5. Porównanie `while` i `for`

| Cecha | `while` | `for` |
|-------|---------|-------|
| Kiedy używać | Gdy nie wiesz ile razy powtórzyć | Gdy wiesz ile razy lub iterujesz po elementach |
| Warunek | Sprawdzany przed każdą iteracją | Automatycznie przechodzi przez elementy |
| Ryzyko | Pętla nieskończona | Bezpieczniejsza |

---

### 6. Praktyczne przykłady

#### Sumowanie liczb:

```python
total = 0

for i in range(1, 6):
    total = total + i
    print(f"Dodaję {i}, suma = {total}")

print(f"Końcowa suma: {total}")
```

---

#### Tabliczka mnożenia (fragment):

```python
number = 7

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

---

#### Zbieranie danych od użytkownika:

```python
total = 0
count = 0

answer = "yes"

while answer == "yes":
    number = int(input("Podaj liczbę: "))
    total = total + number
    count = count + 1
    answer = input("Czy chcesz podać kolejną liczbę? (yes/no) ")

print(f"Suma {count} liczb wynosi: {total}")
```

---

#### 🔹 Ćwiczenie 3:

Napisz program, który:

1. Pyta użytkownika o imię
2. Wyświetla każdą literę imienia w osobnej linii
3. Na końcu wyświetla liczbę liter

---

## 📝 Praca domowa

### Zadanie 1: Odliczanie

Napisz program, który:

* pyta użytkownika o liczbę startową
* odlicza od tej liczby do 1
* na końcu wyświetla "Boom!"

Przykład:

```
Podaj liczbę startową: 5
5
4
3
2
1
Boom!
```

---

### Zadanie 2: Suma liczb

Napisz program, który:

* pyta użytkownika o liczbę `n`
* oblicza sumę wszystkich liczb od 1 do `n`
* wyświetla wynik

Przykład:

```
Podaj liczbę: 5
Suma liczb od 1 do 5 wynosi: 15
```

---

### Zadanie 3: Tabliczka mnożenia

Napisz program, który:

* pyta użytkownika o liczbę
* wyświetla tabliczkę mnożenia dla tej liczby (od 1 do 10)

---

### Zadanie 4: Hasło (⭐ dodatkowe)

Napisz program, który:

* ma zapisane poprawne hasło (np. `"python123"`)
* pyta użytkownika o hasło
* jeśli hasło jest błędne, pyta ponownie (maksymalnie 3 próby)
* po 3 błędnych próbach wyświetla "Dostęp zablokowany"
* jeśli hasło jest poprawne, wyświetla "Dostęp przyznany"

---

### Zadanie 5: Rysowanie (⭐ dodatkowe)

Napisz program, który rysuje prostokąt z gwiazdek:

```
Podaj szerokość: 5
Podaj wysokość: 3

*****
*****
*****
```

---

## 📌 Co dalej?

Na kolejnej lekcji nauczysz się:

* zagnieżdżonych pętli (pętla w pętli)
* instrukcji `break` i `continue`
* bardziej zaawansowanych wzorców z pętlami

---

💪 Powodzenia! Pętle to fundament programowania – ćwicz je regularnie!
