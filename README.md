# Repülőjegy Foglaló Rendszer

Ez a projekt egy egyszerű konzolos alkalmazás, amely belföldi és nemzetközi járatokra történő **jegyfoglalást** tesz lehetővé. A feladat a GDE OOP beadandó keretében készült.

---

## Követelmények

| Szoftver     | Verzió                          |
| ------------ | ------------------------------- |
| **Python**   | 3.11 vagy újabb                 |
| Külső csomag | *nincs* (csak standard library) |

---

## Telepítés 

# repó klónozása
git clone [https://github.com/gonzodr/GDE_Flyight.git]

cd GDE_Flyght

## Fut­tatás 🚀

python main.py


A program indításakor egy menü jelenik meg:

1) Jegy foglalása
2) Foglalás lemondása
3) Foglalások listázása
4) Árlista
5) Kilépés


## Fájlstruktúra

| Fájl         | Leírás                                                                    |
| ------------ | ------------------------------------------------------------------------- |
| `main.py`    | Belépési pont, CLI menü                                                   |
| `flight.py`  | **Járat** absztrakt osztály + *Domestic* / *International* implementációk |
| `booking.py` | **Booking** osztály (egyedi foglalások)                                   |
| `helper.py`  | Segéd‑függvények (pl. táblázat‑formázás)                                  |
| `adatok.txt` | Név, szak, Neptun kód                                                     |

---

## Fejlesztő

> **Szilvási Marcell**
> Neptun: **AUZNUT**
> Mérnökinformatika BSc

