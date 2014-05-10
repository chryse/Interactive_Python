import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))

def starting_points(players):
    """Returns a list of random points, one for each player."""
    '''
    points = []
    for player in players:
        point = random_point()
        points.append(point)
        #points += point
    return points
    '''
    return [random_point() for player in players]

players = ["player1", "player2", "player3"]
print starting_points(players)


import simplegui

frame_size = [200, 200]
image_size = [1521, 1818]

def draw(canvas):
    canvas.draw_image(image, image_size,
                      [image_size[0] / 2, image_size[1] / 2],
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

frame.start()
