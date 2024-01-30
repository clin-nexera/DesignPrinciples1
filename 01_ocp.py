# QUESTION: What happens when we add another shape?   

class Circle():
    radius: float

class Square():
    length: float


PI = 3.14
class AreaCalculator():
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            return shape.radius** 2 * PI
        elif isinstance(shape, Square):
            return shape.length ** 2
        else:
            -1



### Notes ###
    # We'll have to add another elif branch
    
# Suggested Solution
from abc import ABCMeta, abstractmethod

class ShapeInterface(metaclass=ABCMeta):

    @abstractmethod
    def area() -> float:
        raise NotImplementedError()
    

class Circle(ShapeInterface):
    radius: float

    def area(self) -> float:
        return self.radius ** 2 * PI
    

class Square(ShapeInterface):
    length: float

    def area(self) -> float:
        return self.length ** 2
    

class AreaCalculator():
    def calculate_area(self, shape: ShapeInterface):
        return shape.area()
    


    
