# Class is a callection of callable method that are related in an object oriented programming language 
# for example in a Rectangle demo event that can happen to a rectangle could be  finding the Area and perimetr of the rectange

# DEMO
class Rectangle:
    def __init__(self, width,height):
         self.width = width
         self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
# calling the to_string methon 
    def to_sting(self):
        return 'Rectangle: width={0},hieght={1}'.format(self.width,self.height)

# we can also call the  magic method like this

    def __str__(self):
        return 'Rectangle: width={0},hieght={1}'.format(self.width,self.height)

    def __repr__(self):
        return 'Rectangle({0},{1})'.format(self.width,self.height)

# implemeteing the comparism method of this class of rectangle to show that  two rectangle can be equal

    def __eq__(self, other):
      if isinstance(other, Rectangle):
        return self.width == other.width and self.height == other.height

      else:
        return False


    def __lt__(self,other):
        if isinstance(other, Rectangle):
            return  self.area() < other.area()
        else:
            return NotImplemented

    def __gt__(self,other):
        if isinstance(other,Rectangle):
            return self.perimeter() > other.perimeter()
        else:
            return NotImplemented
        


### the call of this class methods
r1 =  Rectangle(10,20)
r2 =  Rectangle(10,20)
r3 =  Rectangle(100,400)
r4 =  Rectangle(1000,500)
print(r1.area())
print("------- answer 2------")
print(r1.perimeter())
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
print (r1 < r3)
print (r2 < r1)
print("------- answer 7------")
print (r1 < r3)
print (r2 < r1)
print (r2 < r4)
print (r4 < r1)
