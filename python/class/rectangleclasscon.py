# DEMO

# _width and _height are private variables and should noty be modified and we can only talk to it 
# through getter and setter meothods

class Rectangle:
    def __init__(self, width,height):
         self._width = width
         self._height = height


#getter and setter method is releavant cos it adds logic to the input.


    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width


# calling the to_string methon 
    def to_sting(self):
        return 'Rectangle: width={0},hieght={1}'.format(self._width,self._height)

# we can also call the  magic method like this

    def __str__(self):
        return 'Rectangle: width={0},hieght={1}'.format(self._width,self._height)

    def __repr__(self):
        return 'Rectangle({0},{1})'.format(self._width,self._height)

# implemeteing the comparism method of this class of rectangle to show that  two rectangle can be equal

    def __eq__(self, other):
      if isinstance(other, Rectangle):
        return self._width == other._width and self._height == other._height

      else:
        return False


  
# Pythonic way of applying gethher and setter       


### the call of this class methods
r1 =  Rectangle(10,20)
r2 =  Rectangle(10,20)
r3 =  Rectangle(100,400)
r4 =  Rectangle(1000,500)




value = r1.get_width()
print(value)
print("------- answer 3------")
print(r1.to_sting())
print("------- answer 4------")
print(str(r1))
print("------- answer 5------")
print(r1) # still not working
print("------- answer 6------")
print (r1 == r2)
print(r1 == 100)
print (r1 is not r2)
print("------- answer 6------")
print("------- answer 8 using getter and setter------")

