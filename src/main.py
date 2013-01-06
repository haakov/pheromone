import pyglet


pyglet.resource.path = ["../res"]
pyglet.resource.reindex()

antIdle = pyglet.resource.image("ants/idle.png")


if __name__ == '__main__':
	window = pyglet.window.Window(800, 600, caption="Pheromone")
	window.clear()

	pyglet.app.run()
