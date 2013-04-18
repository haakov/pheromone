import pyglet
from random import randrange # needed since everything is randomly positioned

screenWidth = 1200
screenHeight = 600

window = pyglet.window.Window(screenWidth, screenHeight, caption="Pheromone")

pyglet.resource.path = ["../res"]
pyglet.resource.reindex()

class Ant(object):
	def __init__(self):
		pass

class Debris(object):
	def __init__(self): 
		self.image = pyglet.image.load("res/debris/" + str(randrange(1, 3)) + ".png")
		self.width, self.height = self.image.width, self.image.height

		self.x = randrange(0, screenWidth - self.width)
		self.y = randrange(0, screenHeight - self.height)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y)

class Food(object):
	def __init__(self):
		pass

class Nest(object): 
	def __init__(self):
		self.image = pyglet.image.load("res/ants/nest.png") # TODO: Whether to use image or resource here
		self.width, self.height = self.image.width, self.image.height
		
		self.x = randrange(0, screenWidth - self.width)
		self.y = randrange(0, screenHeight - self.height)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
home = Nest()
debris = Debris()
debris1 = Debris()
debris2 = Debris()
debris3 = Debris()
debris4 = Debris()

@window.event
def update(self):
	pass


def main():
	print "Welcome to Pheromone!"
	print "Pheromone is an ant colony simulator."



if __name__ == "__main__":
	main()

@window.event
def on_draw():
	window.clear()
	home.sprite.draw()
	debris.sprite.draw()
	debris1.sprite.draw()
	debris2.sprite.draw()
	debris3.sprite.draw()
	debris4.sprite.draw()
# TODO: move this somewhere else
pyglet.app.run()
