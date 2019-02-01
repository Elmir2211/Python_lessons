# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math
class Treugolnik:
    def __init__(self, A, B, C):
        # Функция вычисляет длину стороны согласно координатам точек
        def storona(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        # На основании соседних координат вычисляем длину стороны AB
        self.AB = storona(self.A, self.B)
        self.BC = storona(self.B, self.C)
        self.CA = storona(self.C, self.A)

    # Вычисление площади треугольника по формуле Герона
    def plothad(self):
        semi_perimeter = self.perimeter() / 2

        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.AB)
                         * (semi_perimeter - self.BC)
                         * (semi_perimeter - self.CA))

    # вычисляем периметр треугольника
    def perimeter(self):
        return self.AB + self.BC + self.CA

    # Вычисляем высоту треугольника
    def visota(self):
        return self.plothad() / (self.AB / 2)


treugolnik1 = Treugolnik((4, 3), (7, 8), (1, 13))

print('Площадь треугольника:',treugolnik1.plothad())
print('Высота треугольника:',treugolnik1.visota())
print('Периметр треугольника:',treugolnik1.perimeter())

########################################################################################################################
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class Trapezia:
    def __init__(self, A, B, C, D):
        # Функция вычисляет длину стороны согласно координатам точек
        def storona(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        def plothad_treugolnika(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2

            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = storona(self.A, self.B)
        self.BC = storona(self.B, self.C)
        self.CD = storona(self.C, self.D)
        self.DA = storona(self.D, self.A)
        self.diagonal_AC = storona(self.C, self.A)
        self.diagonal_BD = storona(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA

        # представим трапецию как 2 треугольника и сложим 2 площади этих треугольников
        # Для этого у нас есть все необходимые длины сторон
        self.plothad_trapezi = plothad_treugolnika(self.AB, self.diagonal_BD, self.DA) \
                    + plothad_treugolnika(self.diagonal_BD, self.BC, self.CD)

    def ravnobothnaya(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False

trapezia1=Trapezia((1,3),(7,10),(15,10),(20,3))
print('Длина стороны AB:',trapezia1.AB)
print('Длина стороны BC:',trapezia1.BC)
print('Длина стороны CD:',trapezia1.CD)
print('Длина стороны DA:',trapezia1.DA)
print('Периметр трапеции равна:',trapezia1.perimeter)
print('Площадь трапеции равна:',trapezia1.plothad_trapezi)
print('Является ли трапеция равнобочной? :',trapezia1.ravnobothnaya())