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
    
    def distance(self, other):
        return (int)(((self.x - other.x)**2 + (self.y - other.y)**2)**0.5)

    
class Line2D:
    def __init__(self, vector1, vector2):
        self.__vector1 = vector1
        self.__vector2 = vector2
    
    def set_vector1(self, vector1) : # 캡슐화를 위한 setter
        if type(vector1) is Vector2D:
            self.vector1 = vector1
        
    def set_vector2(self, vector2) :
        if type(vector2) is Vector2D:
            self.vector2 = vector2
    
    def __str__(self):
        return f'({self.__vector1.x},{self.__vector1.y}) - ({self.__vector2.x},{self.__vector2.y})'
    
    def __eq__(self,other):
        if type(other) is Line2D:
            return self.__vector1 == other.__vector1 and self.__vector2 == other.__vector2
        else:
            return False
    
    def __len__(self):
        return (int)(((self.__vector1.x - self.__vector2.x)**2 + (self.__vector1.y - self.__vector2.y)**2)**0.5)
    
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
print(f"{v1.distance(v2)}")

l1 = Line2D(v1,v2)
print(l1)
print(f"{l1} == {Line2D(v1,v2)} = {l1 == Line2D(v1,v2)}")
print(f"length of {l1} = {len(l1)}")
print(f"{l1} < {Line2D(v1,v1)} = {l1 < Line2D(v1,v1)}")
print(f"{l1} <= {Line2D(v1,v1)} = {l1 <= Line2D(v1,v1)}")
print(f"{l1} > {Line2D(v1,v1)} = {l1 > Line2D(v1,v1)}")
print(f"{l1} >= {Line2D(v1,v1)} = {l1 >= Line2D(v1,v1)}")
print("20225122 김상훈")