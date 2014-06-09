bplist00Ñ_WebMainResourceÕ	
_WebResourceMIMEType_WebResourceTextEncodingName_WebResourceFrameName^WebResourceURL_WebResourceData]text/x-pythonUUTF-8P_Uhttp://codeskulptor-user34.commondatastorage.googleapis.com/user34_8DsstoRVUKqIbzV.pyO«<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;"># Final project for Rice University - RiceRocks (By Marios Mamzeris, May 2014)
# An Introduction to Interactive Programming in Python
# by Joe Warren, Scott Rixner, John Greiner, Stephen Wong
import time
import simplegui
import math
import random

# globals for user interface
WIDTH = 1000
HEIGHT = WIDTH / 1.333333
standard_res = 1000.0
res_factor = WIDTH / standard_res 
score = 0
topscore = 0
lives = 3
ttime = 0.5
rock_speed_factor = 2	# initial value for rock speedup
started = False
paused = False			# checks if game paused
max_missiles = False	# checks if one missile or 3
max_screen_missiles = 15# max number of missiles spawned simultaneously
Max_Big_Rocks = 12		# Max number of rocks in normal game
small_rocks = False		# checks if normal or advanced game
use_small_rock = False	# sets the size of rocks in Sprite
ship_must_glow = False	# when ship has just exploded, for 3 secs it doesn't
ship_crashed = False	# checks if ship crashed
flashing = True
lost_life_msg = False	# checks if ok to show lost life msg
little_ship = 1			# which ship image is initial
which_powerup = None	# power up choice
max_powerups = 1
slowdown = 1			# slowdown factor (used in power up)
has_powerups = True		# Powerups on/off
powerup_message = False	# show power up messages
is_it_the_ship = True	# if ship is checked against collisions
is_it_small_rocks = False # same for small
got_time = False		# used in calculating powerup time
power_time1 = 0			#
power_time2 = 0			#
power_time = False		#
time_for_power = False	#
game_time_played1 = 0	#
game_time_played2 = 0	#
lost_life_time1 = 0
lost_life_time2 = 0
glow_time1 = 0			# used as timers
glow_time2 = 0			#
glow_time11 = 0			#
glow_time22 = 0			#
shield = False
fps_canvas = 60.0		# Used in FPS calulations
fps_time0 = []
fps_time1 = None
system_speed = 60.0		# initial speed factor

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
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
nebula_image1 = simplegui.load_image("http://i.imgur.com/2owoVDY.jpg")
nebula_image2 = simplegui.load_image("http://i.imgur.com/LB70rjC.png")
nebula_image3 = simplegui.load_image("http://i.imgur.com/LfI06P4.jpg")
nebula_image4 = simplegui.load_image("http://i.imgur.com/Y6VhPIF.jpg")
nebula_image5 = simplegui.load_image("http://i.imgur.com/CkfnReb.jpg")
nebula_image6 = simplegui.load_image("http://i.imgur.com/uiY5pY9.jpg")
nebula_image7 = simplegui.load_image("http://i.imgur.com/w9cYJEx.jpg")
nebula_image8 = simplegui.load_image("http://i.imgur.com/SfkHZ3A.jpg")
nebula_image9 = simplegui.load_image("http://i.imgur.com/3pCJ5Cl.jpg")
nebulas = {1:nebula_image2, 2:nebula_image9, 3:nebula_image4, 4:nebula_image1, 5:nebula_image3, 
           6:nebula_image6, 7:nebula_image7, 8:nebula_image8, 9:nebula_image5,}
bg_image_index = 1
new_nebula = False

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 45)
ship_image1 = simplegui.load_image("http://i.imgur.com/k9U0prE.png") #star wars 1
ship_image2 = simplegui.load_image("http://i.imgur.com/OOBSobM.png") #star wars 2
ship_image3 = simplegui.load_image("http://i.imgur.com/MJFiUGj.png") #star wars 3
ship_image4 = simplegui.load_image("http://i.imgur.com/K1bgoG1.png") #Ricerocks originals
spaceships = {1:ship_image1, 2:ship_image2, 3:ship_image3, 4:ship_image4}

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50 * res_factor * (system_speed / 60.0))
missile_image0 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")
missile_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_info2 = ImageInfo([10,10], [20, 20], 3, 60 * res_factor * (system_speed / 60.0))
missile_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")
missiles = {0:missile_image0, 1:missile_image1}
missile_color = 0
            
# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 45)
asteroid_image1 = simplegui.load_image("http://i.imgur.com/ZKUQ1dQ.png")
asteroid_image2 = simplegui.load_image("http://i.imgur.com/TOnxO3W.png")
asteroid_image3 = simplegui.load_image("http://i.imgur.com/xJJKdNn.png")
asteroid_image4 = simplegui.load_image("http://i.imgur.com/eNUGm7N.png")
asteroid_image5 = simplegui.load_image("http://i.imgur.com/S6GZyxv.png")
asteroids = {1:asteroid_image1, 2:asteroid_image2, 3:asteroid_image3, 4:asteroid_image4, 5:asteroid_image5}

# pause button
pause_button_info = ImageInfo([100, 100], [200, 200], 50)
pause_button_image = simplegui.load_image("http://i.imgur.com/qI4lhP1.png")

# power up images
powerup_info = ImageInfo([32, 32], [64, 64], 32, 500)
powerup_image1 = simplegui.load_image("http://i.imgur.com/P7wttnS.png")
powerup_image2 = simplegui.load_image("http://i.imgur.com/LmZktWe.png")
powerup_image3 = simplegui.load_image("http://i.imgur.com/QFfIH7q.png")
powerup_image4 = simplegui.load_image("http://i.imgur.com/XywAwWt.png")
powerups = {1:powerup_image1, 2:powerup_image2, 3:powerup_image3, 4:powerup_image4}
new_powerup = False

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosion_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")
explosion_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")

ship_explosion_info = ImageInfo([50, 50], [100, 100], 5, 80, True)
ship_explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

game_sounds = {'activate_shield': 'k39lx8hb4lv1udq/', 'game_button': 'hfp9fplq47vbouk/','game_laser_shot': 'xta83dzdf2jsfhu/',
         'game_level_up': '4i6ci30wcrjrnrz/', 'game_over': 'rt6dtb6wdsh8t2q/', 'game_pause': 'qzndjj50esbyurr/', 
         'game_power_up': '1p5mdej4fiyja6w/', 'game_start': 'sg66pofp9ww7f1s/', 'missile': 'fu55418mv99fi8g/', 
         'warning_shields_are_down': '4c2jy7aygjw9thu/', 'explosion_blast': 'a9sh6vjygso3hje/'} #sounds from http://www.pond5.com/
      
# load game sounds
def load_sounds():
    dropbox = 'https://dl.dropboxusercontent.com/s/'
    extension = '.mp3'
    for key in game_sounds:
        sound_resource = dropbox + game_sounds[key] + key + extension
        game_sounds[key] = simplegui.load_sound(sound_resource)

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.radius *= res_factor
        
    def draw(self,canvas):
        global flashing
        img_size = list(self.image_size)
        img_size[0] = img_size[0] * res_factor
        img_size[1] = img_size[1] * res_factor  
        if self.thrust and not paused:		# show ship with thrusters
            if not ship_must_glow:
                var_image_center = self.image_center[0] + self.image_size[0], self.image_center[1]
            else:
                if flashing:				# flash ship for 3 secs
                    var_image_center = self.image_center[0] + ( 3 * self.image_size[0]), self.image_center[1]
                    draw_color1 = "rgba(255,255,255,0.2)"
                    draw_color2 = "rgba(130,130,130,0.2)"
                    canvas.draw_circle(self.pos, 70 * res_factor, 7 * res_factor, draw_color1, draw_color1)

                    flashing = not flashing
                else:
                    var_image_center = self.image_center[0] + self.image_size[0], self.image_center[1]
                    flashing = not flashing
        else:								# show ship without thrusters
            if not ship_must_glow:
                var_image_center = self.image_center
            else: 
                if flashing:				# flash ship for 3 secs
                    var_image_center = self.image_center[0] + ( 2 * self.image_size[0]), self.image_center[1]
                    flashing = not flashing
                    draw_color1 = "rgba(255,255,255,0.2)"
                    draw_color2 = "rgba(130,130,130,0.2)"
                    canvas.draw_circle(self.pos, 70 * res_factor, 7 * res_factor, draw_color1, draw_color1)

                else:
                    var_image_center = self.image_center
                    flashing = not flashing
                    
        canvas.draw_image(self.image, var_image_center, self.image_size, self.pos, img_size, self.angle)

    def ship_turn_right(self):					# turn ship clockwise
        self.angle_vel = self.angle_vel + (0.1 / (system_speed / 60.0))

    def ship_turn_left(self):					# turn ship counter clockwise
        self.angle_vel = self.angle_vel - (0.1 / (system_speed / 60.0))

    def ship_stop_turning(self):				# stop turning ship
        self.angle_vel = 0
        
    def ship_thrust_is_on(self):				# turn boolean ship thrust on 
        self.thrust = True

    def ship_thrust_is_off(self):				# turn boolean ship thrust off
        self.thrust = False

    def ship_shoot_missile(self):				# shoot missile
        my_ship.shoot()

    def check_thrusters(self):					# control ship thrust
        if self.thrust:
            acceleration = 0.1 / (system_speed / 60.0)
            forward = angle_to_vector(self.angle)
            ship_thrust_sound.play()
            self.vel[0] += forward[0] * acceleration * res_factor
            self.vel[1] += forward[1] * acceleration * res_factor
        else:
            ship_thrust_sound.rewind()

    def get_ship_position(self):
        return self.pos
    
    def get_ship_vel(self):
        return self.vel

    def get_ship_angle(self):
        return self.angle

    def update(self):
        friction = 0.99
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[0] *= friction
        self.vel[1] *= friction
        self.angle += self.angle_vel
        self.check_thrusters()
        # check if ship moves outside canvas
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
           
    def shoot(self):
        global a_missile, missile_color
        if not started or paused: return
        forward = angle_to_vector(my_ship.angle) 
        if not max_missiles:							# just laser shots
            pos = [0,0]
            vel = [0,0]
            pos[0] = self.pos[0] + (self.radius * forward[0]) * res_factor
            pos[1] = self.pos[1] + (self.radius * forward[1]) * res_factor
            vel[0] = self.vel[0] + 7 * forward[0] 
            vel[1] = self.vel[1] + 7 * forward[1]
            missile_image = missiles[missile_color]
            missile_color += 1
            missile_color %= 2
            a_missile = Sprite(pos, vel, 0, 0, 1, False, missile_image, missile_info, game_sounds['game_laser_shot'])
            missile_group.add(a_missile)
        elif len(missile_group) &lt; max_screen_missiles:	# 3 missiles, up to max_screen_missiles
            pos = [0,0]
            vel = [0,0]
            for i in range(-1, 2): 
                missile_angle = my_ship.angle + (i / 5.0)
                forward = angle_to_vector(missile_angle)
                pos[0] = my_ship.pos[0] + (self.radius * forward[0]) * res_factor
                pos[1] = my_ship.pos[1] + (self.radius * forward[1]) * res_factor
                vel[0] = self.vel[0] + (7 - (i*3) % 6) * forward[0]
                vel[1] = self.vel[1] + (7 - (i*3) % 6) * forward[1]
                a_missile = Sprite(pos, vel, missile_angle, 0, 1, False, missile_image2, missile_info2, game_sounds['missile'])
                missile_group.add(a_missile)

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, how_big, ItsSmallRock, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.ttime = 0
        self.how_big = how_big
        self.is_it_small_rock = ItsSmallRock
        self.radius *= self.how_big
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        img_size = list(self.image_size)
        img_size[0] = img_size[0] * res_factor * self.how_big
        img_size[1] = img_size[1] * res_factor * self.how_big    
        if self.animated:
            if self.image == ship_explosion_image:
                explosion_dim = [9, 9]
                explosion_index = [self.ttime % explosion_dim[0], 
                                   (self.ttime // explosion_dim[0]) % explosion_dim[1]]
                canvas.draw_image(ship_explosion_image, 
                        [self.image_center[0] + explosion_index[0] * self.image_size[0], 
                         self.image_center[1] + explosion_index[1] * self.image_size[1]], 
                         self.image_size, self.pos, img_size)
                if not paused:
                    self.ttime += 1
            else:    
                center = self.image_center
                center = [(self.image_size[0] * self.age) - self.image_size[0]/2, center[1]]
                canvas.draw_image(self.image, center, self.image_size ,self.pos, img_size, self.angle) 
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, img_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.age += 1
        # check if sprite moves outside canvas
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
    
    def get_sprite_image(self, some_sprite):
        return some_sprite.image
    
    def get_sprite_position(self, some_sprite):
        return some_sprite.pos

    def get_sprite_how_big(self, some_sprite):
        return some_sprite.how_big

    def get_is_it_small_rock(self, some_sprite):
        return some_sprite.is_it_small_rock
    
    def set_sprite_position(self, some_sprite, new_pos):
        self.pos = new_pos
            
    def get_sprite_radius(self, some_sprite):
        return some_sprite.radius
    
    def get_sprite_angle(self, some_sprite):
        return some_sprite.angle

    def collide(self, other_object):
        other_pos = self.get_sprite_position(other_object)
        other_radius = self.get_sprite_radius(other_object)
        collision = dist(self.pos, other_pos)  &lt; ((self.radius * res_factor) + (other_radius * res_factor))
        return collision
     
def group_collide(inp_group, any_object, is_it_powerup):
    collisions = False
    for check_object in list(inp_group):
        if check_object.collide(any_object):
            inp_group.remove(check_object)
            collisions = True
            if not is_it_powerup:
                angle = random.randint(0, 10)
                if is_it_the_ship:
                    exploded = Sprite(any_object.get_ship_position(), [0, 0], angle, 0, 2, False, ship_explosion_image, ship_explosion_info, explosion_sound)
                elif is_it_small_rocks:
                    exploded = Sprite(check_object.get_sprite_position(check_object), [0, 0], angle, 0, 1, False, explosion_image2, explosion_info, explosion_sound)
                else:
                    exploded = Sprite(check_object.get_sprite_position(check_object), [0, 0], angle, 0, 1, False, explosion_image1, explosion_info, explosion_sound)
                explosion_group.add(exploded)
                if small_rocks:
                    if not check_object.get_is_it_small_rock(check_object):
                        spawn_smaller_rocks(check_object.get_sprite_position(check_object), check_object.get_sprite_image((check_object)), check_object.get_sprite_how_big((check_object)))             
    return collisions

def group_group_collide(group1, group2):
    global is_it_the_ship
    is_it_the_ship = False
    collisions = 0
    for check_object in list(group2):
        if group_collide(group1, check_object, False):
            group2.discard(check_object)
            collisions += 1
    is_it_the_ship = True
    return collisions

def spawn_smaller_rocks(pos, asteroid_image, asteroid_size):
    global use_small_rock
    r1 = rock_speed_factor * (0 - (5 + (score/50)))	# increasing speed of rocks based on score
    r1 /= slowdown									# decrease with every powerup  
    r2 = abs(r1) + 1        
    vel = [0,0]
    for i in range(random.randint(2,4)):									# Max small Rocks
        vel[0] = float(random.randrange(r1,r2) / 10.0) / (system_speed / 60.0)
        vel[1] = float(random.randrange(r1,r2) / 10.0) / (system_speed / 60.0) 
        angle_vel = float(random.randrange(-5,6, 2) / 100.0) 		# never 0 so always turning
        use_small_rock = True
        rock = Sprite(pos, vel, 0, angle_vel, 0.6 * asteroid_size, True, asteroid_image, asteroid_info)
        rock_small_group.add(rock)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score, bg_image_index, new_nebula, my_ship, little_ship
    #check if splah screen clicked
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    check_size = list(size)
    check_size[0] *= res_factor
    check_size[1] *= res_factor
    inwidth = (center[0] - check_size[0] / 2)  &lt; pos[0] &lt; (center[0] + check_size[0] / 2) 
    inheight = (center[1] - check_size[1] / 2)  &lt; pos[1] &lt; (center[1] + check_size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        bg_image_index = 0
        new_nebula = True
        game_sounds['game_start'].play()
        soundtrack.play()
    #check if little ships on the bottom are clicked
    size = ship_info.get_size()
    check_size = list(size)
    check_size[0] *= res_factor
    check_size[1] *= res_factor
    x = 0	
    for i in spaceships:
        inwidth = (855 * res_factor + (x * (40 * res_factor)) - (35 * res_factor) / 2)  &lt; pos[0] &lt; (855 * res_factor + (x + 1) * (40 * res_factor))
        inheight = (730 * res_factor) - (35 * res_factor) / 2  &lt; pos[1] &lt; (HEIGHT)
        if inwidth and inheight:
           little_ship = i
           game_sounds['game_button'].play()
           my_ship.image = spaceships[i] 
        x += 1
        
# helper function 
def process_sprite_group(inp_set, canvas):
    for sprites in list(inp_set):
        if not paused:
            sprites.update()
            if sprites.age &gt; sprites.lifespan:
                inp_set.remove(sprites)
        sprites.draw(canvas)
        
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, use_small_rock
    if not started or paused: return
    if len(rock_group) &lt; Max_Big_Rocks:	# Max Rocks
        r1 = rock_speed_factor * (0 - (5 + (score/50)))	# increasing speed of rocks based on score
        r1 /= slowdown									# decrease with every powerup  
        r2 = abs(r1) + 1        
        pos = [0,0]
        vel = [0,0]
        angle_vel = float(random.randrange(-5,6, 2) / 100.0) # never 0 so always turning

        # find far place for rock spawn without use of loop
        distance = (my_ship.radius * 5) * res_factor
        height_dist = int((my_ship.radius * 1.5) * res_factor) 
        width_dist = int((my_ship.radius * 1.5) * res_factor)
        x = random.randrange(width_dist, WIDTH - width_dist)
        if x in range(int(my_ship.pos[0] - distance), int(my_ship.pos[0] + distance)):
            y = random.randrange(height_dist, int((my_ship.pos[1] - distance) +  ((HEIGHT - height_dist) - (my_ship.pos[1] + distance))))
            if y &gt; my_ship.pos[1] - distance:
                y = (my_ship.pos[1] + distance) + (y - (my_ship.pos[1] - distance))
        else:
            y = random.randrange(0, HEIGHT)

        pos[0] = x
        pos[1] = y
        vel[0] = float(random.randrange(r1,r2) / 10.0) / (system_speed / 60.0)
        vel[1] = float(random.randrange(r1,r2) / 10.0) / (system_speed / 60.0)
        use_small_rock = False
        asteroid_image = asteroids[random.randint(1,5)]		# pick random asteroid image
        size = random.randrange(7, 10) / 10.0
        rock = Sprite(pos, vel, 0, angle_vel, size, False, asteroid_image, asteroid_info)
        rock_group.add(rock)
        
def explode_all(groups):
    global rock_group, rock_small_group, score
    collisions = 0
    for group in groups:
        for check_object in list(group):
            group.discard(check_object)
            collisions += 1
            angle = random.randint(0, 10)                
            exploded = Sprite(check_object.get_sprite_position(check_object), [0, 0], angle, 0, 1, False, explosion_image3, explosion_info, explosion_sound)
            explosion_group.add(exploded)
    score += collisions  * 10
         
def powerup_spawner():
    global powerup_group, which_powerup
    r1 = -5 #+ (0 - score/40)	# increasing speed of power ups based on score
    r2 = abs(r1) + 1
    pos = [0,0]
    vel = [0,0]
    angle_vel = float(random.randrange(-3,4, 2) / 100.0) # never 0 so always turning
    pos[0] = random.randrange(0,WIDTH)
    pos[1] = random.randrange(0,HEIGHT)
    vel[0] = float(random.randrange(r1,r2) / 10.0) / (system_speed / 60.0)
    vel[1] = float(random.randrange(r1,r2) / 10.0) / (system_speed / 60.0)
    which_powerup = random.randint(1, 4)			# pick random power up
    powerup_image = powerups[which_powerup]		
    if len(powerup_group) &lt; max_powerups:		# Max powerups
        powerup = Sprite(pos, vel, 0, angle_vel, 1, False, powerup_image, powerup_info)
        powerup_group.add(powerup)
        
def pause_game(): # sets the global variable for pause
    global paused
    if started:
        paused = not paused
        if paused:
            soundtrack.pause()
            game_sounds['game_pause'].play()
        else:
            soundtrack.play()

def more_missiles():	# controls if laser or 3 missiles
    global max_missiles
    max_missiles = not max_missiles

def switch_powerups():	# switch for powerups on/off
    global has_powerups
    has_powerups = not has_powerups

def change_level():		# turns small rocks on/off
    global small_rocks, Max_Big_Rocks
    small_rocks = not small_rocks
    if small_rocks:
        Max_Big_Rocks = 4	# max big rocks when game is in advance mode
    else:
        Max_Big_Rocks = 12	# max big rocks when game is in normal mode
    
def keydown(key):
    global canvas
    inputs = {"up" : my_ship.ship_thrust_is_on, "right": my_ship.ship_turn_right,
              "left":my_ship.ship_turn_left, "space":my_ship.ship_shoot_missile,
              "p":switch_powerups, "m":more_missiles, "l":change_level}
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
             inputs[i]()
        if key == 27:
            pause_game()

def keyup(key): 
    inputs = {"up" : my_ship.ship_thrust_is_off, "right": my_ship.ship_stop_turning,
              "left":my_ship.ship_stop_turning}
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i]()

def dummy():
    pass
  
def show_powerup_msg(powerup):
    msgs = {'1': "- HYPER BLAST -", '2': "- EXTRA LIFE -", 
            '3': "- SHIELDS ARE UP -", '4':"- SLOW DOWN -"}
    message = msgs.get(powerup)
    return message
        
    
        
#**********************************************************************************

class Game:
    def __init__(self):
        global WIDTH, HEIGHT
        self.frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(keydown)
        self.frame.set_keyup_handler(keyup)
        self.frame.set_mouseclick_handler(click)
        self.frame.add_button("Pause &lt;press ESC&gt;", pause_game, 200)
        self.frame.add_button("Toggle missiles &lt;press M&gt;", more_missiles, 200)
        self.frame.add_button("Advanced level: Rocks break in smaller pieces (2-4) &lt;press L&gt;", change_level, 200)
        self.frame.add_label("")
        self.frame.add_button("Canvas size: " + str(WIDTH), dummy, 200)
        self.frame.add_button("Enter canvas size (600-1200) and press &lt;enter&gt;", dummy, 200)
        self.frame.add_input("", self.input_size, 200)
        self.frame.add_label("")

        self.frame.add_button("Power ups: Shield, Extra life, Slow down rocks, Hyper blast &lt;press P&gt;", switch_powerups, 200)
        self.frame.add_label("")
        #self.frame.add_label("")

        self.frame.add_button("Rock speed factor: " + str(rock_speed_factor), dummy, 200)
        self.frame.add_button("Enter new value (1-5) and press &lt;enter&gt;", dummy, 200)
        self.frame.add_input("", self.input_rock_speed_factor, 200)

        self.timer = simplegui.create_timer(1000.0, rock_spawner)
        self.timer.start()
        self.frame.start()
        HEIGHT = int(WIDTH / 1.333)

        
    def frames_per_second():
        global fps_canvas, fps_time0, fps_time1
        gettime = time.time()
        fps_time0.append(gettime - fps_time1)
        fps_time1 = gettime
        fps_canvas = len(fps_time0) / sum(fps_time0)
        if len(fps_time0) &gt;= 60: 
            fps_time0.pop(0)
        
    def get_fps():
        global fps_time1
        fps_time1 = time.time()
        Game.get_fps = Game.frames_per_second
        
    def fix_positions(self, groups, oldwidth, oldheight):
        for group in groups:
            for item in list(group):
                    new_pos = [0,0]
                    old_pos = item.get_sprite_position(item)
                    new_pos[0] = old_pos[0] / (oldwidth/WIDTH)
                    new_pos[1] = old_pos[1] / (oldheight/HEIGHT)
                    item.set_sprite_position(item, new_pos)       

    def input_rock_speed_factor(self, value):
        global rock_speed_factor
        # checks if input is numbers only and within range  
        if  value.isdigit() and int(value) in range(1,6): 
            rock_speed_factor = int(value)
            self.frame.stop()
            Game()
                    
    def input_size(self, size):
        global WIDTH, HEIGHT, res_factor
        # checks if input is numbers only and within range  
        if  size.isdigit() and int(size) in range(600,1201): 
            oldwidth = float(WIDTH)
            oldheight = float(HEIGHT)
            WIDTH = int(size)
            HEIGHT = int(WIDTH / 1.333)
            res_factor = WIDTH / standard_res
            #re-arange positions for all items to match new canvas
            self.fix_positions([rock_group, rock_small_group, missile_group, powerup_group, explosion_group], oldwidth, oldheight)
            # re-arange ship's position to match new canvas
            my_ship.pos[0] = my_ship.pos[0] / (oldwidth/WIDTH)
            my_ship.pos[1] = my_ship.pos[1] / (oldheight/HEIGHT)            
            self.frame.stop()
            Game()
                      
    def draw(self, canvas):
        global ttime, started, lives, score, topscore, rock_group, rock_small_group, missile_group, is_it_small_rocks
        global powerup_group, WIDTH, HEIGHT, bg_image_index, new_nebula, ship_must_glow, ship_crashed, fps_canvas
        global slowdown, powerup_message, got_time, power_time1, power_time2, shield, has_powerups
        global power_time, time_for_power, game_time_played1, game_time_played2, lost_life_msg, system_speed
        global lost_life_time1, lost_life_time2, glow_time1, glow_time2, glow_time11, glow_time22

        Game.get_fps()
        # animate background
        if not paused: 
            ttime += 1
        wtime = (ttime / 4) % WIDTH
        center = debris_info.get_center()
        size = debris_info.get_size()
        if score % 250 == 0:	# changes bg image every 250 points
            if new_nebula:
                bg_image_index = 1 + bg_image_index % len(nebulas) #max nebulas
                if score &gt; 0:
                    lives += 1
                    game_sounds['game_level_up'].play()
                new_nebula = False
        else:
            new_nebula = True
        nebula_image = nebulas[bg_image_index]
        canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
        canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
        canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
        # draw ship and sprites
        my_ship.draw(canvas)
        process_sprite_group(rock_group, canvas) 		# updates and draws rocks
        process_sprite_group(powerup_group, canvas) 	# updates and draws powerups
        process_sprite_group(rock_small_group, canvas)  # updates and draws small rocks
        process_sprite_group(missile_group, canvas)		# updates and draws missiles
        process_sprite_group(explosion_group, canvas)	# updates and draws explosions
    
        if not paused:
            if not ship_must_glow:
                if group_collide(rock_group, my_ship, False) or group_collide(rock_small_group, my_ship, False):
                    lives -= 1
                    lost_life_msg = True
                    lost_life_time1 = time.time()
                    game_sounds['activate_shield'].play()
                    ship_crashed = True
            elif not lost_life_msg and started:
                    draw_color = "rgba(130,130,130,0.5)"
                    middle = self.frame.get_canvas_textwidth(str(7 - (int(glow_time22 - glow_time11))), 400 * res_factor)
                    canvas.draw_text(str(7 - (int(glow_time22 - glow_time11))), 
                                     [(WIDTH / 2) - (middle / 2) * res_factor, 
                                     (HEIGHT / 2) + (middle / 2) * res_factor], 
                                     400 * res_factor, draw_color)
                    
            if ship_crashed:
                glow_time1 = time.time()
                ship_must_glow = True
                ship_crashed = False
            elif shield == None:
                glow_time2 = time.time()
                if glow_time2 &gt; glow_time1 + 2: # seconds
                    ship_must_glow = False
                        
            if lost_life_msg:
                lost_life_time2 = time.time()
                if lost_life_time2 &lt; lost_life_time1 + 2: # seconds
                    middle = self.frame.get_canvas_textwidth("- YOU LOST A LIFE -", 22 * res_factor)
                    canvas.draw_text("- YOU LOST A LIFE -", [((WIDTH / 2) - (middle / 2) * res_factor) - 1, 635 * res_factor], 22 * res_factor, "Blue")
                    canvas.draw_text("- YOU LOST A LIFE -", [(WIDTH / 2) - (middle / 2) * res_factor, 635 * res_factor], 22 * res_factor, "Silver")
                else:
                    lost_life_msg = False
            # check power ups
            if not power_time:
                game_time_played1 = time.time()
                power_time = True
                time_for_power = False
            else:
                game_time_played2 = time.time()
                power_spawn_seconds = random.randint(5, 10)
                if game_time_played2 &gt; game_time_played1 + power_spawn_seconds:  #seconds
                    power_time = False
                    time_for_power = True  
           
            if score &gt; 0 and time_for_power and len(powerup_group) == 0 and not powerup_message and started and has_powerups: 
                powerup_spawner()
                power_time = False

            if len(powerup_group) &gt; 0:
                if group_collide(powerup_group, my_ship, True): 
                    powerup_message = True
                    game_sounds['game_power_up'].play()
                    
                    if which_powerup == 1:
                        explode_all([rock_group, rock_small_group])
                        
                    elif which_powerup == 2:
                        lives += 1
                        game_sounds['game_level_up'].play()
                        
                    elif which_powerup == 3:
                        game_sounds['activate_shield'].play()
                        shield = True
                        
                    elif which_powerup == 4:
                        slowdown += 1

            if shield:
                glow_time11 = time.time()
                ship_must_glow = True
                shield = False
            elif shield == False:
                glow_time22 = time.time()
                if glow_time22 &gt; glow_time11 + 7: # seconds
                    ship_must_glow = False
                    if which_powerup &lt;&gt; None:
                        game_sounds['warning_shields_are_down'].play()
                    shield = None	#prevent first time
                                    
            if powerup_message:
                message = show_powerup_msg(str(which_powerup))
                middle = self.frame.get_canvas_textwidth(message, 22 * res_factor)
                canvas.draw_text(message, [((WIDTH / 2) - (middle / 2) * res_factor) - 3, 675 * res_factor], 22 * res_factor, "Blue")
                canvas.draw_text(message, [(WIDTH / 2) - (middle / 2) * res_factor, 675 * res_factor], 22 * res_factor, "Silver")

                #check if 2 secs will pass before powerup msg is disabled
                if not got_time:
                    power_time1 = time.time()
                    got_time = True
                else:
                    power_time2 = time.time()
                    if power_time2 &gt; power_time1 + 2: # seconds
                        powerup_message = False
                        got_time = False
                        
            if lives == 0:
                if started:
                    game_sounds['game_over'].play()
                started = False
                lost_life_msg = False
                powerup_message = False
                rock_group = set([])
                powerup_group = set([])
                rock_small_group = set([])
                soundtrack.pause()
                middle = self.frame.get_canvas_textwidth("GAME OVER", 120 * res_factor)
                draw_color = "rgba(130,130,130,0.3)"
                canvas.draw_text("GAME OVER", [(WIDTH / 2) - (middle / 2), (HEIGHT / 2) + (305 * res_factor)], 120 * res_factor, draw_color)
                canvas.draw_text("NO MORE SHIPS", [120 * res_factor, 735 * res_factor], 18 * res_factor, "White")

            score += group_group_collide(rock_group, missile_group) * 10
            is_it_small_rocks = True
            score += group_group_collide(rock_small_group, missile_group) * 10
            is_it_small_rocks = False
            if score &gt; topscore:
                topscore = score
    
            # update ship and sprites
            my_ship.update()
        else:
            ship_thrust_sound.rewind()
            
        # draw splash screen if not started
        img_size = list(splash_info.get_size())
        img_size[0] = img_size[0] * res_factor
        img_size[1] = img_size[1] * res_factor      
        if not started:
            draw_color = "rgba(255,0,0,0.3)"
            canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), 
                              [WIDTH / 2, HEIGHT / 2], img_size)
            middle = self.frame.get_canvas_textwidth("USE LEFT &amp; RIGHT TO TURN, UP FOR THRUST", 45 * res_factor)
            canvas.draw_text("USE LEFT &amp; RIGHT TO TURN, UP FOR THRUST", 
                             [(WIDTH / 2) - (middle / 2) - 2 * res_factor, (HEIGHT / 2) - 248 * res_factor], 45 * res_factor, draw_color)        
            middle = self.frame.get_canvas_textwidth("Press SPACE to shoot missile(s)", 55 * res_factor)
            canvas.draw_text("Press SPACE to shoot missile(s)", 
                             [(WIDTH / 2) - (middle / 2) - 2 * res_factor, (HEIGHT / 2) - 198 * res_factor], 55 * res_factor, draw_color)
            draw_color = "rgba(255,255,255,0.5)"
            middle = self.frame.get_canvas_textwidth("USE LEFT &amp; RIGHT TO TURN, UP FOR THRUST", 45 * res_factor)
            canvas.draw_text("USE LEFT &amp; RIGHT TO TURN, UP FOR THRUST", 
                             [(WIDTH / 2) - (middle / 2), (HEIGHT / 2) - 250 * res_factor], 45 * res_factor, draw_color)        
            middle = self.frame.get_canvas_textwidth("Press SPACE to shoot missile(s)", 55 * res_factor)
            canvas.draw_text("Press SPACE to shoot missile(s)", 
                             [(WIDTH / 2) - (middle / 2), (HEIGHT / 2) - 200 * res_factor], 55 * res_factor, draw_color)
        elif paused:
            img_size = list(pause_button_info.get_size())
            img_size[0] = img_size[0] * res_factor
            img_size[1] = img_size[1] * res_factor

            canvas.draw_image(pause_button_image, pause_button_info.get_center(), 
                              pause_button_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                              img_size)
            draw_color = "rgba(130,130,130,0.3)"
            middle = self.frame.get_canvas_textwidth("GAME PAUSED", 120 * res_factor)
            canvas.draw_text("GAME PAUSED", [(WIDTH / 2) - (middle / 2), (HEIGHT / 2) + (305 * res_factor)], 120 * res_factor, draw_color)

        # draw score &amp; lives
        draw_color = "rgba(0, 0, 0, 0.4)"
        canvas.draw_line([0, 731 * res_factor],[WIDTH, 731 * res_factor], 44 * res_factor, draw_color)
        canvas.draw_line([0, 20 * res_factor],[WIDTH, 20 * res_factor], 48 * res_factor, draw_color)
        draw_color = "rgba(55, 251, 55, 0.7)"    
        system_speed = fps_canvas
        canvas.draw_text("|  FPS: " + "%.1f" % system_speed, [555 * res_factor, 30 * res_factor], 18 * res_factor, draw_color)    
        draw_color = "rgba(55, 251, 55, 0.7)" 
        canvas.draw_text("LIVES:", [40 * res_factor, 735 * res_factor], 18 * res_factor, draw_color)
        x = 0
        for i in range(lives):				# draws little ships as lives left
                pos = [120 * res_factor  + (x * (35 * res_factor)), 730 * res_factor]
                x += 1
                img_size = [35 * res_factor, 35 * res_factor]
                if x &lt;= 17:	# limit to as many ships fit in screen
                    canvas.draw_image(spaceships[little_ship], [135,45], [90, 90], pos, img_size)
        if max_missiles:
            level = "ON"
        else:
            level = "OFF"
        draw_color = "rgba(255, 255, 255, 0.7)" 
        canvas.draw_text("TOP SCORE:  " + "%.5d" % topscore, [WIDTH - (320 * res_factor), 30 * res_factor], 18 * res_factor, draw_color)
        canvas.draw_text("SCORE:  " + "%.5d" % + score, [WIDTH - (130 * res_factor), 30 * res_factor], 18 * res_factor, draw_color)
        draw_color = "rgba(255, 255, 0, 0.7)"            
        canvas.draw_text("Missiles: " + level, [40 * res_factor, 30 * res_factor], 18 * res_factor, draw_color)
        middle = self.frame.get_canvas_textwidth('TOP SCORE:  ' + str(topscore), 18 * res_factor)
        canvas.draw_line([0, 45 * res_factor],[WIDTH, 45 * res_factor], 1, "Gray")
        if not small_rocks:
            level = "NORMAL"
        else:
            level = "ADVANCED"
        canvas.draw_text("|  Level: " + level, [150 * res_factor, 30 * res_factor], 18 * res_factor, draw_color)
        if has_powerups:
            level = "ACTIVATED"
        else:
            level = "DEACTIVATED"
        canvas.draw_text("|  Power-ups: " + level, [320 * res_factor, 30 * res_factor], 18 * res_factor, draw_color)

        canvas.draw_line([0, 710 * res_factor],[WIDTH, 710 * res_factor], 1, "Gray")
        draw_color = "rgba(55, 251, 55, 0.7)"
        canvas.draw_text("Pick you ship:", [715 * res_factor, 735 * res_factor], 18 * res_factor, draw_color)
        x = 0
        for i in spaceships:				# draws little icons to pick spaceship
            pos = [855 * res_factor  + (x * (40 * res_factor)), 730 * res_factor]
            x += 1
            img_size = [35 * res_factor, 35 * res_factor]
            canvas.draw_image(spaceships[i], [45,45], [90, 90], pos, img_size)
        # calculate &amp; draw green box around little ships bottom right corner
        posx1 = 809 * res_factor + (little_ship * (40 * res_factor) - (10* res_factor))
        posx2 = 809 * res_factor + ((little_ship + 1) * (40 * res_factor) - (10* res_factor))
        posy1 = 748 * res_factor
        posy2 = 712 * res_factor
        
        canvas.draw_polyline([[posx1, posy2], [posx2, posy2], [posx2, posy1]], 2, 'Lime')
        canvas.draw_polyline([[posx2, posy1], [posx1, posy1], [posx1, posy2]], 2, 'Lime')
#**********************************************************************************

# initialize ship, rocks, missiles and explosions
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image1, ship_info)
rock_group = set([])
powerup_group = set([])
rock_small_group = set([])
missile_group = set([])
explosion_group = set([])

# get things rolling
load_sounds()
Game()</pre></body></html>    ( > \ s ‚ ” ¢ ¨ ©                           ¬!