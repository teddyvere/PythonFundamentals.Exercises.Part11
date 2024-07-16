from shapes import Rectangle, Square

def test_rectangle_class():
    rectangle = Rectangle(5, 10)
    assert rectangle.area() == 50
    assert rectangle.perimeter() == 30
    
def test_square_class():
    square = Square(7)
    assert square.area() == 49
    assert square.perimeter() == 28