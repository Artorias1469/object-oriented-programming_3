#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import math


class Unit:
    def __init__(self, unit_id, team):
        self.unit_id = unit_id
        self.team = team

class Hero(Unit):
    def __init__(self, hero_id, team):
        super().__init__(hero_id, team)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Герой {self.unit_id} увеличил уровень до {self.level}.")


class Soldier(Unit):
    def follow_hero(self, hero):
        print(f"Солдат {self.unit_id} идет за героем {hero.unit_id}.")


def main():
    hero_team_a = Hero(hero_id=1, team="A")
    hero_team_b = Hero(hero_id=2, team="B")

    soldiers_team_a = []
    soldiers_team_b = []

    for i in range(10):
        soldier_id = i + 1
        team = random.choice(["A", "B"])

        if team == "A":
            soldiers_team_a.append(Soldier(soldier_id, team))
        else:
            soldiers_team_b.append(Soldier(soldier_id, team))

    length_a = len(soldiers_team_a)
    length_b = len(soldiers_team_b)

    print(f"Количество солдат в команде A: {length_a}")
    print(f"Количество солдат в команде B: {length_b}")

    if length_a > length_b:
        hero_team_a.level_up()
    else:
        hero_team_b.level_up()

    if soldiers_team_a:
        soldiers_team_a[0].follow_hero(hero_team_a)
        print(f"Идентификационный номер солдата: {soldiers_team_a[0].unit_id}")
        print(f"Идентификационный номер героя: {hero_team_a.unit_id}")


if __name__ == "__main__":
    main()