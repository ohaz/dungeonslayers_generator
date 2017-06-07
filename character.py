import random
import copy
import crace
import cclass
import os


class Character:

    def __init__(self):

        random.seed()

        # Attribute
        self.attribute = {'Körper': 0, 'Agilität': 0, 'Geist': 0}
        self.koerper = property(lambda: self.attribute['Körper'], lambda: self.attribute['Körper'])
        self.agilitaet = property(lambda: self.attribute['Agilität'], lambda: self.attribute['Agilität'])
        self.geist = property(lambda: self.attribute['Geist'], lambda: self.attribute['Geist'])

        # Eigenschaften
        self.eigenschaften = {'Stärke': 0, 'Härte': 0, 'Bewegung': 0, 'Geschick': 0, 'Verstand': 0, 'Aura': 0}
        #Körper
        self.staerke = property(lambda: self.eigenschaften['Stärke'], lambda: self.eigenschaften['Stärke'])
        self.haerte = property(lambda: self.eigenschaften['Härte'], lambda: self.eigenschaften['Härte'])

        # Agilität
        self.bewegung = property(lambda: self.eigenschaften['Bewegung'], lambda: self.eigenschaften['Bewegung'])
        self.geschick = property(lambda: self.eigenschaften['Geschick'], lambda: self.eigenschaften['Geschick'])

        # Geist
        self.verstand = property(lambda: self.eigenschaften['Verstand'], lambda: self.eigenschaften['Verstand'])
        self.aura = property(lambda: self.eigenschaften['Aura'], lambda: self.eigenschaften['Aura'])

        # Ausrüstung
        self.panzerung = 0
        self.waffenbonus = 0

        # Kampfwerte
        self.lebenskraft = property(lambda: 10 + self.attribute['Körper'] + self.eigenschaften['Härte'])
        self.abwehr = property(lambda: self.attribute['Körper'] + self.eigenschaften['Härte'] + self.panzerung)
        self.initiative = property(lambda: self.attribute['Agilität'] + self.eigenschaften['Bewegung'])
        self.laufen = property(lambda: (self.attribute['Agilität'] * 1.0 / 2.0) + 1)
        self.schlagen = property(lambda: self.attribute['Körper'] + self.eigenschaften['Stärke'] + self.waffenbonus)
        self.schiessen = property(lambda: self.attribute['Agilität'] + self.eigenschaften['Geschick'] + self.waffenbonus)
        self.zaubern = property(lambda: self.attribute['Geist'] + self.eigenschaften['Aura'] - self.panzerung)
        self.zielzauber = property(lambda: self.attribute['Geist'] + self.eigenschaften['Geschick'] - self.panzerung)

        self.klasse = None
        self.volk = None

    def generate_attribute(self):
        punkte = 20
        while (punkte > 0):
            used = 0
            while (not used):
                key = random.choice(list(self.attribute.keys()))
                if (self.attribute[key] < 8):
                    self.attribute[key] += 1
                    used = True
            punkte -= 1

    def generate_eigenschaften(self):
        take_punkte = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        punkte_summe = 0
        current_punkte_liste = []
        while punkte_summe != 8 or len(current_punkte_liste) > 6:
            current_punkte_liste = []
            current_punkte = copy.copy(take_punkte)
            random.shuffle(current_punkte)
            current_sum = 0
            while current_sum < 8:
                c = current_punkte.pop()
                current_punkte_liste.append(c)
                current_sum += c
            punkte_summe = current_sum
        keys = list(self.eigenschaften.keys())
        random.shuffle(keys)
        for wert in current_punkte_liste:
            self.eigenschaften[keys.pop()] = wert

    def generate_klassen_bonus(self):
        self.klasse = cclass.get_random_klasse()
        random.shuffle(self.klasse.bonus)
        self.eigenschaften[self.klasse.bonus[0]] += 1

    def generate_volks_bonus(self):
        self.volk = crace.get_random_volk()
        random.shuffle(self.volk.volksbonus)
        self.eigenschaften[self.volk.volksbonus[0]] += 1

    def generate_talent(self):
        self.klasse.generate_talent()

    def __str__(self):
        result = 'Volk: {} - Klasse: {} --- '.format(self.volk, self.klasse)
        for key, value in self.attribute.items():
            result += '{}: {}, '.format(key, value)
        result += ' || '
        for key, value in self.eigenschaften.items():
            result += '{}: {}, '.format(key, value)
        if isinstance(self.klasse, cclass.Zauberwirker):
            result += os.linesep
            result += 'Zauber: {}'.format(self.klasse.zauber)
        result += os.linesep
        result += 'Lebenskraft: {} Abwehr: {} Initiative: {} Laufen: {} Schlagen: {} + WB Schießen: {} + WB Zaubern: {} - PA Zielzauber: {} - PA'.format(
            self.lebenskraft.fget(), self.abwehr.fget(), self.initiative.fget(), self.laufen.fget(), self.schlagen.fget(), self.schiessen.fget(),
            self.zaubern.fget(), self.zielzauber.fget())
        if self.klasse and self.klasse.talent:
            result += os.linesep
            result += self.klasse.talent
        result += os.linesep + '-------------------------------------------------'
        return result