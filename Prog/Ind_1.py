#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Liquid:
    def __init__(self, name: str, density: float):
        self.name = name
        self.density = density

    def set_name(self, new_name: str):
        """Изменить название жидкости."""
        self.name = new_name

    def set_density(self, new_density: float):
        """Изменить плотность жидкости."""
        if new_density > 0:
            self.density = new_density
        else:
            raise ValueError("Плотность должна быть положительным числом.")

    def __str__(self):
        return f"Жидкость: название={self.name}, плотность={self.density} кг/м³"


class Alcohol(Liquid):
    def __init__(self, name: str, density: float, strength: float):
        super().__init__(name, density)
        self.strength = strength

    def set_strength(self, new_strength: float):
        """Изменить крепость спирта."""
        if 0 <= new_strength <= 100:
            self.strength = new_strength
        else:
            raise ValueError("Крепость должна быть в диапазоне от 0 до 100.")

    def __str__(self):
        return (f"Спирт: название={self.name}, плотность={self.density} кг/м³, "
                f"крепость={self.strength}%")


if __name__ == "__main__":
    # Демонстрация возможностей классов
    # Создаем экземпляр Liquid
    water = Liquid("Вода", 997)
    print(water)  # Жидкость: название=Вода, плотность=997 кг/м³

    # Меняем название и плотность
    water.set_name("Дистиллированная вода")
    water.set_density(998)
    print(water)  # Жидкость: название=Дистиллированная вода, плотность=998 кг/м³

    # Создаем экземпляр Alcohol
    ethanol = Alcohol("Этанол", 789, 95)
    print(ethanol)  # Спирт: название=Этанол, плотность=789 кг/м³, крепость=95%

    # Меняем крепость спирта
    ethanol.set_strength(70)
    print(ethanol)  # Спирт: название=Этанол, плотность=789 кг/м³, крепость=70%
