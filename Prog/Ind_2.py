#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import math


class Body(ABC):
    @abstractmethod
    def surface_area(self) -> float:
        """Абстрактный метод для вычисления площади поверхности тела."""
        pass

    @abstractmethod
    def volume(self) -> float:
        """Абстрактный метод для вычисления объема тела."""
        pass

    @abstractmethod
    def display(self) -> None:
        """Абстрактный метод вывода информации о теле."""
        pass


class Parallelepiped(Body):
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self) -> float:
        """Вычисление площади поверхности параллелепипеда."""
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self) -> float:
        """Вычисление объема параллелепипеда."""
        return self.length * self.width * self.height

    def display(self) -> None:
        """Вывод информации о параллелепипеде."""
        print(f"Параллелепипед: длина={self.length}, ширина={self.width}, высота={self.height}")
        print(f"Площадь поверхности: {self.surface_area()} кв.ед., Объем: {self.volume()} куб.ед.")


class Ball(Body):
    def __init__(self, radius: float):
        self.radius = radius

    def surface_area(self) -> float:
        """Вычисление площади поверхности шара."""
        return 4 * math.pi * self.radius ** 2

    def volume(self) -> float:
        """Вычисление объема шара."""
        return (4 / 3) * math.pi * self.radius ** 3

    def display(self) -> None:
        """Вывод информации о шаре."""
        print(f"Шар: радиус={self.radius}")
        print(f"Площадь поверхности: {self.surface_area()} кв.ед., Объем: {self.volume()} куб.ед.")


def show_body_info(body: Body) -> None:
    """Функция вывода, демонстрирующая виртуальный вызов методов базового класса."""
    body.display()


if __name__ == "__main__":
    # Демонстрация работы классов
    parallelepiped = Parallelepiped(3, 4, 5)
    ball = Ball(7)

    # Вызов функции вывода для параллелепипеда
    print("Параллелепипед:")
    show_body_info(parallelepiped)

    print("\nШар:")
    # Вызов функции вывода для шара
    show_body_info(ball)
