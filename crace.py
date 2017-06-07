# -*- coding: utf-8 -*-
import random


class Volk:

    def __init__(self):
        self.faehigkeiten = []
        self.volksbonus = []
        self.name = ''

    def __str__(self):
        return self.name


class Elf(Volk):

    def __init__(self):
        super(Elf, self).__init__()
        self.faehigkeiten = ['Leichtfüßig (Schleichen +2)', 'Nachtsicht', 'Unsterblich']
        self.volksbonus = ['Bewegung', 'Geschick', 'Aura']
        self.name = 'Elf'


class Mensch(Volk):

    def __init__(self):
        super(Mensch, self).__init__()
        self.faehigigkeiten = ['+1 Talentpunkte']
        self.volksbonus = ['Stärke', 'Härte', 'Bewegung', 'Geschick', 'Verstand', 'Aura']
        self.name = 'Mensch'


class Zwerg(Volk):

    def __init__(self):
        super(Zwerg, self).__init__()
        self.faehigkeiten = ['Dunkelsicht', 'Langlebig', 'Zäh (+1 Abwehr)']
        self.volksbonus = ['Stärke', 'Härte', 'Geschick']
        self.name = 'Zwerg'


def get_random_volk():
    voelker = [Elf, Mensch, Zwerg]
    random.shuffle(voelker)
    return (voelker.pop())()