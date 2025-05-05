# -*- coding: utf-8 -*-

def flights_table(flights):
    header = 'Légitárs. | Kód   | Célállomás   | Kategória     | Ár      | Szabad/Össz'
    sep = '-' * len(header)
    lines = [header, sep]
    for f in flights:
        free = f.seats - f.booked
        cat = 'Belföldi' if f.category == 'domestic' else 'Nemzetközi'
        line = f'{f.airline:8} | {f.code:5} | {f.destination:12} | {cat:12} | {f.price():6} Ft | {free}/{f.seats}'
        lines.append(line)
    return '\n'.join(lines)

def bookings_table(bookings):
    if not bookings:
        return '(nincs foglalás)'
    header = 'Azonosító | Utas            | Légitárs. | Kód   | Célállomás   | Ár'
    sep = '-' * len(header)
    lines = [header, sep]
    for b in bookings:
        lines.append(str(b))
    return '\n'.join(lines)

def find_flight_by_code(flights, code):
    for f in flights:
        if f.code == code:
            return f
    raise Exception('Ismeretlen járatszám!')