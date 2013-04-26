import pyglet
from random import randrange # needed since everything is randomly positioned

screenWidth = 1200
screenHeight = 600

window = pyglet.window.Window(screenWidth, screenHeight, caption="Pheromone")

pyglet.resource.path = ["../res"]
pyglet.resource.reindex()

class Ant(object):
	def __init__(self):
		self.image = pyglet.resource.image("ants/idle.png")
		self.width, self.height = self.image.width, self.image.height
		
		self.x = randrange(home.x-self.width, home.x+home.width)
		self.y = randrange(home.y-self.height, home.y+home.height)
		# Flip if the ant if facing the other way
		if (self.x+self.width/2)<(home.x+home.width/2):
			self.image = pyglet.resource.image("ants/idle.png", flip_x=True)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y, batch=antBatch)

class Debris(object):
	def __init__(self): 
		self.image = pyglet.resource.image("debris/" + str(randrange(1, 3)) + ".png")
		self.width, self.height = self.image.width, self.image.height
		while True:
			self.x = randrange(0, screenWidth - self.width)
			self.y = randrange(0, screenHeight - self.height)
			if (self.x+self.width < home.x or self.x > home.x+home.width):
				break
			elif (self.y+self.height < home.y or self.y > home.y+home.height):
				break

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y, batch=debrisBatch)

class Food(object):
	def __init__(self):
		pass

class Nest(object): 
	def __init__(self):
		self.image = pyglet.resource.image("ants/nest.png") # TODO: Whether to use image or resource here
		self.width, self.height = self.image.width, self.image.height
		
		self.x = randrange(0, screenWidth - self.width)
		self.y = randrange(0, screenHeight - self.height)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
home = Nest()

debrises = []
ants = []

antBatch = pyglet.graphics.Batch()
debrisBatch = pyglet.graphics.Batch()

for i in range(0,8):
	ants.append(Ant())

for i in range(0, 255):
	debrises.append(Debris())

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
	debrisBatch.draw()
	antBatch.draw()

# TODO: move this somewhere else
pyglet.app.run()
