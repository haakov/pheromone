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

def project(u, v):
	quotient = float(u[0] * v[0] + u[1] * v[1])
	quotient /= float(v[0]**2 + v[1]**2)
	return quotient * v[0], quotient * v[1]
			
class Drawable(object):
	def __init__(self):
		pass

	def get_x(self):
		return self.sprite.x
	def get_y(self):
		return self.sprite.y
	def get_width(self):
		return self.sprite.width
	def get_height(self):
		return self.sprite.height
	def get_rotation(self):
		return self.sprite.rotation

	def set_x(self, x):
		self.sprite.x = x
	def set_y(self, y):
		self.sprite.y = y
	def set_rotation(self, rotation):
		self.sprite.rotation = rotation

	def get_rotated_vertex(self, x, y):
		rotated_x = float((x - self.sprite.x) * math.cos(self.sprite.rotation) - (y - self.sprite.y) * math.sin(self.sprite.rotation) + self.sprite.x)
		rotated_y = float((x - self.sprite.x) * math.sin(self.sprite.rotation) + (y - self.sprite.y) * math.cos(self.sprite.rotation) + self.sprite.y)
		return rotated_x, rotated_y

	def get_vertices(self):
		bottom_left = ((self.get_x() - self.get_width() / 2), (self.get_y() - self.get_height() / 2))
		bottom_right = ((self.get_x() + self.get_width() / 2), (self.get_y() - self.get_height() / 2))
		top_left = ((self.get_x() - self.get_width() / 2), (self.get_y() + self.get_height() / 2))
		top_right = ((self.get_x() + self.get_width() / 2), (self.get_y() + self.get_height() / 2))

		bottom_left = self.get_rotated_vertex(*bottom_left)
		bottom_right = self.get_rotated_vertex(*bottom_right)
		top_left = self.get_rotated_vertex(*top_left)
		top_right = self.get_rotated_vertex(*top_right)

		self.vertices = [bottom_left, bottom_right, top_left, top_right]

	def get_axes(self):
		return [(self.vertices[1][0] - self.vertices[0][0], self.vertices[1][1] - self.vertices[0][1]), (self.vertices[3][0] - self.vertices[1][0], self.vertices[3][1] - self.vertices[1][1])]

	def collides_with(self, other):
		self.get_vertices()
		other.get_vertices()
		self.axes = self.get_axes()
		other.axes = other.get_axes()

		self.projected_vertices = []
		other.projected_vertices = []
		for i in range(0,4):
			self.projected_vertices.append(project(self.vertices[i], self.axes[0]))
			other.projected_vertices.append(project(other.vertices[i], self.axes[0]))		
		for i in range(4,8):
			self.projected_vertices.append(project(self.vertices[i], self.axes[1]))
			other.projected_vertices.append(project(other.vertices[i], self.axes[1]))
		
		
		

class Cloud(Drawable):
	def __init__(self):
		self.image = pyglet.resource.image("intro/cloud.png")
		# Don't need to care about width and height

		self.x = random.randrange(-50, 1150)
		self.y = random.randrange(-50, 550)

		self.sprite = pyglet.sprite.Sprite(self.image, random.randrange(-50, 1150), random.randrange(-50, 550), batch=cloudBatch)

class Title(Drawable):
	def __init__(self):
		# Ubuntu font
		self.image = pyglet.resource.image("intro/title.png")

		self.sprite = pyglet.sprite.Sprite(self.image, screenWidth/2-self.image.width/2, 1.5*screenHeight)

		self.dy = 1500.0

class Ant(Drawable):
	def __init__(self):
		self.image = pyglet.resource.image("ants/topdown.png")

		self.plus_x = None 
		self.plus_y = None
		self.plus_rotation = None

		self.sprite = pyglet.sprite.Sprite(self.image, random.randrange(home.get_x()-self.image.width, home.get_x()+home.get_width()), random.randrange(home.get_y()-self.image.height, home.get_y()+home.get_height()), batch=antBatch)
		self.sprite.image.anchor_x = self.get_width() / 2
		self.sprite.image.anchor_y = self.get_height() / 2

class Food(Drawable):
	def __init__(self):
		self.image = pyglet.resource.image("food/100.png")

		self.sprite = pyglet.sprite.Sprite(self.image, random.randint(0, screenWidth-self.image.width), random.randint(0, screenHeight-self.image.height), batch=foodBatch)

	def one_less(): # When an ant grabs a piece of food
		pass


class Nest(Drawable): 
	def __init__(self):
		self.image = pyglet.resource.image("ants/nest.png") 
		self.width, self.height = self.image.width, self.image.height
		
		self.sprite = pyglet.sprite.Sprite(self.image, random.randrange(0, screenWidth - self.width), random.randrange(0, screenHeight - self.height))
home = Nest()

ants = []
clouds = []
foods = []
title = Title()

antBatch = pyglet.graphics.Batch()
cloudBatch = pyglet.graphics.Batch()
foodBatch = pyglet.graphics.Batch()

for i in range(0, 8):
	ants.append(Ant())

for i in range(0, 4):
	clouds.append(Cloud())

for i in range(0, 3):
	foods.append(Food())

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
	for ant in ants:
		ant.plus_x = 5 * float(
				math.sin(
					math.radians(
						random.randint(
							int(ant.get_rotation()-20), int(ant.get_rotation()+20)
							))))
		while ant.plus_x == 0:
			ant.plus_x = 5 * float(
					math.sin(
						math.radians(
							random.randint(
								int(ant.get_rotation()-20), int(ant.get_rotation()+20)
								))))

		ant.plus_y = 5 * float(
				math.cos(
					math.radians(
						random.randint(
							int(ant.get_rotation()-20), int(ant.get_rotation()+20)
							))))
		while ant.plus_y == 0:
			ant.plus_y = 5 * float(
					math.cos(
						math.radians(
							random.randint(
								int(ant.get_rotation()-20), int(ant.get_rotation()+20)
								))))

		ant.plus_rotation = math.degrees(math.atan(ant.plus_x/ant.plus_y))
		
		if(ant.plus_y < 0):
			ant.plus_rotation += 180.0

		ant.set_rotation(ant.plus_rotation)
		ant.set_x(ant.get_x() + ant.plus_x)
		ant.set_y(ant.get_y() + ant.plus_y)

		if ant.get_x() < 0:
			ant.set_x(0)
			ant.set_rotation(ant.get_rotation() - 180)
		elif ant.get_y() < 0:
			ant.set_y(0)
		elif ant.get_x() - ant.get_width() < 0:
			ant.set_x(ant.get_width())
			ant.set_rotation(ant.get_rotation() - 180)
		elif ant.get_y() - ant.get_width() < 0:
			ant.set_y(ant.get_width())
			ant.set_rotation(ant.get_rotation() - 180)
		elif ant.get_x() + ant.get_height() / 2 > screenWidth:
			ant.set_x(screenWidth - ant.get_height() / 2)
			ant.set_rotation(ant.get_rotation() - 180)
		elif ant.get_y() + ant.get_height() / 2 > screenHeight:
			ant.set_y(screenHeight - ant.get_height() / 2)
			ant.set_rotation(ant.get_rotation() - 180)

	home.sprite.draw()
	foodBatch.draw()
	antBatch.draw()
	pdb.set_trace()

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

