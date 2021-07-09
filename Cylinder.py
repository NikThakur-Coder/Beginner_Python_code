class Cylinder:
    pi=3.14

    def __init__(self, height, radius):
        self.height=height
        self.radius=radius

    def volume(self):
        return Cylinder.pi*(self.radius)**2*self.height

    def surface_area(self):
        return (2*Cylinder.pi*self.radius*self.height)+(2*Cylinder.pi*self.radius**2)

height=int(input('Please enter the height: '))
radius=int(input('Please enter the radius: '))
c=Cylinder(height, radius)
print(c.volume())
print(c.surface_area())

