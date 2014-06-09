# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800    
HEIGHT = 600
SHIP_SPEED = 0.1
MISSILE_SPEED = 5
FRICTION = 0.01
ANGLE_CHANGE = 0.07
MISSILE_LIFESPAN = 80
ASTEROID_LIFESPAN = float("inf")
HOW_MANY_ROCKS = 12
ROCK_SPAWN_TIME = 1000.0
GAME_OVER_TIME = 180
INVINCIBLE_TIME = 180
SHIP_DIM = 3
EXPLOSION_DIM = 24


score = 0
lives = 3
time = 0.5
game_started = False
game_over = False
game_over_time = 180
invincible = False
invincible_time = 180
level = 1
angle_level = 0.1
bonus_life = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float("inf")
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# game over image
gameover_info = ImageInfo([200, 150], [400, 300])
gameover_image = simplegui.load_image("http://hyunjunkim.com/images/ricerocks/gameover.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://hyunjunkim.com/images/ricerocks/double_ship.png")

# ship blinking
ship_blinking_info = ImageInfo([45, 45], [90, 90], 35)
ship_blinking_image = simplegui.load_image("http://hyunjunkim.com/images/ricerocks/ship_blinking.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, MISSILE_LIFESPAN)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40, ASTEROID_LIFESPAN)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
#asteroid_info = ImageInfo([64, 64], [128, 128], 40, ASTEROID_LIFESPAN)
#asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.4)
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound.set_volume(.5)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.set_volume(.5)

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def process_sprite_group(group, canvas):
    for element in list(group):
        if not element.is_died():
            element.draw(canvas)
        else:
            group.discard(element)
        # explosion detection & draw
        if element.animated:
            element.draw(canvas)

# collision detections            
def group_collide(group, sprite):
    global explosion_group, invincible
    how_many = 0
    for element in list(group):
        if element.collide(sprite):
            element.animated = True
            sprite.animated = True
            #explosion_group.add(element)
            #explosion_group.add(sprite)
            rock_exp = Explosion(element.pos, element.vel, element.angle, element.angle_vel, explosion_image, explosion_info, explosion_sound)
            ship_exp = Explosion(sprite.pos, sprite.vel, sprite.angle, sprite.angle_vel, explosion_image1, explosion_info)
            explosion_group.add(rock_exp)
            explosion_group.add(ship_exp)
            group.remove(element)
            invincible = True
            how_many += 1
    return how_many

def group_group_collide(group1, group2):
    global explosion_group
    how_many = 0
    for element1 in list(group1):
        for element2 in list(group2):
            if element1.collide(element2):
                element2.animated = True
                #explosion_group.add(element2)
                rock_exp = Explosion(element2.pos, element2.vel, element2.angle, element2.angle_vel, explosion_image, explosion_info, explosion_sound)
                explosion_group.add(rock_exp)
                #element1.age = element1.lifespan
                #element2.age = element2.lifespan
                group1.discard(element1) 
                group2.discard(element2)                  
                how_many += 1                
    return how_many                
   
# draw background
def draw_background(canvas):
    global time
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

# draw splash screen if not started
def draw_splash(canvas):
    if not game_started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    
# restart game
def restart():
    global score, lives, time, game_started, game_over, my_ship, rock_set, missile_set, explosion_set, invincible, invincible_time, level, angle_level
    score = 0
    lives = 3
    #time = 0.5
    level = 1
    angle_level = 0.1
    game_started = False
    game_over = False
    invincible = False
    invincible_time = INVINCIBLE_TIME
    my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], -1.57079, ship_image, ship_info)
    rock_set = set([])
    missile_set = set([])
    explosion_set = set([])
    soundtrack.rewind()
    
# game level chagne
def level_change():
    global level, angle_level
    global bonus_life
    if score == 25:
        level = 2
        angle_level = 0.2
        #bonus_life = True
        #get_bonus_life(bonus_life)
    elif score == 50:
        level = 3
        angle_level = 0.2
    elif score == 75:
        level = 4
        angle_level = 0.3
    elif score == 100:
        level = 5
        angle_level = 0.3
    elif score == 125:
        level = 6
        angle_level = 0.5
    elif score == 150:
        level = 7
        angle_level = 0.5
    
# get bonus life
def get_bonus_life(on):
    if on:
        global lives
        lives += 1
        on = False
            
            
    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.thrust = False
        self.animated = info.get_animated()
        
    def draw(self,canvas):
        global invincible, invincible_time
        
        # normal draw
        if not self.thrust and not invincible:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
        # normal but blinking draw
        elif not self.thrust and invincible:
            index = (invincible_time % SHIP_DIM) // 1
            canvas.draw_image(self.image,  
                        [self.image_center[0] + index * self.image_size[0] * 2, self.image_center[1]], 
                        self.image_size, self.pos, self.image_size, self.angle)    
        # thrust on draw    
        elif self.thrust and not invincible:
            canvas.draw_image(self.image, [self.image_center[0]+ self.image_size[0], self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        
        # thrust on and blinking draw
        elif self.thrust and invincible:
            index = (invincible_time % SHIP_DIM) // 1
            canvas.draw_image(self.image,  
                        [(self.image_center[0] + self.image_size[0]) + index * self.image_size[0] * 2, self.image_center[1]], 
                        self.image_size, self.pos, self.image_size, self.angle)                    
        if invincible:   
            invincible_time -= .4
            if invincible_time <= 0:
                invincible = False
                invincible_time = INVINCIBLE_TIME          
                      
    def update(self):
        # position update
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]        
        self.angle += self.angle_vel
        
        # friction update
        self.vel[0] *= (1 - FRICTION)
        self.vel[1] *= (1 - FRICTION)
        
        # thrust update
        acc = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += acc[0] * SHIP_SPEED
            self.vel[1] += acc[1] * SHIP_SPEED
            
        # boundary check
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
    
    # thrust sound set
    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
            
    def shoot(self):
        #global a_missile
        global missile_set
        forward = angle_to_vector(self.angle)
        
        # initial missile position
        missile_x_pos = self.pos[0] + forward[0] * self.image_center[0]
        missile_y_pos = self.pos[1] + forward[1] * self.image_center[1]
        missile_pos = [missile_x_pos, missile_y_pos]
        # missile velocities
        missile_x_vel = self.vel[0] + forward[0] * MISSILE_SPEED
        missile_y_vel = self.vel[1] + forward[1] * MISSILE_SPEED
        missile_vel = [missile_x_vel, missile_y_vel]
        missile_set.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound))                
        
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.animated_time = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):            
        # position update
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]        
        self.angle += self.angle_vel
        
        # boundary check
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        
        # age increase
        self.age += 1
              
    def is_died(self):
        if self.age <= self.lifespan:
            return False
        else:
            return True
        
    def collide(self, other):
        distance =  dist(self.pos, other.pos)
        if distance < self.radius + other.radius:
            return True
        else:
            return False
        

class Explosion(Sprite):
    # override draw method
    def draw(self, canvas):
        explosion_index = (self.animated_time % EXPLOSION_DIM) // 1
        self.animated_time += .5
    
        canvas.draw_image(self.image, 
                        [self.image_center[0] + explosion_index * self.image_size[0], self.image_center[1]], 
                        self.image_size, self.pos, self.image_size)
        
        if self.animated_time >= EXPLOSION_DIM:            
            my_ship.animated = False
            explosion_group.discard(self)


# draw handler           
def draw(canvas):
    global my_ship, lives, score, game_started, game_over, game_over_time

    # animiate background
    draw_background(canvas)
    
    #draw splash
    draw_splash(canvas)
    
    if game_started:
        # start rock spawn
        timer.start()
        
        # draw ship and sprites
        if not my_ship.animated: my_ship.draw(canvas)             
        process_sprite_group(rock_set, canvas)        
        process_sprite_group(missile_set, canvas)
        process_sprite_group(explosion_group, canvas)
                    
        # update ship and sprites
        my_ship.update()              
        for rock in rock_set:
            rock.update()           
        for missile in missile_set:
            missile.update()
        for explosion in explosion_group:
            explosion.update()
                        
        # ship and rocks collision detection and return lives
        if not invincible:
            lives -= group_collide(rock_set, my_ship)    
        
        # missiles and rocks collision detection and return score
        score += group_group_collide(missile_set, rock_set)
                
        for sprite in explosion_group:
            if sprite.animated:
                pass                
                #explode(sprite, canvas)
              
        # draw life and score boards
        canvas.draw_text("Lives", [50, 50], 20, "White", "monospace")
        canvas.draw_text(str(lives), [50, 70], 20, "White", "monospace")
        canvas.draw_text("Score", [700, 50], 20, "White", "monospace")
        canvas.draw_text(str(score), [700, 70], 20, "White", "monospace")
        
        if lives <= 0:
            timer.stop()
            ship_thrust_sound.rewind()
            ship_thrust_sound.pause()
            my_ship.vel = [0, 0]
            for rock in rock_set:
                rock.vel = [0, 0]
            game_over = True
            game_over_time -= 1

            canvas.draw_image(gameover_image, gameover_info.get_center(), 
                          gameover_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          gameover_info.get_size())

            if game_over_time < 0:
                game_over_time = GAME_OVER_TIME
                restart()
        
        # game level change
        level_change()
                    
   
            
# timer handler that spawns a rock    
def rock_spawner():
    a_rock_center = asteroid_info.get_center()
    random_x_pos = random.randint(a_rock_center[0], WIDTH - a_rock_center[0])
    random_y_pos = random.randint(a_rock_center[1], HEIGHT - a_rock_center[1])
    rock_pos = [random_x_pos, random_y_pos]
    random_x_vel = random.choice([-1, 1]) * random.random() * level
    random_y_vel = random.choice([-1, 1]) * random.random() * level
    rock_vel = [random_x_vel, random_y_vel]
    rock_angle = 0
    rock_angle_vel = random.random() * random.choice([-1, 1]) * angle_level
    a_rock = Sprite(rock_pos, rock_vel, rock_angle, rock_angle_vel, asteroid_image, asteroid_info)        
        
    # prevent duplicate positions of rock and ship
    distance = dist(my_ship.pos, rock_pos)
    if distance > (a_rock.radius + my_ship.radius + 10):     
        # limit amount of rocks
        if len(rock_set) <= HOW_MANY_ROCKS:
            rock_set.add(a_rock)           
    
# keyboard event handlers
def keydown(key):
    if game_started and not game_over:
        if key == simplegui.KEY_MAP["left"]:
            my_ship.angle_vel = -ANGLE_CHANGE
        elif key == simplegui.KEY_MAP["right"]:
            my_ship.angle_vel = ANGLE_CHANGE
        elif not my_ship.animated:    
            if key == simplegui.KEY_MAP["up"]:
                my_ship.set_thrust(True)
            elif key == simplegui.KEY_MAP["space"]:
                my_ship.shoot()
                            
def keyup(key):
    if game_started:
        if key == simplegui.KEY_MAP["left"]:
            my_ship.angle_vel = 0
        elif key == simplegui.KEY_MAP["right"]:
            my_ship.angle_vel = 0
        elif key == simplegui.KEY_MAP["up"]:
            my_ship.set_thrust(False)

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global game_started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not game_started) and inwidth and inheight:
        game_started = True
        soundtrack.play()
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], -1.57079, ship_image, ship_info)
rock_set = set([])
missile_set = set([])
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

#frame.add_button("Restart", restart, 100)

# Tutorial
description = frame.add_label("Welcome to the RiceRocks!")
descr = frame.add_label(" ")
description2 = frame.add_label("Game Control Keys:")
description21 = frame.add_label("[UP ARROW] - to thrust the ship")
description3 = frame.add_label("[LEFT ARROW] - to turn the ship clockwise") 
description31 = frame.add_label("[RIGHT ARROW] - to turn the ship counter-clockwise")
description4 = frame.add_label("[SPACEBAR] - to shoot a missile")
descr = frame.add_label(" ")
description1 = frame.add_label("Blast the Rocks off, earn the points and enjoy.")

timer = simplegui.create_timer(ROCK_SPAWN_TIME, rock_spawner)

# get things rolling
frame.start()
