# # Python - Lekcja 2

**Temat:** Instrukcje warunkowe `if`, `elif`, `else` oraz operatory logiczne

---

## 1️⃣ Warunki `if` i `else`
**Wcięcia mają znaczenie.**

```python
age = int(input("How old are you? "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 2️⃣ Instrukcja `elif` – wiele warunków

**Cel:** obsługa więcej niż dwóch przypadków

### Wyjaśnienie

`elif` (else if) pozwala sprawdzić **kolejny warunek**, jeśli poprzedni był fałszywy.

### Składnia:

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

### Przykład:

```python
age = int(input("How old are you? "))

if age < 12:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

Podkreśl:

* Python sprawdza warunki **od góry do dołu**
* wykonuje się tylko **jedna gałąź**

---

## 3️⃣ Operatory logiczne: `and`, `or`, `not`

**Cel:** łączenie warunków

### `and` – oba warunki muszą być prawdziwe

```python
age = int(input("How old are you? "))
has_id = input("Do you have an ID? (yes/no) ")

if age >= 18 and has_id == "yes":
    print("You can enter")
else:
    print("Entry denied")
```

---

### `or` – wystarczy jeden warunek

```python
day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")
```

---

### `not` – negacja warunku

```python
is_raining = input("Is it raining? (yes/no) ")

if not is_raining == "yes":
    print("You can go outside")
else:
    print("Take an umbrella")
```

---

## 4️⃣ Zadania
### Zadanie 1
Napisz program, który pobierze wynik z egzaminu użytkownika od 0 do 100 punktów,
a następnie zwróci mu ocenę.
- A - [90, 100]
- B - [80, 89]
- C - [50, 79]
- D - [0, 49]

```python
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")
```


---

## 🏠 Praca domowa

### Zadanie 1

#### 🏗️ Rozszerzony Profil Użytkownika + logika

Twoim zadaniem jest rozbudowanie programu z lekcji tak, aby **analizował dane użytkownika i podejmował decyzje**.

---

#### 🔹 Część 1 – Pobieranie danych

Program powinien zapytać o:

* imię
* wiek
* miasto
* zawód
* jedną umiejętność, której chcesz się nauczyć
* wzrost

---

#### 🔹 Część 2 – Warunki logiczne 

##### 1️⃣ Analiza wieku (`if / elif / else`)

Program powinien określić kategorię wiekową:

* jeśli wiek < 13 → `"Child"`
* jeśli wiek od 13 do 17 → `"Teenager"`
* jeśli wiek od 18 do 64 → `"Adult"`
* jeśli wiek ≥ 65 → `"Senior"`

---

##### 2️⃣ Sprawdzenie długości imienia

Program powinien:

* policzyć długość imienia (`len()`)
* jeśli długość imienia **< 4** → `"Short name"`
* jeśli długość imienia **4–7** → `"Medium name"`
* jeśli długość imienia **> 7** → `"Long name"`

---

##### 3️⃣ Logika AND (`and`)

Jeśli:

* wiek ≥ 18 **i**
* zawód to `"Programmer"` lub `"Developer"`

→ wyświetl:

```
You are already in IT
```

---

##### 4️⃣ Logika OR (`or`)

Jeśli użytkownik chce nauczyć się:

* `"Python"` **lub**
* `"Automation"`

→ wyświetl:

```
Great choice for the future!
```

---

##### 5️⃣ Logika NOT (`not`)

Jeśli miasto **nie** jest `"Warsaw"`:

→ wyświetl:

```
You are not from the capital
```

---

##### 🔹 Część 3 – Podsumowanie

Program powinien wyświetlić **czytelne podsumowanie** w formacie:

```
Welcome to the Profile App!
---------------------------
Name: Alex
Name length: 4 (Medium name)
Age: 30 (Adult)
City: Berlin
Job: Graphic Designer
Learning goal: Python
Height: 1.73m
```

---

### Zadania dodatkowe

#### Poziom 2

Dodaj sprawdzenie:

* jeśli wiek < 18 → `"Access limited"`
* w przeciwnym razie → `"Full access"`

---

#### Poziom 3

Dodaj pytanie:

```
Do you like programming? (yes/no)
```

Jeśli:

* odpowiedź `"yes"` **i**
* cel nauki to `"Python"`

→ wyświetl:

```
You are on the right path!
```

---

## 📌 Wskazówki

* używaj tylko `if / elif / else`
* używaj `and`, `or`, `not`
* dbaj o wcięcia


---

### Zadanie 2 

Program:

* pyta o nazwę użytkownika i hasło
* jeśli nazwa to `"admin"` **i** hasło to `"1234"` → `"Login successful"`
* w przeciwnym razie → `"Login failed"`

---

### Zadanie 3

Program:

* pyta o dzień tygodnia
* jeśli to `"Saturday"` lub `"Sunday"` → `"Free day"`
* jeśli to `"Monday"` i **nie** jest `"holiday"` → `"Work day"`

*(można dodać drugie pytanie: `"Is it a holiday? (yes/no)"`)*
