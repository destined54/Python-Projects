
class Circle(object):
	pi = 3.14

#attributes

	def __init__(self, radius):
		self.radius = radius
	
#methods
	def circumference(self):
		pi = 3.14
		circumference = 2 * pi * self.radius
		return circumference
	
	def area(self):
		pi = 3.14
		area = pi * self.radius ** 2
		return area
		
small = Circle(3)
medium = Circle(50)                       

print(small.circumference())
print(medium.area())