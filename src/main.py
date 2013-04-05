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
		super(AnimateDrawable, self).__init(self, x, y)
		self.animation = animation

class InanimateDrawable(Drawable):
	def __init__(self, image, x, y):
		super(InanimateDrawable, self).__init(self, x, y)
		self.image = image


class Ant(AnimateDrawable):
	def __init__(self, x, y):
		super(Ant, self).__init__(self, animation, x, y)

class Debris(InanimateDrawable):
	def __init__(self, x, y): 
		super(Debris, self).__init__(self, image, x, y)

class Food(InanimateDrawable):
	def __init__(self, x, y):
		super(Food, self).__init__(self, image, x, y)

class Nest(InanimateDrawable): 
	def __init__(self):
		# The Nest image can't be outside the screen. The Nest graphics will be made soon.
		# x = randrange(0, screenWidth - baseWidth)
		# y = randrange(0, screenHeight - baseHeight)

		super(Nest, self).__init__(self, image, x, y)


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
