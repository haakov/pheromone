import pyglet
from random import randrange # needed since everything is randomly positioned

screenWidth = 1200
screenHeight = 600

window = pyglet.window.Window(screenWidth, screenHeight, caption="Pheromone")
window.clear()

pyglet.resource.path = ["../res"]
pyglet.resource.reindex()

class Drawable(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


class AnimateDrawable(Drawable):
	def __init__(self, animation, x, y):
		super(AnimateDrawable, self).__init__(x, y)
		self.animation = animation

class InanimateDrawable(Drawable):
	def __init__(self, image, x, y):
		super(InanimateDrawable, self).__init__(x, y)
		self.image = image


class Ant(AnimateDrawable):
	def __init__(self, x, y):
		super(Ant, self).__init__(animation, x, y)

class Debris(InanimateDrawable):
	def __init__(self, x, y): 
		super(Debris, self).__init__(image, x, y)

class Food(InanimateDrawable):
	def __init__(self, x, y):
		super(Food, self).__init__(image, x, y)

class Nest(InanimateDrawable): 
	def __init__(self):
		self.image = pyglet.image.load("res/ants/nest.png") # TODO: Whether to use image or resource here
		self.width, self.height = self.image.width, self.image.height
		
		self.x = randrange(0, screenWidth - self.width)
		self.y = randrange(0, screenHeight - self.height)
		print self.x, self.y

		super(Nest, self).__init__(self.image, self.x, self.y)


@window.event
def update(self):
	pass

def main():
	print "Welcome to Pheromone!"
	print "Pheromone is an ant colony simulator."

	home = Nest()


if __name__ == "__main__":
	main()


# TODO: move this somewhere else
pyglet.app.run()
