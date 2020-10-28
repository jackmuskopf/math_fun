import random as r
import numpy as np
import turtle as birds

flock_mean_speed = 300
flock_theta_variance = .3
flock_speed_variance = 10
bird_error_variance = 60
n_birds = 30
v_formation_scale = 30
animation_speed = 100

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

class Bird(object):

    def __init__(self,number,flock):
        self.birdie = birds.Turtle()
        self.birdie.speed(animation_speed)
        self.number = number
        self.flock = flock
        d = (self.number+1)*v_formation_scale

        # spots when Flock.theta = 0
        self.xspot_o = self.flock.offset - d
        self.yspot_o = d if is_even(number) else -1*d

        # effective spots for arbitary theta
        # set in flock.set_spots
        self.xspot = self.xspot_o
        self.yspot = self.yspot_o
        self.x = self.xspot_o
        self.y = self.yspot_o

    def goto(self, x, y):
        self.x = x
        self.y = y
        self.birdie.goto(x,y)



class Flock(object):

    def __init__(self,nbirds,theta=0,speed=flock_mean_speed):
        colors  = ["red","green","blue","orange","purple","pink","yellow"]
        self.nbirds = nbirds
        self.offset = nbirds/2 + 1
        self.birdies = [Bird(j,self) for j in range(nbirds)]
        for bird in self.birdies:
            bird.birdie.color(r.choice(colors))
            bird.birdie.shape('turtle')
        self.theta = theta
        self.speed = speed
        self.x = 0
        self.y = 0
        self.xcoords = None
        self.ycoords = None

        self.past_x = list()
        self.past_y = list()
        self.reset_coords()

    def reset_coords(self):
        positions = [bird.birdie.position() for bird in self.birdies]
        self.xcoords = [p[0] for p in positions]
        self.ycoords = [p[1] for p in positions]
        self.past_x.extend(self.xcoords)
        self.past_y.extend(self.ycoords)
        self.x = sum(self.xcoords)/float(self.nbirds)
        self.y = sum(self.ycoords)/float(self.nbirds)




    def set_spots(self):

        # get birds into V formation
        for bird in self.birdies:

            # rotation matrix
            bird.xspot = np.cos(self.theta)*bird.xspot_o - np.sin(self.theta)*bird.yspot_o
            bird.yspot = np.sin(self.theta)*bird.xspot_o + np.cos(self.theta)*bird.yspot_o



    def move(self,dv=None,dtheta=None):
        
        self.speed  = np.random.normal(flock_mean_speed, flock_speed_variance)
        if dtheta is None:
            dtheta = np.random.normal(0,flock_theta_variance)
        self.theta += dtheta

        self.set_spots()

        flock_xv = self.speed*np.cos(self.theta)
        flock_yv = self.speed*np.sin(self.theta)

        positions = []
        for bird in self.birdies:
            dbx = flock_xv + np.random.normal(0,bird_error_variance)
            dby = flock_yv + np.random.normal(0,bird_error_variance)
            bird.goto(bird.x+dbx,bird.y+dby)


        self.reset_coords()


wn = birds.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(-500,-500,500,500)

flock = Flock(n_birds)
mx = max(flock.xcoords)
ix = min(flock.xcoords)
my = max(flock.ycoords)
iy = min(flock.ycoords)


xs = [flock.x]
ys = [flock.y]

while True:

    flock.move()
    xs.append(flock.x)
    ys.append(flock.y)
    mx = max(flock.past_x)
    ix = min(flock.past_x)
    my = max(flock.past_y)
    iy = min(flock.past_y)
    d = 3*abs(flock.speed)
    wn.setworldcoordinates(ix-d,iy-d,mx+d,my+d)
