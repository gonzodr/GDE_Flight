# -*- coding: utf-8 -*-

from flight import DomesticFlight, InternationalFlight, Airline
from booking import Booking
from datetime import datetime
import helper

wizz = Airline('Wizz')
ryan = Airline('Ryan')

flights = [
    DomesticFlight('Budapest', 15000, 4, wizz, datetime(2025, 7, 15, 9, 0)),
    DomesticFlight('Debrecen', 13000, 3, wizz, datetime(2025, 7, 16, 15, 30)),
    InternationalFlight('London', 58000, 5, wizz, datetime(2025, 7, 20, 6, 45)),
    DomesticFlight('Pécs', 14000, 3, ryan, datetime(2025, 7, 18, 11, 10)),
    InternationalFlight('Dublin', 62000, 4, ryan, datetime(2025, 7, 22, 13, 5)),
    InternationalFlight('Berlin', 55000, 5, ryan, datetime(2025, 7, 25, 8, 0)),
]

for f in flights:
    f.airline.add(f)


bookings = []

def add_booking(passenger, flight):
    flight.book()
    b = Booking(passenger, flight)
    bookings.append(b)

add_booking('Mohamed Lee', flights[0])
add_booking('Szabó János', flights[0])
add_booking('Nagy István', flights[3])
add_booking('Kiss János', flights[1])
add_booking('Takács Anna', flights[4])
add_booking('Kovács Piroska', flights[4])

# ---------------------------------------------------------------------
def render(output=''):
    header = (
        '================================\n'
        '     GDE‑Travel  v4.0 (CLI)\n'
        '================================\n'
        f'  Járatok:    {len(flights)} | Foglalások: {len(bookings)}\n'
        '================================\n'
    )
    menu = (
        '\nMűveletek (szám + ENTER):\n'
        ' 1  Jegy foglalása\n'
        ' 2  Foglalás lemondása\n'
        ' 3  Foglalások listázása\n'
        ' 4  Árlista\n'
        ' 0  Kilépés\n'
        '----------------------------------------\n'
    )
    print(header)
    print(menu)
    if output:
        print(output)
        print('\n----------------------------------------')

# ---------------------------------------------------------------------
def main():
    output = ''
    while True:
        render(output)
        choice = input('> ').strip()
        output = ''
        try:
            if choice == '1':
                tmp = helper.flights_table(flights) + '\n'
                render(tmp)
                name = input('Utas neve: ').strip()
                if not name:
                    output = 'Nem adtál meg nevet!'
                    continue
                code = input('Járatszám: ').strip().upper()
                flight = helper.find_flight_by_code(flights, code)
                flight.book()
                b = Booking(name, flight)
                bookings.append(b)
                output = helper.bookings_table(bookings)
                output += f'\nSikeres foglalás! Azonosító: {b.id}, ár: {flight.price()} Ft'
            elif choice == '2':
                tmp = helper.bookings_table(bookings)
                render(tmp)
                bid_in = input('Melyik foglalást töröljem (id)? ').strip()
                if not bid_in.isdigit():
                    output = 'Érvénytelen azonosító!'
                    continue
                bid = int(bid_in)
                for b in bookings:
                    if b.id == bid:
                        b.flight.cancel()
                        bookings.remove(b)
                        output = helper.bookings_table(bookings)
                        output += '\nFoglalás törölve!'
                        break
                else:
                    output = 'Nincs ilyen azonosító!'
            elif choice == '3':
                output = helper.bookings_table(bookings)
            elif choice == '4':
                output = helper.flights_table(flights)
            elif choice == '0':
                print('Köszönjük, hogy velünk repült! Vizslát!!!')
                break
            else:
                output = 'Ismeretlen opció!'
        except Exception as e:
            output = f'Hiba: {e}'

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKilépés.')
