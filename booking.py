# -*- coding: utf-8 -*-

class Booking:
    _next_id = 1

    def __init__(self, passenger, flight):
        self.id = Booking._next_id
        Booking._next_id += 1
        self.passenger = passenger
        self.flight = flight

    def __str__(self):
        return f'#{self.id:<3} | {self.passenger:15} | {self.flight.airline:8} | {self.flight.code:5} | {self.flight.destination:12} | {self.flight.price():6}\xa0Ft'