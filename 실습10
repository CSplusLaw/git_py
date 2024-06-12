class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    
    def __eq__(self, other):
        if type(other) is Vector2D:
            return self.x == other.x and self.y == other.y
        else:
            return False
    def __neg__(self):
        return Vector2D(-self.x, -self.y)

v1 = Vector2D(10,20)
v2 = Vector2D(2,5)
print(f"{v1} + {v2} = {v1 + v2}")
print(f"{v1} - {v2} = {v1 - v2}")
print(f"{v1} * {v2} = {v1 * v2}")
print(f"{v1} / {v2} = {v1 / v2}")
print(f"-{v1} = {-v1}")
print(f"{v1} == {v2} = {v1 == v2}")
print(f"{v1} == {v1} = {v1 == v1}")
print(f"{v1} == 10 = {v1 == 10}")
print("20225122 김상훈")