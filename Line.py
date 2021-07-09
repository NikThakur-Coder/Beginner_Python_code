class Line:
    def __init__(self, cordi_1, cordi_2):
        self.cordi_1 = cordi_1
        self.cordi_2 = cordi_2

    def distance(self):
        return ((cordi_2[0] - cordi_1[0]) ** 2 + (cordi_2[1] - cordi_1[1]) ** 2) ** 0.5

        # return ((other.x-self.x)**2+(other.y-self.y)**2)**0.5
    def slope(self):
        return (int(cordi_2[1]) - int(cordi_1[1])) / (int(cordi_2[0]) - int(cordi_1[0]))

a = input('Please enter coordinate for starting point of line: ')
b = input('Please enter coordinate for ending point of line: ')
cordi_1 = tuple(int(x) for x in a.split())
cordi_2 = tuple(int(x) for x in b.split())
li = Line(cordi_1, cordi_2)
print(li.distance())
print(li.slope())