import math


class Calculator():
    def __init__(self):
        self.radom = 0

    def density(self, mass, volume):
        self.mass = mass
        self.volume = volume

        print(self.mass / self.volume)

    def mass(self, density, volume):
        self.density = density
        self.volume = volume

        print(self.density * self.volume)

    def volume(self, density, mass):
        self.mass = mass
        self.density = density
        print(self.mass / self.density)

    def distance(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.random = math.sqrt((self.x1 - self.x2) * (self.x1 - self.x2) + (self.y1 - self.y2) * (self.y1 - self.y2))
        print(self.random)

    def rtd(self, rad):
        return rad * 180 / math.pi

    def dtr(self, degree):
        return degree * math.pi / 180

    def integral(self):
        pass

    def avertex(self, y, k, x, h):
        self.y = y
        self.k = k
        self.x = x
        self.h = h
        return (self.y - self.k) / ((self.x - self.h) ** 2)

    def fft(self):
        pass
