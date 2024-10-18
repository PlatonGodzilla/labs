class circle():
    def __init__(self,radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius

print(circle(5).get_radius())
test = circle(5)
print(test.get_radius())
test.set_radius(10)
print(test.get_radius())