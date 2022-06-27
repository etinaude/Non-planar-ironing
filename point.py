class Point:
    x = 0.000
    y = 0.000
    z = 0.000
    e = 2.000

    def __init__(self, x, y, z, e):
        self.x = x
        self.y = y
        self.z = z
        self.e = e

    def __str__(self):
        return "G1 X{:.3f} Y{:.3f} Z{:.3f} E{:.3f}".format(self.x, self.y, self.z, self.e)

    def smaller(self, other_point):
        if(self.x < other_point.x):
            return [self, other_point]

        return [other_point, self]