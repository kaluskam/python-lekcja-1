# Python - Lekcja 1

## 👋 Wprowadzenie

Ten materiał jest przeznaczony **dla Ciebie jako studenta**. Poprowadzi Cię krok po kroku przez pierwszą lekcję Pythona i pomoże stworzyć **pierwszy praktyczny program**.

Nie musisz mieć wcześniejszego doświadczenia z programowaniem.

---

## 🎯 Cel lekcji

Po tej lekcji będziesz potrafił/a:

* Wyjaśnić, czym jest Python i do czego się go używa
* Uruchomić prosty program w Pythonie
* Korzystać z:

  * `print()` – do wyświetlania informacji
  * zmiennych – do przechowywania danych
  * `input()` – do pobierania danych od użytkownika
* Napisać prosty program w formie **mini projektu**

---

## 🛠️ Mini projekt: Generator Profilu Osobistego

Podczas lekcji stworzysz program, który:

* zadaje użytkownikowi kilka pytań
* zapisuje odpowiedzi w zmiennych
* wyświetla czytelne podsumowanie

Program działa w terminalu (konsoli).

---

## ⏱️ Przebieg lekcji

### 1. Pierwszy program

Zaczniemy od najprostszego programu:

```python
print("Hello, world!")
```

📌 Co warto zapamiętać:

* Python wykonuje kod linijka po linijce
* `print()` wyświetla tekst na ekranie
* Tekst zapisujemy w cudzysłowie

---


### 2. Typy danych, zmienne tekstowe i liczbowe

W Pythonie każda zmienna ma **typ danych**, który określa, jakiego rodzaju informację przechowuje.

#### 🔤 Zmienne tekstowe (strings)

Tekst w Pythonie zapisujemy w cudzysłowie (`" "` lub `' '`).

```python
first_name = "Anna"
city = "Warszawa"
print(first_name)
print(city)
```

📌 Tekst (string):

* służy do przechowywania napisów
* zawsze jest w cudzysłowie

Możesz łączyć teksty:

```python
print("Cześć, mam na imię", first_name)
```

---

#### 📏 Funkcja `len()` – długość tekstu

Python posiada wbudowaną funkcję `len()`, która zwraca **długość tekstu**, czyli liczbę znaków w napisie.

```python
name = "Anna"
print(len(name))
```

📌 W tym przykładzie:

* `"Anna"` ma **4 znaki**
* `len(name)` zwraca liczbę `4`

Funkcja `len()` bardzo często używana jest do:

* sprawdzania długości imion
* walidacji haseł
* pracy z tekstem

🔹 Ćwiczenie:

1. Poproś użytkownika o podanie imienia
2. Zapisz imię w zmiennej
3. Wyświetl długość imienia używając `len()`

📌 Przykład wyniku:

```
Twoje imię ma 5 znaków
```
---

#### 🧩 f-stringi – wygodne formatowanie tekstu

Python umożliwia wygodne tworzenie tekstu z użyciem **f-stringów**. Pozwalają one wstawiać zmienne bezpośrednio do tekstu.

```python
first_name = "Anna"
age = 30
print(f"Mam na imię {first_name} i mam {age} lat")
```

📌 Co warto wiedzieć o f-stringach:

* przed cudzysłowem zawsze stoi litera `f`
* zmienne umieszczamy w klamrach `{}`
* kod jest czytelniejszy niż przy łączeniu tekstów

F-stringi są **najczęściej polecanym sposobem** tworzenia tekstu w Pythonie.

---

### 🏷️ Zasady tworzenia nazw zmiennych

Aby kod był czytelny i zgodny z dobrymi praktykami Pythona, należy stosować się do poniższych zasad:

#### ✅ Snake case (zalecany styl)

Nazwy zmiennych powinny być zapisywane w **snake_case**, czyli:

* małe litery
* słowa oddzielone znakiem podkreślenia `_`

```python
first_name = "Anna"
total_price = 199.99
user_age = 30
```

❌ Niepoprawnie:

```python
FirstName = "Anna"
totalPrice = 199.99
userage = 30
```

---

#### 🚫 Słowa kluczowe (keywords)

W Pythonie istnieją **słowa kluczowe**, których **nie wolno używać jako nazw zmiennych**, ponieważ mają specjalne znaczenie w języku.

Przykłady słów kluczowych:

* `if`
* `else`
* `for`
* `while`
* `class`
* `def`

❌ Przykład błędu:

```python
if = 5
class = "Python"
```

📌 Python zgłosi błąd, jeśli spróbujesz użyć słowa kluczowego jako nazwy zmiennej.

---

```python
print("Cześć, mam na imię", first_name)
```

---

#### 🔢 Zmienne liczbowe (numbers)

Najczęściej używane typy liczb:

* `int` – liczby całkowite (np. 10, 25)
* `float` – liczby z częścią dziesiętną (np. 3.14, 2.5)

```python
age = 30          # int
price = 19.99     # float
```

---

#### ➕ Operacje arytmetyczne

Na zmiennych liczbowych możesz wykonywać obliczenia:

```python
a = 10
b = 3

print(a + b)   # dodawanie
print(a - b)   # odejmowanie
print(a * b)   # mnożenie
print(a / b)   # dzielenie
```

📌 Ważne:

* Dzielenie (`/`) zawsze zwraca liczbę typu `float`
* Python sam rozpoznaje typ danych

---

#### 🧠 Sprawdzanie typu danych

Możesz sprawdzić, jakiego typu jest zmienna:

```python
print(type(age))
print(type(first_name))
```

---

### 3. Dane od użytkownika (`input()`)

Teraz sprawimy, że program będzie „rozmawiał” z użytkownikiem.

```python
name = input("Podaj swoje imię: ")
print("Cześć", name)
```

📌 Ważne informacje:

* `input()` zatrzymuje program i czeka na odpowiedź
* Wszystko, co wpisze użytkownik, jest traktowane jako tekst

🔹 Ćwiczenie:
Poproś użytkownika o:

* wiek
* zawód

i wyświetl jedno zdanie z tymi informacjami.

---

## 📝 Praca domowa – projekt

### 🏗️ Rozszerzony Profil Użytkownika

Twoim zadaniem domowym jest rozbudowanie programu z lekcji.

Program powinien:

* zapytać o:

  * imię
  * wiek
  * miasto
  * zawód
  * jedną umiejętność, której chcesz się nauczyć
* wyświetlić czytelne i estetyczne podsumowanie

📌 Przykład:

```
Witamy w aplikacji Profil!
-------------------------
Imię: Alex
Długość imienia: 4
Wiek: 30
Miasto: Berlin
Zawód: Grafik
Cel nauki: Automatyzacja w Pythonie
```

### ⭐ Zadania dodatkowe (opcjonalne)

* Dodaj powitanie na początku programu
* Dodaj linie oddzielające sekcje
* Spraw, aby komunikat końcowy był bardziej osobisty

---

## 📌 Co dalej?

Na kolejnej lekcji nauczysz się:

* instrukcji warunkowych `if`, `elif`, `else`
* jak podejmować decyzje w programie
* jak reagować na różne dane od użytkownika

---

💪 Powodzenia! Ten projekt to Twój pierwszy krok w programowaniu w Pythonie.
