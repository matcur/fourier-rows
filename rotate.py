import math
from matplotlib import pyplot as plt


class Vector:
    def __init__(self, start, length, angle):
        self.start = start
        self.length = length
        self.angle = angle

    def get_start(self):
        return self.start

    def get_end(self):
        radiant = to_radiant(self.angle)
        x = self.start[0] + math.cos(radiant) * self.length
        y = self.start[1] + math.sin(radiant) * self.length

        return [x, y]

    def angle(self):
        return self.angle

    def rotate(self, angle):
        return Vector(self.start, self.length, self.angle + angle)


def to_radiant(angle):
    return angle / 180 * math.pi


length = 3
angle = 10
vector1 = Vector([0, 0], length, angle)
vector2 = vector1.rotate(90)
vectors = [vector1, vector2]
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()

for vector in vectors:
    start = vector.get_start()
    end = vector.get_end()

    ax.plot([start[0], end[0]], [start[1], end[1]])

circle = plt.Circle((0, 0), length, fill=False, color='green')
ax.add_artist(circle)

plt.ylim([-length, length])
plt.xlim([-length, length])
plt.grid()
plt.show()
