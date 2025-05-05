# -*- coding: utf-8 -*-

from datetime import datetime
from abc import ABC, abstractmethod

class Flight(ABC):
    
    _next_code = 1

    def __init__(self, destination, base_price, seats, airline, departure: datetime):
        self.code = f"N{Flight._next_code:03d}"
        Flight._next_code += 1

        self.destination = destination
        self.base_price = base_price
        self.seats = seats
        self.airline = airline
        self.departure = departure
        self.booked = 0

    @property
    @abstractmethod
    def category(self):
        ...

    def price(self):
        return int(self.base_price * self.multiplier())

    @abstractmethod
    def multiplier(self):
        ...

    def book(self):
        if datetime.now() >= self.departure:
            raise Exception("Ehhez a járathoz már késő foglalni!")
        if self.booked >= self.seats:
            raise Exception("Erre a járatra már nincs szabad hely!")
        self.booked += 1

    def cancel(self):
        if self.booked == 0:
            raise Exception("Nincs mit törölni!")
        self.booked -= 1

    def __str__(self):
        free = self.seats - self.booked
        cat_label = "Belföldi" if self.category == "domestic" else "Nemzetközi"
        date_str = self.departure.strftime('%Y‑%m‑%d %H:%M')
        airline_name = self.airline.name if hasattr(self.airline, "name") else self.airline

        return (
        f"{airline_name:8} | {self.code:5} | {self.destination:12} | "
        f"{cat_label:12} | {date_str:16} | Ár: {self.price():6} Ft | "
        f"Szabad: {free}/{self.seats}"
    )

class DomesticFlight(Flight):
    category = "domestic"
    DISCOUNT = 0.20           # 20 % kedvezmény

    def multiplier(self):
        return 1 - self.DISCOUNT

class InternationalFlight(Flight):
    category = "international"
    SURCHARGE = 0.35          # 35 % felár

    def multiplier(self):
        return 1 + self.SURCHARGE

class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add(self, flight):
        self.flights.append(flight)

    def list(self):
        for f in self.flights:
            print(f)

    def find(self, code):
        for f in self.flights:
            if f.code == code:
                return f
        raise Exception("Ismeretlen járatszám!")
