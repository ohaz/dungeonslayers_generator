# -*- coding: utf-8 -*-
import random


class Klasse:

    def __init__(self):
        self.bonus = []
        self.name = ''
        self.talents = ['Ausweichen', 'Bildung', 'Charmant', 'Diener der Dunkelheit', 'Diener des Lichts', 'Einstecker', 'Genesung',
        'Glückspilz', 'Handwerk', 'Instrument', 'Magieresistent', 'Reiten', 'Schlitzohr', 'Schnelle Reflexe', 'Schwimmen', 'Wahrnehmung', 'Wissensgebiet']
        self.talent = None

    def generate_talent(self):
        random.shuffle(self.talents)
        self.talent = self.talents.pop()

    def __str__(self):
        return self.name


class Krieger(Klasse):

    def __init__(self):
        super(Krieger, self).__init__()
        self.bonus = ['Stärke', 'Härte']
        self.name = 'Krieger'
        self.talents.extend(['Blocker', 'Kämpfer', 'Parade', 'Standhaft', 'Zwei Waffen'])


class Spaeher(Klasse):

    def __init__(self):
        super(Spaeher, self).__init__()
        self.bonus = ['Bewegung', 'Geschick']
        self.name = 'Späher'
        self.talents.extend(['Akrobat', 'Diebeskunst', 'Flink', 'Heimlichkeit', 'Jäger', 'Schütze'])


class Zauberwirker(Klasse):

    def __init__(self):
        super(Zauberwirker, self).__init__()
        self.bonus = ['Verstand', 'Aura']
        self.name = 'Zauberwirker'
        self.zauber = self.first_spell()
        self.talents.extend(['Alchemie', 'Runenkunde', 'Umdenken', 'Wechsler'])

    def first_spell(self):
        return None


class Heiler(Zauberwirker):

    def __init__(self):
        super(Heiler, self).__init__()
        self.name = 'Heiler'
        self.talents.extend(['Fürsorger', 'Manipulator', 'Rüstzauberer'])

    def first_spell(self):
        spells = ['Blenden', 'Giftschutz', 'Heilbeeren', 'Heilende Aura', 'Heilende Hand', 'Licht', 'Magie entdecken', 'Magische Waffe',
             'Niesanfall', 'Tiere besänftigen', 'Verteidigung', 'Vertreiben', 'Wasser weihen']
        random.shuffle(spells)
        return spells.pop()


class Zauberer(Zauberwirker):

    def __init__(self):
        super(Zauberer, self).__init__()
        self.name = 'Zauberer'

    def first_spell(self):
        spells = ['Duftnote', 'Feuerstrahl', 'Licht', 'Magie entdecken/identifizieren', 'Magische Waffe', 'Magisches Schloss', 'Öffnen', 'Zaubertrick']
        random.shuffle(spells)
        return spells.pop()


class Schwarzmagier(Zauberwirker):

    def __init__(self):
        super(Schwarzmagier, self).__init__()
        self.name = 'Schwarzmagier'
        self.talents.extend(['Feuermagier'])

    def first_spell(self):
        spells = ['Feuerstrahl', 'Magie entdecken/identifizieren', 'Magische Waffe', 'Magisches Schloss', 'Öffnen', 'Zaubertrick']
        random.shuffle(spells)
        return spells.pop()


def get_random_klasse():
    klassen = [Krieger, Spaeher, Zauberwirker]
    subklassen = [Heiler, Zauberer, Schwarzmagier]

    random.shuffle(klassen)
    random.shuffle(subklassen)
    klasse = klassen.pop()
    if klasse == Zauberwirker:
        klasse = subklassen.pop()
    return klasse()