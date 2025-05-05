# -*- coding: utf-8 -*-

class Flight:
    _next_id = 1

    def __init__(self, destination, base_price, seats, category, airline):
        self.code = f'N{Flight._next_id:03d}'
        Flight._next_id += 1
        self.destination = destination
        self.base_price = base_price
        self.seats = seats
        self.category = category
        self.airline = airline
        self.booked = 0

    def price(self):
        if self.category == 'domestic':
            return int(self.base_price * 0.8)
        if self.category == 'international':
            return int(self.base_price * 1.35)
        return self.base_price

    def has_seat(self):
        return self.booked < self.seats

    def book(self):
        if not self.has_seat():
            raise Exception('Erre a járatra már nincs szabad hely!')
        self.booked += 1

    def cancel(self):
        if self.booked == 0:
            raise Exception('Nincs mit törölni!')
        self.booked -= 1

    def __str__(self):
        free = self.seats - self.booked
        cat = 'Belföldi' if self.category == 'domestic' else 'Nemzetközi'
        return f'{self.airline:8} | {self.code:5} | {self.destination:12} | {cat:12} | Ár: {self.price():6}\xa0Ft | Szabad: {free}/{self.seats}'

def make_domestic(destination, base_price, seats, airline):
    return Flight(destination, base_price, seats, 'domestic', airline)

def make_international(destination, base_price, seats, airline):
    return Flight(destination, base_price, seats, 'international', airline)