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
    
class Line2D:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2
    
    def set_vector1(self, vector1) : # 캡슐화를 위한 setter
        if type(vector1) is Vector2D:
            self.vector1 = vector1
        
    def set_vector2(self, vector2) :
        if type(vector2) is Vector2D:
            self.vector2 = vector2
    
    def __str__(self):
        return f'({self.vector1.x},{self.vector1.y}) - ({self.vector2.x},{self.vector2.y})'
    
    def __eq__(self,other):
        if type(other) is Line2D:
            return self.vector1 == other.vector1 and self.vector2 == other.vector2
        else:
            return False
    
    def __len__(self):
        return (int)(((self.vector1.x - self.vector2.x)**2 + (self.vector1.y - self.vector2.y)**2)**0.5)
    
    def __lt__(self, other):
        if isinstance(other, Line2D):
            return len(self) < len(other)

    def __le__(self, other):
        if isinstance(other, Line2D):
            return len(self) <= len(other)

    def __gt__(self, other):
        if isinstance(other, Line2D):
            return len(self) > len(other)

    def __ge__(self, other):
        if isinstance(other, Line2D):
            return len(self) >= len(other)


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

l1 = Line2D(v1,v2)
print(l1)
print(f"{l1} == {Line2D(v1,v2)} = {l1 == Line2D(v1,v2)}")
print(f"length of {l1} = {len(l1)}")
print(f"{l1} < {Line2D(v1,v1)} = {l1 < Line2D(v1,v1)}")
print(f"{l1} <= {Line2D(v1,v1)} = {l1 <= Line2D(v1,v1)}")
print(f"{l1} > {Line2D(v1,v1)} = {l1 > Line2D(v1,v1)}")
print(f"{l1} >= {Line2D(v1,v1)} = {l1 >= Line2D(v1,v1)}")
print("20225122 김상훈")