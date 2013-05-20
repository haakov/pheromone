import pyglet
from random import randrange # needed since everything is randomly positioned
from pyglet.gl import *

screenWidth = 1200
screenHeight = 600

window = pyglet.window.Window(screenWidth, screenHeight, caption="Pheromone")

pyglet.resource.path = ["../res"]
pyglet.resource.reindex()

class Cloud(object):
	def __init__(self):
		self.image = pyglet.resource.image("intro/cloud.png")
		# Don't need to care about width and height

		self.x = randrange(-50, 1150)
		self.y = randrange(-50, 550)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y, batch=cloudBatch)

class Title(object):
	def __init__(self):
		# Ubuntu font
		self.image = pyglet.resource.image("intro/title.png")
		self.width, self.height = self.image.width, self.image.height

		self.sprite = pyglet.sprite.Sprite(self.image, screenWidth/2-self.width/2, 1.5*screenHeight)

		self.dy = 1500.0

class Ant(object):
	def __init__(self):
		self.image = pyglet.resource.image("ants/topdown.png", rotate=270)
		self.width, self.height = self.image.width, self.image.height
		
		self.x = randrange(home.x-self.width, home.x+home.width)
		self.y = randrange(home.y-self.height, home.y+home.height)
		# Flip if the ant if facing the other way
		if (self.x+self.width/2)>(home.x+home.width/2):
			self.image = pyglet.resource.image("ants/topdown.png", rotate=90)

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
		self.image = pyglet.resource.image("ants/nest.png") 
		self.width, self.height = self.image.width, self.image.height
		
		self.x = randrange(0, screenWidth - self.width)
		self.y = randrange(0, screenHeight - self.height)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
home = Nest()

debrises = []
ants = []
clouds = []
title = Title()

antBatch = pyglet.graphics.Batch()
debrisBatch = pyglet.graphics.Batch()
cloudBatch = pyglet.graphics.Batch()

for i in range(0,8):
	ants.append(Ant())

for i in range(0, 255):
	debrises.append(Debris())

for i in range(0, 4):
	clouds.append(Cloud())

def introScene(dt):
	title.sprite.y -= title.dy * dt
	if (title.sprite.y+title.sprite.height/2 < screenHeight/2):
		pyglet.clock.unschedule(introScene)
	glClearColor(0.396, 0.745, 1.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	cloudBatch.draw()
	title.sprite.draw()

pyglet.clock.schedule_interval(introScene, 1/60.0)

def main():
	print "Welcome to Pheromone!"
	print "Pheromone is an ant colony simulator."
	# The following is here to avoid ugliness/artifacts on the very first frame
	glClearColor(0.396, 0.745, 1.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)



if __name__ == "__main__":
	main()

@window.event
def on_draw():
	pass

# TODO: move this somewhere else
pyglet.app.run()
