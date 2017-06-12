# -*- coding: utf-8 -*-

from character import Character

c = Character()
print('Start:', c)
c.generate_attribute()
print('Post Attributes:', c)
c.generate_eigenschaften()
print('Post Eigenschaften:', c)
c.generate_klassen_bonus()
print('Post Klasse:', c)
c.generate_volks_bonus()
print('Post Volk:', c)
c.generate_talent()
print('Post Talent:', c)
c.generate_equipment()
print('Equipment:', c)
