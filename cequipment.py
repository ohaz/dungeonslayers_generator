import random


class Money:

    def __init__(self, gold: int, silber: int, kupfer: int):
        self.value = self.calculate_value(gold, silber, kupfer)

    @staticmethod
    def calculate_value(gold: int, silber: int, kupfer: int):
        return 100 * gold + 10 * silber + kupfer

    @staticmethod
    def calculate_gold_silber_kupfer(value):
        gold = int(value / 100)
        rest = int(value % 100)
        silber = int(rest / 10)
        rest = int(value % 10)
        kupfer = rest
        return gold, silber, kupfer

    def subtract(self, gold: int, silber: int, kupfer: int):
        other_value = self.calculate_value(gold, silber, kupfer)
        if other_value > self.value:
            return False
        self.value -= other_value
        return True

    def subtract_money(self, money):
        return self.subtract(*money.calculate_gold_silber_kupfer(money.value))

    def has_enough(self):
        return self.value > 50

    def __str__(self):
        return '{}g {}s {}k'.format(*self.calculate_gold_silber_kupfer(self.value))

existing_equipment_general = [
    ('Kletterausrüstung', Money(1, 0, 0)),
    ('Seil 10m', Money(1, 0, 0)),
    ('Tagesration 3 Mahlzeiten', Money(0, 5, 0)),
    ('Wasserschlauch 5l', Money(0, 5, 0)),
    ('Heilkraut', Money(0, 25, 0)),
    ('Pfeife + 5x Kraut', Money(0, 6, 0)),
    ('Tinte (50 Seiten)', Money(2, 0, 0)),
    ('Topf', Money(1, 0, 0)),
    ('Waffenpaste', Money(0, 5, 0)),
    ('Fackel', Money(0, 0, 1)),
    ('Feuerstein + Zunder', Money(0, 0, 5)),
    ('Wachskerze', Money(0, 0, 2)),
    ('Laterne + Öl', Money(5, 0, 5)),
    ('Brechstange', Money(0, 15, 0)),
    ('Dietrich', Money(1, 0, 0)),
    ('Werkzeugset', Money(5, 0, 0)),
    ('Hund', Money(1, 0, 0)),
    ('Katze', Money(0, 1, 0)),
    ('Tür', Money(5, 0, 0)),
]

existing_equipment_sets = [
    ('Robe + Holzschild + Kampfstab 2h', Money(2, 5, 0)),
    ('Lederpanzer + Kurzbogen', Money(10, 0, 0)),
    ('Lederpanzer + Dolch + Holzschild', Money(7, 0, 0)),
    ('Lederpanzer + 3x Speer', Money(7, 0, 0)),
    ('Robe + Dolch', Money(3, 0, 0)),
    ('Streitaxt', Money(7, 0, 0)),
    ('Lederpanzer + Keule', Money(4, 2, 0)),
    ('Robe + Keule', Money(1, 2, 0)),
    ('Lederpanzer + Schlagring', Money(5, 0, 0)),
    ('Lederpanzer + Schleuder', Money(4, 1, 0)),
    ('Robe + Kurzschwert', Money(7, 0, 0)),
    ('Kurzschwert + Holzschild', Money(7, 0, 0)),
    ('Breitschwert + Holzschild', Money(8, 0, 0)),
    ('3x Wurfmesser', Money(6, 0, 0)),
    ('Langbogen', Money(10, 0, 0)),
    ('Streithammer', Money(6, 0, 0)),
    ('Kurzschwert + Schleuder', Money(6, 1, 0))
]


def generate_equipment():
    money = Money(10, 0, 0)
    equipment = ['Kleidung', 'Feuerstein + Zunder', 'Wasserschlauch', '2x Heilkraut', 'Decke', 'Rucksack']
    random.shuffle(existing_equipment_sets)
    eset = existing_equipment_sets[0]
    money.subtract_money(eset[1])
    equipment.append(eset[0])
    while money.has_enough():
        random.shuffle(existing_equipment_general)
        if money.subtract_money(existing_equipment_general[0][1]):
            equipment.append(existing_equipment_general[0][0])
    return equipment, money
