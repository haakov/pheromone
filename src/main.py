import pyglet
import random # needed since everything is randomly positioned
from pyglet.gl import *
import time # for time.sleep()
import math
import pdb

screenWidth = 1200
screenHeight = 600

window = pyglet.window.Window(screenWidth, screenHeight, caption="Pheromone")

pyglet.resource.path = ["../res"]
pyglet.resource.reindex()

class Cloud(object):
	def __init__(self):
		self.image = pyglet.resource.image("intro/cloud.png")
		# Don't need to care about width and height

		self.x = random.randrange(-50, 1150)
		self.y = random.randrange(-50, 550)

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
		self.image = pyglet.resource.image("ants/topdown.png")
		self.width, self.height = self.image.width, self.image.height

		self.plus_x = 0.0 
		self.plus_y = 0.0
		self.plus_rotation = 0.0

		self.x = random.randrange(home.x-self.width, home.x+home.width)
		self.y = random.randrange(home.y-self.height, home.y+home.height)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y, batch=antBatch)
		self.sprite.image.anchor_x = self.width / 2
		self.sprite.image.anchor_y = self.height / 2

class Food(object):
	def __init__(self):
		pass

class Nest(object): 
	def __init__(self):
		self.image = pyglet.resource.image("ants/nest.png") 
		self.width, self.height = self.image.width, self.image.height
		
		self.x = random.randrange(0, screenWidth - self.width)
		self.y = random.randrange(0, screenHeight - self.height)

		self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y)
home = Nest()

ants = []
clouds = []
title = Title()

antBatch = pyglet.graphics.Batch()
cloudBatch = pyglet.graphics.Batch()

for i in range(0, 8):
	ants.append(Ant())

for i in range(0, 4):
	clouds.append(Cloud())

def introScene(dt):
	title.sprite.y -= title.dy * dt
	
	glClearColor(0.396, 0.745, 1.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	
	cloudBatch.draw()
	title.sprite.draw()

	if (title.sprite.y+title.sprite.height/2 < screenHeight/2):
		window.flip()
		time.sleep(1)
		
		pyglet.clock.unschedule(introScene)
		pyglet.clock.schedule_interval(mainScene, 1/10.0)

def mainScene(dt):
	glClearColor(0.612, 0.286, 0.023, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	for i in range(0, 8):
		ants[i].plus_x = float(random.randint(-25, 25))
		while ants[i].plus_x == 0:
			ants[i].plus_x = float(random.randint(-25, 25))

		ants[i].plus_y = float(random.randint(-25, 25))
		while ants[i].plus_y == 0:
			ants[i].plus_y = float(random.randint(-25, 25))

		ants[i].plus_rotation = math.degrees(math.atan(ants[i].plus_x/ants[i].plus_y))
		
		if(ants[i].plus_y < 0):
			ants[i].plus_rotation += 180.0

		ants[i].sprite.rotation = ants[i].plus_rotation
		ants[i].sprite.x += ants[i].plus_x
		ants[i].sprite.y += ants[i].plus_y

		if ants[i].sprite.x < 0:
			ants[i].sprite.x = 0
		if ants[i].sprite.y < 0:
			ants[i].sprite.y = 0

		if ants[i].sprite.x - ants[i].sprite.width < 0:
			ants[i].sprite.x = 0 + ants[i].sprite.width
		if ants[i].sprite.y - ants[i].sprite.width < 0:
			ants[i].sprite.y = 0 + ants[i].sprite.width

		if ants[i].sprite.x + ants[i].sprite.width > screenWidth:
			ants[i].sprite.x = screenWidth - ants[i].sprite.width
		if ants[i].sprite.y + ants[i].sprite.height > screenHeight:
			ants[i].sprite.y = screenHeight - ants[i].sprite.width
		

	home.sprite.draw()
	antBatch.draw()

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
